import rclpy
from glob import glob
from rclpy.node import Node
from rclpy.qos import QoSReliabilityPolicy, QoSHistoryPolicy, QoSDurabilityPolicy, QoSProfile

from sensor_msgs.msg import Image
from example_interfaces.srv import Trigger,AddTwoInts

from cv_bridge import CvBridge

import cv2

class VideoPublisher(Node):

    def __init__(self, videoDevice, QoSProfile):
        super().__init__('VideoPublisher'+str(videoDevice))


        self.service = self.create_service(Trigger, "change_color", self.changeColor)
        self.service2 = self.create_service(AddTwoInts, "change_shape", self.changeShape)

        self.bridge = CvBridge()
        self.camera = cv2.VideoCapture(videoDevice)
        self.isColor = False
        self.imageShape = (640, 480)

        self.publisher = self.create_publisher(Image, 'video'+str(videoDevice), qos_profile=QoSProfile)
  
        callbackFunction = self.framePublish

        self.timer = self.create_timer(1/24, callbackFunction)

        print(f'VideoPublisher {videoDevice} sarted!!!')


    def framePublish(self):
        ret, frame = self.camera.read()

        if self.isColor:
            frame = cv2.resize(frame, self.imageShape)
            msg = self.bridge.cv2_to_imgmsg(frame,'bgr8')
            self.publisher.publish(msg)

        else:
            frame = cv2.resize(frame, self.imageShape)
            grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            msg = self.bridge.cv2_to_imgmsg(grayImg,'mono8')
            self.publisher.publish(msg)

    def changeColor(self, request, response):
        response.success = True
        response.message = "Color changed"
        self.isColor = not self.isColor
        return response
    
    def changeShape(self, request, response):
        self.imageShape = (request.a, request.b)
        return response



    
def setQoSProfile() -> QoSProfile:
    qosProfile = QoSProfile(depth=0)
    qosProfile.durability = QoSDurabilityPolicy.VOLATILE
    qosProfile.reliability = QoSReliabilityPolicy.BEST_EFFORT
    qosProfile.history = QoSHistoryPolicy.KEEP_LAST
    return qosProfile 



def main():
    rclpy.init()
    try:
        print("Available video devices:")
        for dev in glob("/dev/video*"):
            print(dev)
        videoDevice = int(input("Select video device: "))

        node = VideoPublisher(videoDevice, setQoSProfile())
        rclpy.spin(node)

    except:
        pass


if __name__ == '__main__':
    main()