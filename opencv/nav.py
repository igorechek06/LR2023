import math
from dataclasses import dataclass
from typing import Callable, Optional

import rospy
from clover import srv
from std_srvs.srv import Trigger

__get_telemetry = rospy.ServiceProxy("get_telemetry", srv.GetTelemetry)
__navigate = rospy.ServiceProxy("navigate", srv.Navigate)
__land = rospy.ServiceProxy("land", Trigger)


@dataclass
class Telemetry:
    x: float
    y: float
    z: float
    yaw: float


HANDLER = Optional[Callable[[Telemetry], bool]]


# Получить данные с датчиков
def get_telemetry(frame_id: str = "map") -> Telemetry:
    return __get_telemetry(frame_id=frame_id)


# Функция перемещения в заданную точку
def navigate(
    x: float,
    y: float,
    z: float,
    yaw: float = float("nan"),
    yaw_rate: float = 0,
    speed: float = 0.5,
    auto_arm: bool = False,
    frame_id: str = "map",
    handler: HANDLER = None,
) -> None:
    res = __navigate(
        x=x,
        y=y,
        z=z,
        yaw=yaw,
        yaw_rate=yaw_rate,
        speed=speed,
        frame_id=frame_id,
        auto_arm=auto_arm,
    )

    if not res.success:
        raise Exception(res.message)

    while not rospy.is_shutdown():
        telemetry = __get_telemetry(frame_id="navigate_target")
        result = False if handler is None else handler(telemetry)
        if (
            math.sqrt(telemetry.x**2 + telemetry.y**2 + telemetry.z**2) < 0.2
            or result
        ):
            return


# Функция посадки
def land(handler: HANDLER = None) -> None:
    __land()
    while True:
        telemetry = __get_telemetry(frame_id="navigate_target")
        result = False if handler is None else handler(telemetry)
        if telemetry.armed or result:
            break
