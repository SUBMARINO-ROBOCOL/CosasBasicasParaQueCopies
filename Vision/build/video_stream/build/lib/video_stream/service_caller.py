from example_interfaces.srv import Trigger, AddTwoInts
import rclpy
from rclpy.node import Node

class ServiceCaller(Node):

    def __init__(self):
        super().__init__('service_call')
        self.changeColorClient = self.create_client(Trigger, 'change_color')
        self.changeShapeClient = self.create_client(AddTwoInts, 'change_shape')

        

        self.servicesList = [self.changeColor, self.changeShape]

    def printServices(self):
        print("Available Services:")
        print("0. changeColor")
        print("1. changeShape")

    def changeColor(self):
        request = Trigger.Request()
        self.future = self.changeColorClient.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()
    
    def changeShape(self):
        request = AddTwoInts.Request()
        print("Input the new shape (X,Y): ")
        request.a = int(input("X = "))
        request.b = int(input("Y = "))
        
        self.future = self.changeShapeClient.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()
        


def main():
    rclpy.init()

    service_caller = ServiceCaller()
    service_caller.printServices()
    try:
        response = service_caller.servicesList[int(input("Select desired service: "))]()
        print(response)
        rclpy.shutdown()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()