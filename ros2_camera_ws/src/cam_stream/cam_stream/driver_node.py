import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge

import cv2

class DriverNode(Node):

    def __init__(self, camIndex):
        super().__init__('driver_node_'+str(camIndex))

        self.bridge = CvBridge()
        self.camera = cv2.VideoCapture(camIndex)

        self.publisher = self.create_publisher(Image, 'camera_'+str(camIndex), 10)

        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        check, frame = self.camera.read()
        if check:
            msg = self.bridge.cv2_to_imgmsg(frame,'mono8')
            self.publisher.publish(msg)


def returnCameraIndexes():
        index = 0
        arr = []
        while index < 6:
            cap = cv2.VideoCapture(index)
            if cap.read()[0]:
                arr.append(index)
                cap.release()
            index += 1
        if (len(arr)>0):
            print("\nThe following camera indexes were detected: ")
            msg = ""
            for i in arr:
                msg += str(i)+", "
            print(msg[:-2])

            return True
        else:
             print("\nNo cameras available")

             return False
    
def setCamIndx():
    return int(input("Select a camIndex: "))

def main():
    rclpy.init()
    if(returnCameraIndexes()):
        node = DriverNode(setCamIndx())
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()


#https://blog.misterblue.com/2021/2021-05-29-ros2-sending-image
#ros2 run rqt_image_view rqt_image_view
#https://docs.ros.org/en/foxy/Concepts/About-RQt.html
#sudo apt install ros-foxy-rqt*