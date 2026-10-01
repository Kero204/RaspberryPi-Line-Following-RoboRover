from gpiozero import DigitalOutputDevice, PWMOutputDevice

from config import (
    LEFT_IN1,
    LEFT_IN2,
    LEFT_EN,
    RIGHT_IN1,
    RIGHT_IN2,
    RIGHT_EN,
    LEFT_MOTOR_REVERSED,
    RIGHT_MOTOR_REVERSED,
)


class RobotMotors:
    def __init__(self):
        self.left_in1 = DigitalOutputDevice(LEFT_IN1)
        self.left_in2 = DigitalOutputDevice(LEFT_IN2)
        self.left_enable = PWMOutputDevice(LEFT_EN)

        self.right_in1 = DigitalOutputDevice(RIGHT_IN1)
        self.right_in2 = DigitalOutputDevice(RIGHT_IN2)
        self.right_enable = PWMOutputDevice(RIGHT_EN)

        self.stop()

    def _set_motor(self, in1, in2, enable, speed, reversed_motor=False):
        speed = max(-1.0, min(1.0, speed))

        if reversed_motor:
            speed = -speed

        if speed > 0:
            in1.on()
            in2.off()
            enable.value = speed

        elif speed < 0:
            in1.off()
            in2.on()
            enable.value = abs(speed)

        else:
            in1.off()
            in2.off()
            enable.value = 0

    def drive(self, left_speed, right_speed):
        self._set_motor(
            self.left_in1,
            self.left_in2,
            self.left_enable,
            left_speed,
            LEFT_MOTOR_REVERSED
        )

        self._set_motor(
            self.right_in1,
            self.right_in2,
            self.right_enable,
            right_speed,
            RIGHT_MOTOR_REVERSED
        )

    def forward(self, speed):
        self.drive(speed, speed)

    def backward(self, speed):
        self.drive(-speed, -speed)

    def stop(self):
        self.drive(0, 0)

    def close(self):
        self.stop()

        self.left_in1.close()
        self.left_in2.close()
        self.left_enable.close()

        self.right_in1.close()
        self.right_in2.close()
        self.right_enable.close()