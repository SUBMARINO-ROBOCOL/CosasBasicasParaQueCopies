import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class NombreNodo(Node):
    
    def __init__(self):
        super().__init__('NombreNodo')
        self.publisher_ = self.create_publisher(Twist, 'turtlebot_cmdVel', 1)
        #self.publisher_ = self.create_subscription(Twist, 'turtlebot_cmdVel', 1)
        #Los argumentos del metodo indican el tipo de mensaque que se manda

    def corregir():
        pass

def main(args = None):
    rclpy.init(args=args)
    nodo = NombreNodo()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()
    


if __name__ == '__main__':
    main()
