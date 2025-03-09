import cv2
import os

# Define input and output folder paths
input_folder = '/mnt/data/sheng/EgoSTVidQA_Data/egostvidqa/ego4d/fps6_video'  # Folder containing video files
output_folder = '/mnt/data/sheng/EgoSTVidQA_Data/egostvidqa/ego4d/fps1_frames'  # Folder to save extracted frames

# Set video frame rate (FPS) and sampling interval
fps = 6  # Assuming the video FPS is 6
sampling_interval = fps  # Extract one frame per second

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all video files in the input folder
for video_file in os.listdir(input_folder):
    if video_file.endswith(('.mp4', '.avi')):  # Process only .mp4 and .avi files
        video_path = os.path.join(input_folder, video_file)

        # Open the video file
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Error: Cannot open video file {video_file}")
            continue

        frame_count = 0  # Track total frames processed
        sampled_frame_count = 0  # Track extracted frames

        # Create a subfolder for the current video's frames
        video_output_folder = os.path.join(output_folder, os.path.splitext(video_file)[0])
        os.makedirs(video_output_folder, exist_ok=True)

        # Read and process video frames
        while True:
            ret, frame = cap.read()
            if not ret:  # Stop if video ends
                break

            # Extract one frame per second
            if frame_count % sampling_interval == 0:
                frame_filename = os.path.join(video_output_folder, f"frame_{sampled_frame_count:05d}.jpg")
                cv2.imwrite(frame_filename, frame)
                sampled_frame_count += 1

            frame_count += 1

        # Release the video file
        cap.release()
        print(f"Processed video: {video_file}")

print("All videos processed successfully!")
