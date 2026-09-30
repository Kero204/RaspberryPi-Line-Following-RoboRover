from time import sleep

from sensors import LineSensors


sensors = LineSensors()

try:
    while True:
        left, right = sensors.raw()

        print(
            f"Venstre: {left} | "
            f"Højre: {right}"
        )

        sleep(0.2)

except KeyboardInterrupt:
    print("\nSensortest stoppet.")

finally:
    sensors.close()