import rospy

rospy.init_node("flight")

from nav import land, navigate

# Взлёт на 1 метр
navigate(x=0, y=0, z=1, frame_id="body", auto_arm=True)

# Посадка
land()
