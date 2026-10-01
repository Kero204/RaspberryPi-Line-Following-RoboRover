from time import sleep

from motors import RobotMotors


motors = RobotMotors()

try:
    print("Tester venstre motor frem...")
    motors.drive(0.35, 0)
    sleep(1)
    motors.stop()
    sleep(1)

    print("Tester venstre motor tilbage...")
    motors.drive(-0.35, 0)
    sleep(1)
    motors.stop()
    sleep(1)

    print("Tester højre motor frem...")
    motors.drive(0, 0.35)
    sleep(1)
    motors.stop()
    sleep(1)

    print("Tester højre motor tilbage...")
    motors.drive(0, -0.35)
    sleep(1)
    motors.stop()
    sleep(1)

    print("Motortest færdig.")

finally:
    motors.stop()
    motors.close()