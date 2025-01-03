import cv2
import mediapipe as mp
from mouse_control import MouseControl
from eye_tracker import EyeTracker
import pyautogui

# Initialize Mediapipe, MouseControl, and EyeTracker
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
mouse_control = MouseControl()  # Default speed multiplier
eye_tracker = EyeTracker(blink_threshold=0.1)  # Set blink threshold
screen_width, screen_height = 1920, 1080  # Your screen resolution

# Ensure the cursor starts at the center of the screen
mouse_control.move_cursor(screen_width // 2, screen_height // 2)

# Open webcam
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    frame_height, frame_width, _ = frame.shape

    if output.multi_face_landmarks:
        landmarks = output.multi_face_landmarks[0].landmark

        # Right eye tracking (landmark indices 474 and 475)
        right_eye_x = (landmarks[474].x + landmarks[475].x) / 2
        right_eye_y = (landmarks[474].y + landmarks[475].y) / 2

        # Map eye position to screen coordinates
        screen_x = right_eye_x * screen_width
        screen_y = right_eye_y * screen_height

        # Use MouseControl for smooth cursor movement
        mouse_control.move_cursor(screen_x, screen_y)

        # Detect blinks and perform corresponding actions
        left_blink, right_blink = eye_tracker.detect_blinks(frame)
        if left_blink:
            pyautogui.click(button="right")  # Right click for left eye blink
        if right_blink:
            pyautogui.click(button="left")  # Left click for right eye blink

    # Display webcam feed
    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on pressing 'Esc'
        break

cam.release()
cv2.destroyAllWindows()
