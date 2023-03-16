import cv2 as cv
import numpy as np
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

rospy.init_node("computer_vision_sample")
bridge = CvBridge()

DEBUG = rospy.Publisher("~debug", Image)


# Функция получения изображения с камеры
def get_image() -> np.ndarray:
    return bridge.imgmsg_to_cv2(
        rospy.wait_for_message("main_camera/image_raw", Image),
        "bgr8",
    )


# Функция отправки изображения в топик
def send_image(publisher: rospy.Publisher, image: np.ndarray) -> None:
    publisher.publish(bridge.cv2_to_imgmsg(image, "bgr8"))


if __name__ == "__main__":
    pass
