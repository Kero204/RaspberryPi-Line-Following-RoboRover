from time import sleep

from motors import RobotMotors
from sensors import LineSensors
from config import BASE_SPEED, TURN_SPEED


motors = RobotMotors()
sensors = LineSensors()

try:
    while True:
        left_black = sensors.left_on_black()
        right_black = sensors.right_on_black()

        # Begge sensorer ser hvidt
        # Linien ligger mellem sensorerne
        if not left_black and not right_black:
            motors.forward(BASE_SPEED)

        # Venstre sensor rammer sort
        # Korriger mod venstre
        elif left_black and not right_black:
            motors.drive(
                0,
                TURN_SPEED
            )

        # Højre sensor rammer sort
        # Korriger mod højre
        elif not left_black and right_black:
            motors.drive(
                TURN_SPEED,
                0
            )

        # Begge sensorer ser sort
        # Fortsæt frem i stedet for at stoppe
        else:
            motors.forward(BASE_SPEED)

        sleep(0.01)

except KeyboardInterrupt:
    pass

finally:
    motors.stop()
    motors.close()
    sensors.close()