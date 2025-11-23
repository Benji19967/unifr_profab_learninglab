#!/usr/bin/env python3

import math
from typing import Optional
import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Twist
from move_base_msgs.msg import MoveBaseActionResult

NODE_NAME = "controller"
MOTOR_TOPIC_NAME = "motor_speed"
LIGHT_TOPIC_NAME = "light_intensity"

MAIN_LOGIC_CALLBACK_INTERVAL = 0.1

# TODO: Create a map
# TODO: Define goals on map
# TODO: Send goal commands
# TODO: Send motor and light control commands
# TODO: Make sure we can also command light and motor via Node-RED


class Controller:
    def __init__(self):
        rospy.init_node(NODE_NAME, anonymous=True)
        rospy.loginfo("Starting controller")

        self.motor_pub = rospy.Publisher(LIGHT_TOPIC_NAME, Int16)
        self.light_pub = rospy.Publisher(MOTOR_TOPIC_NAME, Int16)

        # Do some cleanup on shutdown
        rospy.on_shutdown(self.clean_shutdown)

        # Publisher to goal commands
        self.goal_pub = rospy.Publisher(
            "/move_base_simple/goal", PoseStamped, queue_size=10
        )

        # Subscriber to goal result information (receives once a message when the robot arrived to its destination goal)
        self.result_sub = rospy.Subscriber(
            "/move_base/result", MoveBaseActionResult, self.result_callback
        )

        # Subscriber to current position information
        self.position_sub = rospy.Subscriber(
            "/amcl_pose", PoseWithCovarianceStamped, self.position_callback
        )

        # callback that handles the main robot logic every 0.1 second
        self.timer = rospy.Timer(
            rospy.Duration(MAIN_LOGIC_CALLBACK_INTERVAL), self.main_logic_callback
        )

        # Publisher to send velocity commands -- used to stop the robot
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

        self.goal: Optional[PoseStamped] = None

    def result_callback(self, msg: MoveBaseActionResult):
        """
        Callback function to process goal result data
        """
        # rospy.loginfo("Goal result %s", msg.status.status)
        self.goal_status = msg.status.status
        if self.goal_status == 3:
            rospy.loginfo("Goal reached successfully")
        elif self.goal_status == 4:
            rospy.loginfo("Goal was aborted by the action server")
        elif self.goal_status == 5:
            rospy.loginfo("Goal has been rejected by the action server")
        elif self.goal_status == 2:
            rospy.loginfo("Goal is being processed")
        elif self.goal_status == 1:
            rospy.loginfo("Goal received, but not yet processed")
        elif self.goal_status == 0:
            rospy.loginfo("Goal status is pending")

    def position_callback(self, msg: PoseWithCovarianceStamped):
        """
        Callback function to process robot position data
        This function will be called whenever a new amcl_pose message is received
        """
        rospy.loginfo(msg.pose.pose)

        if not self.goal:
            raise ValueError("No goal defined")

        curr_pos = msg.pose.pose.position
        goal_pos = self.goal.pose.position
        delta_x = goal_pos.x - curr_pos.x
        delta_y = goal_pos.y - curr_pos.y

        self.euclidean_distance = math.sqrt(delta_x**2 + delta_y**2)

        rospy.loginfo("distance to goal %f cm", self.euclidean_distance)

    def main_logic_callback(self, timer_event):
        """
        This function callback handles the main robot logic every
        MAIN_LOGIC_CALLBACK_INTERVAL seconds
        """
        # TODO
        pass

    # Main loop. spin is blocking and only allows to processes callbacks
    def run(self):
        while not rospy.is_shutdown():
            rospy.spin()

    def clean_shutdown(self):
        rospy.loginfo("Goal controller is shutting down.")

        # Send empty twist to stop the robot
        self.twist = Twist()
        self.cmd_vel_pub.publish(self.twist)

        rospy.loginfo("Robot stopped.")


if __name__ == "__main__":
    try:
        Controller().run()
    except rospy.ROSInterruptException:
        pass
