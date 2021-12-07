#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from ar_track_alvar_msgs.msg import AlvarMarkers

class scan_ar_tag():
	def __init__(self):

		self.detected_markers=set()
		self.markers_in_sight=['a']


	def callback(self, msg):

   		# markers_in_sight.clear() doesn't work. This is a Python 3.3+ command
   		self.markers_in_sight = []
   		n = len(msg.markers)
   		for i in range(n):
      			self.detected_markers.add(msg.markers[i].id)
      			self.markers_in_sight.append(msg.markers[i].id)
   			# print("detected_markers"+str(detected_markers))
   			# print(markers_in_sight)

	def getPose(self):
   		return [self.x,self.y,self.z]


	def odomCallback(self, msg):
 		print{"Test"}

	def main(self):


		rospy.init_node('ar_pose_subscriber', anonymous=False)
		rospy.Subscriber('/tb3_0/ar_pose_marker', AlvarMarkers, self.callback)
		rospy.Subscriber("/tb3_0/odom", Odometry, self.odomCallback)
		rospy.set_param('/start_flag', 'True')
		rospy.set_param('/finish_flag', 'False')

		current_marker_seq = 0
		foundID = 0

		rate = rospy.Rate(10)  # 10hz
		while not rospy.is_shutdown():
			#ar_action(self.markers_in_sight)
			rate.sleep()
			print "Wait for Tags"
			for ar_marks in self.markers_in_sight:
				if ar_marks == 0 or ar_marks == 1 or ar_marks == 3:
					id = ar_marks
					getPose(self)
					print "Fire found"
					rospy.set_param('ar_fire', {'id': NUMBER, 'position': {'x': self.x, 'y': self.y, 'z': self.z}})
					foundID += 1
				elif ar_marks == 2:
					id = ar_marks
					getPose(self)
					print "Person found"
					rospy.set_param('ar_human', {'id': NUMBER, 'position': {'x': self.x, 'y': self.y, 'z': self.z}})
					foundID += 1
				elif ar_marks == 4:
					id = ar_marks
					print "Large fire found"
					getPose(self)
					rospy.set_param('large_fire', {'id': NUMBER, 'position': {'x': self.x, 'y': self.y, 'z': self.z}})
					artagpost = getPose()
					foundID += 1
		    		#elif foundid == 5:
					#rosparam.set_param('finish_flag'= True)




if __name__ == '__main__':
   	scanAT = scan_ar_tag()
	scanAT.main()
