import rospy

rospy.init_node("flight")

from nav import get_telemetry, land, navigate

# Взлёт
navigate(x=0, y=0, z=1, frame_id="body", auto_arm=True)
navigate(x=0, y=0, z=0, frame_id="body")

# # Идем на 0 0
# start_pos = get_telemetry("aruco_map")
# navigate(x=start_pos.x, y=0, z=1, frame_id="aruco_map")
# navigate(x=0, y=0, z=1, frame_id="aruco_map")

# # Летим вдоль стены
# scan_mission = (
#     129,
#     143,
#     139,
#     160,
#     115,
#     156,
#     115,
#     123,
#     128,
#     123,
#     110,
#     138,
#     129,
# )
# for aruco in scan_mission:
#     navigate(x=0, y=0, z=1, frame_id=f"aruco_{aruco}")

# Посадка
# navigate(x=0, y=0, z=1, frame_id="aruco_map")
land()
