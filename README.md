
# Eye-Controlled Mouse Project

This project enables users to control their computer's mouse cursor using eye movements. The system leverages Python, OpenCV, MediaPipe, and PyAutoGUI for real-time eye tracking and smooth cursor manipulation.

## Features

- **Real-time Eye Tracking**: Tracks eye movements via webcam using MediaPipe.
- **Cursor Movement**: Maps eye positions to screen coordinates for controlling the cursor.
- **Blink Detection**: Detects blinks and maps them to mouse clicks:
  - **Left Blink**: Performs a right-click.
  - **Right Blink**: Performs a left-click.
- **Customizable Settings**: Adjust cursor speed and blink thresholds for better control.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

Install the required Python libraries using the following command:

```bash
pip install opencv-python mediapipe pyautogui
```


## How It Works

1. **Eye Tracking**:
   - MediaPipe's Face Mesh is used to identify and track facial landmarks, particularly around the eyes.
2. **Cursor Movement**:
   - Eye positions are mapped to screen coordinates using the resolution of the user's screen.
3. **Blink Detection**:
   - Eye Aspect Ratio (EAR) is calculated to detect blinks. Detected blinks are mapped to specific mouse actions.

## Usage

1. Clone or download this repository to your local machine.
2. Connect a webcam to your system.
3. Run the main Python script:

```bash
python main.py
```

4. Ensure the webcam feed is visible and functional. Move your eyes to control the cursor and blink to perform mouse clicks.

## Project Files

- **`eye_tracker.py`**: Handles eye tracking and blink detection using MediaPipe.
- **`utils.py`**: contains the code to open camera
- **`mouse_control.py`**: Controls mouse movements and clicks using PyAutoGUI.
- **`main.py`**: The main script that integrates all components and runs the application.
- **`README.md`**: Documentation for the project.

## Future Enhancements

- Improve eye tracking accuracy in low-light environments.
- Add support for multi-monitor setups.
- Enhance customization options for blink detection and cursor mapping.
- Add a GUI for user-friendly configuration.

## Acknowledgments

- **OpenCV**: For image processing.
- **MediaPipe**: For facial landmark detection and tracking.
- **PyAutoGUI**: For controlling the mouse programmatically.

## License

This project is licensed under the MIT License - see the `LICENSE` file for more details.

---

Feel free to contribute or suggest improvements by opening issues or pull requests!
