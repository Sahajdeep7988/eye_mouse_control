import cv2

def display_frame(frame):
    """Utility function to display the frame with proper window handling."""
    cv2.imshow('Eye Controlled Mouse', frame)
