import pyautogui

class MouseControl:
    def __init__(self, speed_multiplier=1):
        self.screen_w, self.screen_h = pyautogui.size()
        self.speed_multiplier = speed_multiplier

    def move_cursor(self, screen_x, screen_y):
        screen_x = screen_x * self.speed_multiplier
        screen_y = screen_y * self.speed_multiplier

        # Clamp cursor position to avoid triggering fail-safe
        screen_x = min(max(10, screen_x), self.screen_w - 10)  # Keep cursor 10 pixels away from edges
        screen_y = min(max(10, screen_y), self.screen_h - 10)  # Keep cursor 10 pixels away from edges

        pyautogui.moveTo(screen_x, screen_y)
