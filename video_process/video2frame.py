import cv2
import os

def extract_frames(video_path, output_folder, min_frames=1080):
    """
    Extract frames from a video and save them as images.
    
    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Directory to save extracted frames.
        min_frames (int): Minimum number of frames to check before processing (default: 1080).
    """
    if not os.path.exists(video_path):
        print(f"Warning: Video file {video_path} does not exist.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    
    if len(os.listdir(output_folder)) >= min_frames:
        print(f"{os.path.basename(video_path)} already processed.")
        return
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}.")
        return
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Processing {os.path.basename(video_path)} | Original FPS: {fps}")
    
    frame_count = 1
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:05d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    
    cap.release()
    print(f"Frames extracted and saved in: {output_folder}")

def process_videos(input_folder, output_folder, min_frames=1080):
    """
    Process all videos in a folder and extract frames.
    
    Args:
        input_folder (str): Folder containing input videos.
        output_folder (str): Folder to store extracted frames.
        min_frames (int): Minimum frame count to skip already processed videos.
    """
    if not os.path.exists(input_folder):
        print(f"Error: Input folder {input_folder} does not exist.")
        return
    
    video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    if not video_files:
        print("No video files found in the input folder.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    
    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)
        video_frame_folder = os.path.join(output_folder, os.path.splitext(video_file)[0])
        extract_frames(video_path, video_frame_folder, min_frames)

if __name__ == "__main__":
    INPUT_FOLDER = '/mnt/data/sheng/EgoSTVidQA_Data/egostvidqa/roadtextvqa/fps6_video_low_res'
    OUTPUT_FOLDER = '/mnt/data/sheng/EgoSTVidQA_Data/egostvidqa/roadtextvqa/fps6_frame_low_res'
    
    process_videos(INPUT_FOLDER, OUTPUT_FOLDER)
