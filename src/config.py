# L298N - venstre motor (Motor A)
LEFT_IN1 = 17
LEFT_IN2 = 27
LEFT_EN = 18

# L298N - højre motor (Motor B)
RIGHT_IN1 = 22
RIGHT_IN2 = 23
RIGHT_EN = 12

# MH-B IR-sensorer
LEFT_SENSOR = 5
RIGHT_SENSOR = 6

# MH-B forventes normalt at give LOW over sort.
# Dette BEKRÆFTER vi med test_sensors.py.
BLACK_VALUE = 0

# Motorretning
# Skift False -> True hvis en motor kører baglæns
LEFT_MOTOR_REVERSED = False
RIGHT_MOTOR_REVERSED = False

# Hastigheder: 0.0 - 1.0
BASE_SPEED = 0.55
TURN_SPEED = 0.55