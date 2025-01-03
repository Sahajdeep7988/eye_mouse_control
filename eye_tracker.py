import cv2
import mediapipe as mp

class EyeTracker:
    def __init__(self, blink_threshold=0.1):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1)
        self.blink_threshold = blink_threshold
        self.left_eye_indices = [362, 385, 387, 263, 373, 380]
        self.right_eye_indices = [33, 160, 158, 133, 153, 144]

    def get_eye_position(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = self.face_mesh.process(rgb_frame)
        frame_h, frame_w, _ = frame.shape

        if output.multi_face_landmarks:
            landmarks = output.multi_face_landmarks[0].landmark
            right_eye_x = landmarks[463].x
            right_eye_y = landmarks[463].y
            return right_eye_x, right_eye_y
        return None

    def detect_blinks(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = self.face_mesh.process(rgb_frame)

        if not output.multi_face_landmarks:
            return False, False

        landmarks = output.multi_face_landmarks[0].landmark

        def eye_aspect_ratio(eye_indices):
            a = abs(landmarks[eye_indices[1]].y - landmarks[eye_indices[5]].y)
            b = abs(landmarks[eye_indices[2]].y - landmarks[eye_indices[4]].y)
            c = abs(landmarks[eye_indices[0]].x - landmarks[eye_indices[3]].x)
            return (a + b) / (2.0 * c)

        left_ear = eye_aspect_ratio(self.left_eye_indices)
        right_ear = eye_aspect_ratio(self.right_eye_indices)

        left_blink = left_ear < self.blink_threshold
        right_blink = right_ear < self.blink_threshold

        return left_blink, right_blink
