# EgoTextVQA: Towards Egocentric Scene-Text Aware Video Question Answering

![Task](https://img.shields.io/badge/Task-Egocentric--Text--VideoQA-red)
![Dataset](https://img.shields.io/badge/Dataset-EgoTextVQA-blue)
![Model](https://img.shields.io/badge/Model-Gemini--1.5--Pro-green)
![Model](https://img.shields.io/badge/Model-Gemini--1.5--Flash-green)
![Model](https://img.shields.io/badge/Model-GPT--4o-green)


---

## ![EgoTextVQA](https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/logo.png)  

<p align="center">
  [<a href="https://zhousheng97.github.io/EgoTextVQA_page">🌐 Project Page</a>]
  [<a href="https://arxiv.org/abs/2502.07411">📖 Paper</a>]
  [<a href="https://github.com/zhousheng97/EgoTextVQA">📊 Dataset</a>]
  [<a href="https://github.com/zhousheng97/EgoTextVQA">🏆 Evaluation</a>]
</p>


---

## 🔥 Update
- `2025.03.16` We have released our dataset and welcome researchers to use it for evaluation! (If you want to integrate it into a tool or repository for use, please feel free to let me know.)
- `2025.02.27` Our paper has been accepted by **CVPR 2025**! 🎉 Thanks to all co-authors and dataset annotators.
- `2025.02.11` We are very proud to launch ✨**EgoTextVQA**✨, a novel and rigorously constructed benchmark for egocentric QA assistance involving scene text! Our paper has been released on [arXiv](https://arxiv.org/abs/2502.07411).

## 🔍 EgoTextVQA
EgoTextVQA is a novel and rigorously constructed benchmark for egocentric QA assistance involving scene text. EgoTextVQA contains 1.5K ego-view videos and 7K scene-text aware questions that **reflect real-user needs in outdoor driving** and **indoor house-keeping activities**. The questions are designed to elicit identification and reasoning on scene text in an egocentric and dynamic environment. It consists of two parts: 1) **EgoTextVQA-Indoor** focuses on the outdoor scenarios, with 694 videos and 4,848 QA pairs that may arise when driving; 2) **EgoTextVQA-Outdoor** emphasizes indoor scenarios, with 813 videos and 2,216 QA pairs that users may encounter in house-keeping activities. 

❗❗❗  There are several unique features of EgoTextVQA. 
- It stands out as the first VideoQA testbed towards **egocentric scene-text aware QA assistance** in the wild, with 7K QAs that reflect diverse user intentions under 1.5K different egocentric visual situations.
- The QAs emphasize scene text comprehension, but **only about half invoke the exact scene text**. 
- The situations cover both **indoor and outdoor** activities.
- Detailed **timestamps and categories of the questions** are provided to facilitate **real-time QA** and model analysis.
- The real-time QA setting is that the answer to the question is obtained from the video **captured before the question is asked**, rather than the global content. The answer changes with the timestamp of the question.
- **High and low video resolution** settings can be used to evaluate the scene text reading capabilities of MLLMs. In EgoTextVQA, we evaluate the model in both **high-resolution** (1920×1080, 1280×720) and **low-resolution** (960×540, 640×360) video settings.

#### Dataset Comparison
  
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

 ##  ✅ TODO List
 - [x] Release paper on arxiv.
 - [x] Release dataset.
 - [x] Release model QA and evaluation code.


## 📝 Evaluation Pipeline
1. **Download Videos**:
   
   + *Obtain raw_video*. Please download the EgoTextVQA-Outdoor videos from the [Google Drive](https://drive.google.com/drive/folders/1uGE-dObMFpmuhewHi9K_I8pdCbV8efm1?usp=drive_link) and the EgoTextVQA-Indoor videos from the [EgoSchema](https://github.com/egoschema/EgoSchema) GitHub by following their instructions.
   We provide the video IDs for our dataset in ```egotextvqa_outdoor_videoID.json``` (694 videos) and ```egotextvqa_indoor_videoID.json``` (813 videos).

2. **Video Process**:
   + *Obtain fps6_video*. After downloading the raw video, use ```video_process/change_video_fps.py``` to uniformly process the video to fps=6.
   + *Obtian fps6_video_high_res and fps6_video_low_res*. The EgoTextVQA outdoor video is processed into two versions, where the original video is a high-resolution version (1920×1080, 1280×720) and the low-resolution version (960×540, 640×360) is processed using ```video_process/change_video_res.py```. For EgoTextVQA-Indoor, we do not deal with video resolution.
   + *Obtian fps6_frame*. Then use ```video_process/video2frame.py``` to process the fps=6 video into video frames for model evaluation.
   + *Others*. More video process codes in the experiment can be found in ```video_process``` of the repo.

    Data structure as below:
    ```
    root
    ├── data
    │   └──  indoor
    │       ├── fps6_frames
    │       ├── fps6_videos
    │       ├── raw_videos
    │   └──  outdoor
    │       ├── fps6_frame_high_res
    │       ├── fps6_frame_low_res
    │       ├── fps6_video_high_res
    │       ├── fps6_video_low_res
    │       ├── raw_videos
    ```


3. **QA files**:
   
     Please clone our GitHub Repo.
      ```
      git clone https://github.com/zhousheng97/EgoTextVQA.git
      cd data
      ```

5. MLLM QA Prompt: Please see ```mllm_prompt.json```.

6. MLLM Evaluation: Please use ```gpt_eval.py```.


## 📈 Experiment Results
- **Evaluation results of MLLMs on EgoTextVQA-Outdoor with low resolution (960×540, 640×360).**
<p align="center">
<img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/model-evaluation-1.png" alt="Sample Image" width="900">
</p>


- **Evaluation results of MLLMs on EgoTextVQA-Indoor with resolution (640×360, 480×360).**
<p align="center">
<img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/model-evaluation-2.png" alt="Sample Image" width="900">
</p>

- **Evaluation results of MLLMs on the real-time QA subset of EgoTextVQA-Outdoor (∼623 QA pairs).**
<p align="center">
<img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/realtime-evaluation.png" alt="Sample Image" width="500">
</p>

- **Evaluation results of MLLMs on EgoTextVQA-Outdoor with high resolution (1920×1080, 1280×720).**
<p align="center">
<img src="https://github.com/zhousheng97/EgoTextVQA/blob/main/asset/high-res-evaluation.png" alt="Sample Image" width="500">
</p>

## 🎨 Result Visualization

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

## 📧 Contact

If you have any questions or suggestions about the dataset, please contact: hzgn97@gmail.com. We are happy to communicate 😊. 

## ✨ Citation
If this work is helpful to you, consider giving this repository a 🌟 and citing our papers as follows:
```
@article{zhou2025egotextvqa,
      title={EgoTextVQA: Towards Egocentric Scene-Text Aware Video Question Answering}, 
      author={Sheng Zhou and Junbin Xiao and Qingyun Li and Yicong Li and Xun Yang and Dan Guo and Meng Wang and Tat-Seng Chua and Angela Yao},
      journal={arXiv preprint arXiv:2502.07411},
      year={2025}
}
```


## 💌 Acknowledgement
We would like to thank the following repos for their great work:

Our dataset is built upon: [RoadTextVQA](https://github.com/georg3tom/RoadtextVQA), [EgoSchema](https://github.com/egoschema/egoschema), and [Ego4D](https://ego4d-data.org/).

Our evaluation is built upon: [VideoChatGPT](https://github.com/mbzuai-oryx/Video-ChatGPT).
