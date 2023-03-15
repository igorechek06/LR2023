import math
from dataclasses import dataclass
from typing import Any, Callable, Optional

import rospy
from clover import srv
from std_srvs.srv import Trigger

__get_telemetry = rospy.ServiceProxy("get_telemetry", srv.GetTelemetry)
__navigate = rospy.ServiceProxy("navigate", srv.Navigate)
__land = rospy.ServiceProxy("land", Trigger)

HANDLER = Optional[Callable[[Any], bool]]


def get_telemetry(frame_id: str = "map"):
    return __get_telemetry(frame_id=frame_id)


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
):
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


def land(handler: HANDLER = None):
    __land()
    while True:
        telemetry = __get_telemetry(frame_id="navigate_target")
        result = False if handler is None else handler(telemetry)
        if telemetry.armed or result:
            break
