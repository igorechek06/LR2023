import rospy
from ser import drop_all
from visualization_msgs.msg import MarkerArray

rospy.init_node("flight")

from nav import land, navigate

rviz_wall = rospy.Publisher(
    "~wall_rviz",
    MarkerArray,
    queue_size=1,
)
rviz_fire_and_injured = rospy.Publisher(
    "~fire_and_injured_rviz",
    MarkerArray,
    queue_size=1,
)

# Взлёт на 1 метр
navigate(x=0, y=0, z=1, frame_id="body", auto_arm=True)

# Получить 2.4 балла за сброс всего
drop_all()

# Посадка
land()
