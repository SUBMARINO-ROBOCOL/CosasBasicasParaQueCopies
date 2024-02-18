from example_interfaces.srv import Trigger
from sensor_msgs.msg import Image

import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge

import cv2

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(Trigger, "idk", self.add_two_ints_callback)


        self.camera = cv2.VideoCapture(0)
        self.bridge = CvBridge()
        self.publisher = self.create_publisher(Image, 'video'+str(0),  qos_profile=1)


        self.timer = self.create_timer(1/24, self.framePublish)

    def framePublish(self):
        ret, frame = self.camera.read()

        msg = self.bridge.cv2_to_imgmsg(frame,'bgr8')
        self.publisher.publish(msg)

    def add_two_ints_callback(self, request, response):
        response.success = True
        response.message = "ok"

        return response



def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()