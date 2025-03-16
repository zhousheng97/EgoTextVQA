import openai
from openai import OpenAI
import os
import argparse
import json
import ast


def ensure_json_file_exists(file_path):
    """
    Ensures that the specified JSON file exists. If it does not exist, creates it with an empty list and logs the creation.
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w') as json_file:
            json.dump([], json_file)
        with open('log.txt', 'w') as log_file:
            log_file.write("The file does not exist, has been created and assigned: []")


def read_json_file(file_path):
    """
    Reads and returns the contents of the JSON file if it exists; otherwise, returns an empty list.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []


def write_json_file(file_path, data):
    """
    Writes the provided data to the specified JSON file with indentation.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def update_json_file(file_path, existing_data, pair):
    """
    Appends the pair to the existing data if it does not already exist and updates the JSON file.
    Also logs the update.
    """
    if pair not in existing_data[0]['data']:
        existing_data[0]['data'].append(pair)
        write_json_file(file_path, existing_data)
        with open('log.txt', 'w') as log_file:
            log_file.write("New data added to the JSON file.")
    else:
        print("Data already exists in the JSON file.")


def remove_special_characters(text):
    """
    Removes newline characters from the provided text.
    """
    cleaned_text = text.replace("\n", "")
    return cleaned_text


def annotate(model_name, qa_set):
    """
    Evaluates the question-answer pair using GPT-4o-mini and returns a dictionary containing:
    - 'pred': a string 'yes' or 'no' indicating correctness.
    - 'score': an integer between 0 and 5 indicating the meaningful match.
    """
    api_key = "enter-your-key"
    api_base = "https://api.openai.com/v1"
    client = OpenAI(api_key=api_key, base_url=api_base)

    question = qa_set['q']
    answer = qa_set['a']
    model_pred = qa_set[model_name]
    response_dict = {}
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content":
                        "You are an intelligent chatbot designed for evaluating the correctness of generative outputs for question-answer pairs. "
                        "Your task is to compare the predicted answer with the correct answer and determine if they match meaningfully. Here's how you can accomplish the task:"
                        "------"
                        "##INSTRUCTIONS: "
                        "- Focus on the meaningful match between the predicted answer and the correct answer. "
                        "Please note that not only matches of noun phrases between answers, but also matches of prepositional phrases. "
                        "For example, \"at the car wash on your right\" does not exactly match \"car wash\". "
                        "\"at the gas station beside the sign 'gas sale'\" does not exactly match \"gas station\".\n"
                        "- Consider synonyms or paraphrases as valid matches. "
                        "Note that the predicted answer must be consistent with the string type of the correct answer, which may include phone numbers, email addresses, numbers, dates, etc. "
                        "For example, the string types of \"www.usps.com\" and \"visit their website\" are inconsistent, "
                        "and the string types of \"9849041316\" and \"advertiser's contact number\" are inconsistent.\n"
                        "- Evaluate the correctness of the prediction compared to the answer."
                },
                {
                    "role": "user",
                    "content":
                        "Please evaluate the following video-based question-answer pair:\n\n"
                        f"Question: {question}\n"
                        f"Correct Answer: {answer}\n"
                        f"Predicted Answer: {model_pred}\n\n"
                        "Provide your eval_code only as a yes/no and score where the score is an integer value between 0 and 5, with 5 indicating the highest meaningful match. "
                        "Please generate the response in the form of a Python dictionary string with keys 'pred' and 'score', where value of 'pred' is a string of 'yes' or 'no' and value of 'score' is in INTEGER, not STRING. "
                        "DO NOT PROVIDE ANY OTHER OUTPUT TEXT OR EXPLANATION. Only provide the Python dictionary string. "
                        "For example, your response should look like this: {'pred': 'yes', 'score': 5}, {'pred': 'no', 'score': 1}."
                }
            ],
            stream=False,
        )
        response_message = response.choices[0].message.content
        response_dict = ast.literal_eval(response_message)
    except Exception as e:
        print("Error processing:", e)
    return response_dict


def print_score(model):
    """
    Iterates through each sample in the prediction file, evaluates the QA pair using annotate(),
    and updates the output JSON file accordingly.
    """
    args = parse_args()

    with open(args.pred_path, 'r') as file:
        pred_contents = json.load(file)

    new_pred_contents = pred_contents.copy()
    for sample in new_pred_contents[0]['data']:
        q_id = sample['question_id']
        v_id = sample['video_id']

        q = sample['question']
        a = remove_special_characters(str(sample["correct_answer"])).lower()
        sample["correct_answer"] = a
        sample[model] = remove_special_characters(str(sample[model])).lower()
        qa_set = {"q": q,
                  "a": a,
                  model: sample[model]
                  }

        ensure_json_file_exists(args.output_json)
        existing_data = read_json_file(args.output_json)

        question_id = sample['question_id']
        video_id = sample['video_id']
        if existing_data:
            exists = any(item['question_id'] == question_id and item['video_id'] == video_id for item in existing_data[0]['data'])
            if exists:
                with open('log.txt', 'w') as log_file:
                    log_file.write(f"video_id: {video_id}, question_id: {question_id} already exists")
                continue
            else:
                print(f"video_id: {video_id}, question_id: {question_id} does not exist")

        score_dict = annotate(model, qa_set)
        sample['acc'] = score_dict.get('pred', 'no')
        sample['score'] = score_dict.get('score', 0)

        if not existing_data:
            content = {}
            content['dataset'] = pred_contents[0].get('dataset', '')
            content['split'] = pred_contents[0].get('split', '')
            content['task setting'] = pred_contents[0].get('task setting', '')
            content['data'] = []
            existing_data.append(content)

        update_json_file(args.output_json, existing_data, sample)

    print("All evaluation completed!")


def calculate_score(model_name, dataset):
    """
    Calculates and prints the accuracy and average score per question type based on the output JSON file.
    """
    args = parse_args()

    with open(args.output_json, 'r') as file:
        output_contents = json.load(file)

    print(args.output_json)
    
    if dataset == 'outdoor':
        score_data = {
            'location': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0},
            'direction': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0},
            'description': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0},
            'intention reasoning': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0},
            'others': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0}
        }
    else:
        score_data = {
            'hands-on': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0},
            'kitchen': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0},
            'shopping': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0},
            'gameplay': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0},
            'book-related': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0},
            'others': {'score_sum': 0, 'count': 0, 'yes_count': 0, 'no_count': 0}
        }

    total_score_sum = 0
    total_count = 0
    total_yes_count = 0
    total_no_count = 0

    for sample in output_contents[0]['data']:
        question_type = sample['question_type'].lower()
        pred = sample['acc']
        if "yes" in pred.lower():
            score_data[question_type]['yes_count'] += 1
        elif "no" in pred.lower():
            score_data[question_type]['no_count'] += 1

        score = int(sample['score'])
        score_data[question_type]['score_sum'] += score
        score_data[question_type]['count'] += 1

    for q_type, data in score_data.items():
        if (data['yes_count'] + data['no_count']) > 0:
            accuracy = data['yes_count'] / (data['yes_count'] + data['no_count'])
        else:
            accuracy = 0
        average_score = data['score_sum'] / data['count'] if data['count'] > 0 else 0
        print(f"Type: {q_type}")
        print(f"Accuracy: {accuracy}")
        print(f"Average score: {average_score}\n")

        total_score_sum += data['score_sum']
        total_count += data['count']
        total_yes_count += data['yes_count']
        total_no_count += data['no_count']

    overall_accuracy = (total_yes_count / (total_yes_count + total_no_count)
                        if (total_yes_count + total_no_count) > 0 else 0)
    overall_average_score = (total_score_sum / total_count if total_count > 0 else 0)
    print("Overall Results:")
    print("Overall Accuracy:", overall_accuracy)
    print("Overall Average Score:", overall_average_score)


def parse_args():
    """
    Parses the command-line arguments.
    """
    parser = argparse.ArgumentParser(description="question-answer evaluation using gpt-4o-mini")
    parser.add_argument(
        "--pred_path",
        default='mllm_prediction.json',
        help="The path to the file containing predictions."
    )
    parser.add_argument(
        "--output_json",
        default='output.json',
        help="The path to save the annotation JSON file."
    )
    return parser.parse_args()


if __name__ == "__main__":
    model_name = "gemini-1.5-pro" # gpt-4o
    print_score(model_name)
    dataset = 'indoor'  # 'outdoor'
    calculate_score(model_name, dataset)
