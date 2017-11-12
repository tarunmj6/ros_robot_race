#!/usr/bin/env python
import roslib; roslib.load_manifest('assign3')
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub=rospy.Publisher('/robot/cmd_vel',Twist,queue_size=1)

def talker(data):
	rospy.loginfo('%f %f', data.ranges[0],data.ranges[179])
	msg = Twist()
	right = data.ranges[0]
	left = data.ranges[179]
	speed = data.ranges[89]	
	right1 = data.ranges[44]
	left1 =data.ranges[134] 
	if left < right:
		msg.linear.x= left1-.5
		msg.angular.z=-.28
	elif left > right:
		msg.linear.x= right1-.5
		msg.angular.z=.28
	elif left == right:
		#msg.linear.x=.15
		#msg.angular.z=0
		if left1 < right1:
			msg.linear.x=.15
			msg.angular.z=-.30
		elif right1 < left1:
			msg.linear.x = .15
			msg.angular.z=.30
	#elif data.ranges[0]>1.6 and data.ranges[179]<1.6:
	#	msg.linear.x=0
	#	msg.angular.z=-.25
	pub.publish(msg)
	
def listener():
	rospy.init_node('ListenerTalker',anonymous=True)
	rospy.Subscriber('/robot/base_scan', LaserScan,talker)
	rospy.spin()

if __name__=='__main__':
	listener()
