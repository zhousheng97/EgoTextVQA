import cv2
import os

def process_video(input_path, output_path, target_fps=6):
    """
    Reduce the frame rate of a video and save the processed video.
    
    Args:
        input_path (str): Path to the input video file.
        output_path (str): Path to save the processed video.
        target_fps (int): Desired frames per second (default: 6).
    """
    if not os.path.exists(input_path):
        print(f"Warning: Input video {input_path} does not exist.")
        return
    
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Failed to open video {input_path}.")
        return
    
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, target_fps, (width, height))
    
    frame_interval = max(1, int(original_fps / target_fps))
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % frame_interval == 0:
            out.write(frame)
        
        frame_count += 1
    
    cap.release()
    out.release()
    print(f"Processed video saved to: {output_path}")

def process_video_folder(input_folder, output_folder, target_fps=6):
    """
    Process all videos in a folder and save them with reduced frame rates.
    
    Args:
        input_folder (str): Path to the folder containing raw videos.
        output_folder (str): Path to save processed videos.
        target_fps (int): Desired frames per second (default: 6).
    """
    if not os.path.exists(input_folder):
        print(f"Error: Input folder {input_folder} does not exist.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    
    video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    if not video_files:
        print("No video files found in the input folder.")
        return
    
    for video_file in video_files:
        input_path = os.path.join(input_folder, video_file)
        output_path = os.path.join(output_folder, video_file)
        process_video(input_path, output_path, target_fps)

if __name__ == "__main__":
    RAW_FOLDER = '/mnt/data/sheng/EgoSTVidQA_Data/egostvidqa/ego4d/raw_video'
    SAVE_FOLDER = '/mnt/data/sheng/EgoSTVidQA_Data/egostvidqa/ego4d/fps6_video'
    TARGET_FPS = 6
    
    process_video_folder(RAW_FOLDER, SAVE_FOLDER, TARGET_FPS)
