#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose
from nav_msgs.msg import OccupancyGrid
from multi_robot_challenge.srv import SetPose

class robot_leader():
    def __init__(self):
        rospy.init_node('RobotLeader', anonymous=False)
        rospy.loginfo("Robot Leader class initiated")

        rospy.Subscriber('/map', OccupancyGrid , self.clbk_OG)
        self.pub = rospy.Publisher('/pose', Pose, queue_size=10)

    def clbk_OG(self, msg):
        self.currentMap = OccupancyGrid()
        # self.currentMap.data
        # self.currentMap.info
        self.currentMap = msg

    def main(self):


        rate = rospy.Rate(2)
        p = Pose()
        p.position.x = 0.5
        p.position.y = -0.1
        p.position.z = 1.0
        p.orientation.x = 0.0
        p.orientation.y = 0.0
        p.orientation.z = 0.0
        p.orientation.w = 1.0
        self.pub.publish(p)
        while not rospy.is_shutdown():
            rate.sleep()



    #Given map position returns cartesian coordinates
    def mapToPosition(self, map_pos):
        y_cell = math.floor(map_pos/self.map.info.width)
        x_cell = map_pos - y_cell*self.map.info.width
        position = Point()
        position.x = self.map.info.origin.position.x + (x_cell)*self.map.info.resolution
        position.y = self.map.info.origin.position.y + (y_cell)*self.map.info.resolution
        return position



        # Subscribe to mapmerging
        # Get a whitespace from OccupancyGrid
        # Get a position in the array (map_pos) and use that position in the mapToPosition function
        # Create service to communicate the target to robot
        # Create service to communicate the status to the robot

if __name__ == "__main__":
    leader = robot_leader()
    leader.main()
