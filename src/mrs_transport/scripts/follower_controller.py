#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import WrenchStamped, Twist
from rclpy.qos import qos_profile_sensor_data

class MultiFollowerBrain(Node):
    def __init__(self):
        super().__init__('multi_follower_brain')
        # DISABLE sim_time for a moment to see if it helps connection
        self.get_logger().info("Swarm Brain Online! Listening for sensor data...")
        
        self.sub_f1 = self.create_subscription(WrenchStamped, '/tb3_f1/force_sensor', self.f1_cb, qos_profile_sensor_data)
        self.sub_f2 = self.create_subscription(WrenchStamped, '/tb3_f2/force_sensor', self.f2_cb, qos_profile_sensor_data)
        self.pub_f1 = self.create_publisher(Twist, '/tb3_f1/cmd_vel', 10)
        self.pub_f2 = self.create_publisher(Twist, '/tb3_f2/cmd_vel', 10)

    def f1_cb(self, msg):
        # This will print EVERY message so we know it's working
        force = msg.wrench.force.x
        self.get_logger().info(f"F1 Heartbeat: {force:.2f} N", throttle_duration_sec=1.0)
        if abs(force) > 0.5:
            t = Twist()
            t.linear.x = 0.1 * force
            self.pub_f1.publish(t)

    def f2_cb(self, msg):
        force = msg.wrench.force.x
        self.get_logger().info(f"F2 Heartbeat: {force:.2f} N", throttle_duration_sec=1.0)
        if abs(force) > 0.5:
            t = Twist()
            t.linear.x = 0.1 * force
            self.pub_f2.publish(t)

def main():
    rclpy.init()
    rclpy.spin(MultiFollowerBrain())
    rclpy.shutdown()

if __name__ == '__main__':
    main()