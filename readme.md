# Video Shot Change Detection

This script uses the Google Cloud Video Intelligence API to perform shot change detection on a video file. Shot change detection refers to identifying points in the video where there are significant visual changes, indicating a transition from one shot to another. This can be helpful for segmenting videos into different scenes or shots, which can be useful for further video analysis or editing.

> **Note**: Before using this script, make sure to replace the `GOOGLE_APPLICATION_CREDENTIALS` environment variable with the path to your own Google Cloud Service Account key file (`loyal-vent-356807-b0c9c97dce30.json`) generated from the Google Cloud Console.

## Prerequisites

- Python 3.x installed
- Google Cloud Video Intelligence API enabled
- Google Cloud Service Account key file (JSON) with appropriate permissions

## Installation

1. Clone this repository to your local machine.
2. Install the required Python dependencies using the following command:

```bash
pip install google-cloud-videointelligence
```

## Usage

To perform shot change detection on a video file, use the following command in your terminal or command prompt:

```bash
python shot_change_detection.py
```

Replace the value of `path` in the script with the path to your desired video file. The script will read the video file, analyze it for shot changes, and display the FPS and total number of frames in the video. It will also print the frame numbers where shot changes are detected and store them in the `shot_frames` list for further analysis.

Please ensure that you have properly set up the Google Cloud Service Account key file and enabled the necessary APIs in your Google Cloud Console before running the script.

## Output

After running the script, you will see the following information:
- Frame numbers where shot changes are detected.

This shot change information can be used for segmenting the video into different shots or scenes, enabling further analysis or editing based on the shot boundaries.