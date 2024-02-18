from example_interfaces.srv import Trigger
import rclpy
from rclpy.node import Node

class ServiceCall(Node):

    def __init__(self):
        super().__init__('service_call')
        self.client = self.create_client(Trigger, 'change_color')

        self.req = Trigger.Request()

    def changeColor(self):
        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()

    minimal_client = ServiceCall()

 

    methods = [attr for attr in dir(ServiceCall) if callable(getattr(ServiceCall, attr))]
    print(methods) 

    response = minimal_client.changeColor()
    print(response.message) 

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()