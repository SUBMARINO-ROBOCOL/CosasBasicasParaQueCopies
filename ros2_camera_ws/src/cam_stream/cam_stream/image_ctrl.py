import rclpy
from rclpy.node import Node
from rclpy.qos import QoSReliabilityPolicy, QoSHistoryPolicy, QoSDurabilityPolicy, QoSProfile

from sensor_msgs.msg import Image

from cv_bridge import CvBridge

import cv2

import show_img


class ImageCtrlNode(Node):
    
    def __init__(self, camIndx, QoSProf):
        super().__init__("imageCtrl_"+str(camIndx))
        
        self.camIndx = camIndx
        self.bridge = CvBridge()

        self.sub = self.create_subscription(Image, "camera_"+str(self.camIndx), self.cvProcessing,qos_profile=QoSProf) 
    
    def cvProcessing(self,msg):
        img = self.bridge.imgmsg_to_cv2(msg)
        show_img.showImg(img)




def getCamSubscription():
    return int(input("Choose a camera to subscribe: "))

def setQoSProfile() -> QoSProfile:
    
    qosProfileVar = QoSProfile(depth=2)
    qosProfileVar.durability = QoSDurabilityPolicy.VOLATILE
    qosProfileVar.reliability = QoSReliabilityPolicy.BEST_EFFORT
    qosProfileVar.history = QoSHistoryPolicy.KEEP_LAST

    return qosProfileVar
    
    

def main():
    rclpy.init()


    camIndx = getCamSubscription()
    node = ImageCtrlNode(camIndx, setQoSProfile())
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    show_img.hola()
    main()