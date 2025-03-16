import cv2
import os


def resize_video(input_video_path, output_video_path, scale_factor=0.5):
    """
    Resizes a video by a given scale factor and saves it to the specified output path.

    Parameters:
    - input_video_path (str): Path to the input video.
    - output_video_path (str): Path to save the resized video.
    - scale_factor (float): Scaling factor for resizing (default is 0.5).

    Returns:
    - None
    """
    # Open the input video
    cap = cv2.VideoCapture(input_video_path)

    # Get original video properties
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Compute new dimensions
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    # Define video codec and output file
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (new_width, new_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        resized_frame = cv2.resize(frame, (new_width, new_height))

        # Write the resized frame to the output video
        out.write(resized_frame)

    # Release resources
    cap.release()
    out.release()
    print(f"Video processing completed: {output_video_path}")


# Define input and output video directories
input_folder = '../egotextvqa/outdoor/fps6_video_high_res'
output_folder = '../egotextvqa/outdoor/fps6_video_low_res'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get the list of videos in the input folder
video_files = os.listdir(input_folder)

# Process each video in the input folder
for video_filename in video_files:
    input_video_path = os.path.join(input_folder, video_filename)
    output_video_path = os.path.join(output_folder, video_filename)

    resize_video(input_video_path, output_video_path)
