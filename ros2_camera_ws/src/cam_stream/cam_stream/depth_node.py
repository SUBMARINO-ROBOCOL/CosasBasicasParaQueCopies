import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge

import cv2
from realsense_depth import *

class DriverNode(Node):

    def __init__(self):
        super().__init__('depth_node')

        self.bridge = CvBridge()
        self.camera = DepthCamera()
        self.num_frame=0

        self.color_publisher = self.create_publisher(Image, 'Color_image', 10)
        self.depth_publisher = self.create_publisher(Image, 'Depth_image', 10)

        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        check, depth_frame, color_frame = self.camera.get_frame()
        if check:
            color_msg = self.bridge.cv2_to_imgmsg(color_frame, 'bgr8')
            color_msg.header.frame_id = str(self.num_frame) 

            depth_msg = self.bridge.cv2_to_imgmsg(depth_frame, 'bgr8')
            depth_msg.header.frame_id = str(self.num_frame) 

            self.num_frame +=1
            self.color_publisher.publish(color_msg)
            self.depth_publisher.publish(depth_msg)


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