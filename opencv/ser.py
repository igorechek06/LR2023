import rospy
from serial import Serial

serial = Serial("/dev/ttyUSB0", 9600)


# Функция записи в сериал
def writeln(data: object) -> None:
    serial.write(f"{data}\n".encode("UTF-8"))


# Функция для вращения сервомотора в лево
def rotate_left() -> None:
    writeln(1)


# Функция остановки сервомотора
def rotate_stop() -> None:
    writeln(0)


# Функция сброса всего чего возможно
def drop_all() -> None:
    prepare()
    rotate_left()
    rospy.sleep(3)
    rotate_stop()


# Функция для подготовки к сбросу
def prepare() -> None:
    rotate_left()
    rospy.sleep(0.5)
    rotate_stop()
