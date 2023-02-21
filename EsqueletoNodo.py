import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class NombreNodo(Node):
    
    def __init__(self):
        super().__init__('NombreNodo')
        self.publisher_ = self.create_publisher(tipoMensaje, 'nombre topico', 10) #para indicar que va a publicar dicho topico
        self.publisher_ = self.create_subscription(tipoMensaje, 'nombre topico', 10) #para hacerlo subscribirse a dicho topico
        

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
