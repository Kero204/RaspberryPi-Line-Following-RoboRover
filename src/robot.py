from time import sleep

from motors import RobotMotors
from sensors import LineSensors
from config import BASE_SPEED, TURN_SPEED


motors = RobotMotors()
sensors = LineSensors()


try:
    print("Line follower starter.")
    print("Tryk Ctrl+C for at stoppe.")

    while True:
        left_black = sensors.left_on_black()
        right_black = sensors.right_on_black()

        # Begge sensorer er på hvidt
        if not left_black and not right_black:
            motors.forward(BASE_SPEED)

        # Venstre sensor rammer den sorte linje
        elif left_black and not right_black:
            motors.drive(0, TURN_SPEED)

        # Højre sensor rammer den sorte linje
        elif not left_black and right_black:
            motors.drive(TURN_SPEED, 0)

        # Begge sensorer rammer sort
        else:
            motors.stop()

        sleep(0.01)

except KeyboardInterrupt:
    print("\nRobot stoppet.")

finally:
    motors.stop()
    motors.close()
    sensors.close()