from gpiozero import DigitalInputDevice

from config import LEFT_SENSOR, RIGHT_SENSOR, BLACK_VALUE


class LineSensors:
    def __init__(self):
        self.left = DigitalInputDevice(
            LEFT_SENSOR,
            pull_up=None
        )

        self.right = DigitalInputDevice(
            RIGHT_SENSOR,
            pull_up=None
        )

    def raw(self):
        return self.left.value, self.right.value

    def left_on_black(self):
        return self.left.value == BLACK_VALUE

    def right_on_black(self):
        return self.right.value == BLACK_VALUE

    def close(self):
        self.left.close()
        self.right.close()