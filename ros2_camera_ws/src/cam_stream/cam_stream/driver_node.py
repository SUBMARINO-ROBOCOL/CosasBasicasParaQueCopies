import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge

import cv2

class DriverNode(Node):

    def __init__(self):
        super().__init__('driver_node')

        self.bridge = CvBridge()
        self.camera = cv2.VideoCapture(0)
        self.num_frame=0

        self.publisher = self.create_publisher(Image, 'camera', 10)

        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        check, frame = self.camera.read()
        if check:
            msg = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
            msg.header.frame_id = str(self.num_frame) 
            self.num_frame +=1
            self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DriverNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


#https://blog.misterblue.com/2021/2021-05-29-ros2-sending-image
#ros2 run rqt_image_view rqt_image_view
#https://docs.ros.org/en/foxy/Concepts/About-RQt.html
#sudo apt install ros-foxy-rqt*