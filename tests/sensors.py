import math

import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node("flight")

get_telemetry = rospy.ServiceProxy("get_telemetry", srv.GetTelemetry)

while True:
    telemetry = get_telemetry(frame_id="aruco_map")
    print(telemetry.x, telemetry.y, telemetry.z, telemetry.yaw)
    rospy.sleep(0.5)
