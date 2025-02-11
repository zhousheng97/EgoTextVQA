# EgoTextVQA: Towards Egocentric Scene-Text Aware Video Question Answering

![Task](https://img.shields.io/badge/Task-Egocentric--Text--VideoQA-red)
![Dataset](https://img.shields.io/badge/Dataset-EgoTextVQA-blue)
![Model](https://img.shields.io/badge/Model-Gemini--1.5--Pro-green)
![Model](https://img.shields.io/badge/Model-Gemini--1.5--Flash-green)
![Model](https://img.shields.io/badge/Model-GPT--4o-green)


---

## ![EgoTextVQA](https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/logo.png)  

<p align="center">
  [<a href="https://project-page-link.com">🌐 Project Page</a>]
  [<a href="https://arxiv.org/abs/xxxx">📖 Paper</a>]
  [<a href="https://dataset-link.com">📊 Dataset</a>]
  [<a href="https://leaderboard-link.com">🏆 Leaderboard</a>]
</p>


---

## 🔥 Update
- `2025.02.12` We are very proud to launch ✨**EgoTextVQA**✨, a novel and rigorously constructed benchmark for egocentric QA assistance involving scene text! Our paper has been released on arXiv.

## 🔍 EgoTextVQA
EgoTextVQA is a novel and rigorously constructed benchmark for egocentric QA assistance involving scene text. EgoTextVQA contains 1.5K ego-view videos and 7K scene-text aware questions that **reflect real-user needs in outdoor driving** and **indoor house-keeping activities**. The questions are designed to elicit identification and reasoning on scene text in an egocentric and dynamic environment. It consists of two parts: 1) **EgoTextVQA-Indoor** focuses on the outdoor scenarios, with 694 videos and 4,848 QA pairs that may arise when driving; 2) **EgoTextVQA-Outdoor** emphasizes indoor scenarios, with 813 videos and 2,216 QA pairs that users may encounter in house-keeping activities. There are several unique features of EgoTextVQA. 

- It stands out as **the first VideoQA testbed towards egocentric scene-text aware QA assistance** in the wild, with 7K QAs that reflect diverse user intentions under 1.5K different egocentric visual situations.
- The QAs emphasize scene text comprehension, but **only about half invoke the exact scene text**. 
- The situations cover both **indoor and outdoor** activities.
- Detailed **timestamps and categories of the questions** are provided to facilitate **real-time QA** and model analysis.



#### Dataset Comparision
  
  <p align="center">
  <img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/dataset-comparision.png" alt="Sample Image" width="900">
  </p>


<details>
  <summary>QA examples of different question categories.</summary>
  
  <p align="center">
  <img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/qa-example.png" alt="Sample Image" width="500">
  </p>

</details>


<details>
  <summary>Dataset analysis.</summary>
  
  <p align="center">
  <img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/dataset-analysis.png" alt="Sample Image" width="1000">
  </p>

</details>




## 🎨 Dataset Examples
<details>
  <summary>Examples on EgoTextVQA-Outdoor.</summary>
  
  <p align="center">
  <img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/result-outdoor.png" alt="Sample Image" width="900">
  </p>

</details>


<details>
  <summary>Examples on EgoTextVQA-Indoor.</summary>
  
  <p align="center">
  <img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/result-indoor.png" alt="Sample Image" width="900">
  </p>

</details>


## 📝 Evaluation Pipeline
📍Video Process:

📍MLLM QA Prompt:

📍Evaluation Prompt:


## 📈 Experiment Results
- **Evaluation results of MLLMs on EgoTextVQA-Outdoor.**
<p align="center">
<img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/model-evaluation-1.png" alt="Sample Image" width="900">
</p>


- **Evaluation results of MLLMs on EgoTextVQA-Indoor.**
<p align="center">
<img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/model-evaluation-2.png" alt="Sample Image" width="900">
</p>



## ✨ Citation


## 💌 Acknowledgement
We would like to thank the following repos for their great work:

Our dataset is built upon: [RoadTextVQA](https://github.com/georg3tom/RoadtextVQA)  and [EgoSchema](https://github.com/egoschema/egoschema).

Our evaluation is built upon: [VideoChatGPT](https://github.com/mbzuai-oryx/Video-ChatGPT).
