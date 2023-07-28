from google.cloud import videointelligence_v1 as videointelligence
import os
import io
import cv2
import logging

# Replace with your file, downloaded from Google Cloud Video Intelligence API
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'loyal-vent-356807-b0c9c97dce30.json'


def analyze_shots(path, video):
    fps = float(video.get(cv2.CAP_PROP_FPS))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print("FPS: ",fps)
    print("Total Frames: ", total_frames)

    # Read the video file as binary and convert to bytes
    with io.open(path, "rb") as f:
        input_content = f.read()

    # Use the VideoIntelligenceServiceClient from videointelligence_v1
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.SHOT_CHANGE_DETECTION]

    # Use annotate_video method from videointelligence_v1, not VideoIntelligenceServiceClient
    operation = video_client.annotate_video(
        request={"features": features, "input_content": input_content}
    )

    print("\nProcessing video for shot change annotations:")

    # result method is not available in videointelligence_v1
    result = operation.result(timeout=90)

    print("\nFinished processing.")

    shot_frames = []  # Store the frame numbers where shot changes occur

    # Iterate through the shot annotations and store the frame numbers
    for i, shot in enumerate(result.annotation_results[0].shot_annotations):
        start_time = (
                shot.start_time_offset.seconds + shot.start_time_offset.microseconds / 1e6
        )
        start_frame = int(start_time * fps)
        shot_frames.append(start_frame)

    print("Saved Frames after Shot Change Detection: ", shot_frames)
    return shot_frames



if __name__ == "__main__":
    path = "sample_video.mp4"
    video = cv2.VideoCapture(path)
    try:
        shot_frames = analyze_shots(path, video)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        video.release()
