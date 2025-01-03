

# Eye-Controlled Mouse

This project is a Python-based application that allows users to control the mouse cursor using eye movements. 
It employs OpenCV for image processing, MediaPipe for facial landmark detection, and PyAutoGUI for cursor manipulation.

## Features

- **Real-time Eye Tracking**: Tracks eye movements using the device's webcam.
- **Cursor Movement**: Maps eye directions to cursor movements on the screen.
- **Adjustable Settings**: Customize cursor speed and sensitivity as needed.

## Prerequisites

Ensure you have the following software and libraries installed before running the project:

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

Install the required dependencies using the following command:

```bash
pip install opencv-python mediapipe pyautogui
```

or use pip install -r requirements.txt

## How It Works

1. **Camera Feed**: Captures real-time video using the webcam.
2. **Eye Detection**: Utilizes MediaPipe to detect facial landmarks and track the eyes.
3. **Cursor Control**: Translates eye movement to mouse cursor movement using PyAutoGUI.

## Usage

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the main Python script:

```bash
python eye_control.py
```

4. Make sure your webcam is enabled, as it is required for eye tracking.

## Project Structure

- **`eye_control.py`**: The primary script for eye tracking and cursor control.
- **`README.md`**: This file, providing project details and instructions.

## Future Enhancements

- Add blink-based mouse clicks for hands-free interaction.
- Enhance accuracy of eye movement detection in varying lighting conditions.
- Implement support for multiple screen resolutions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- [OpenCV](https://opencv.org/) for image processing.
- [MediaPipe](https://mediapipe.dev/) for face and eye detection.
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) for mouse control.

---

Feel free to contribute by submitting issues or pull requests. We welcome any feedback or suggestions for improvement!
