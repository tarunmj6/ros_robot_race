# ros_robot_race
A python program to make ros simulated robot complete racetrack

The starter code is available from  https://github.com/uml-robotics/uml_race.git
Under scripts there is a python file "tarun_rosrace.py" which makes the robot complete the ractrack given in the starter code.
The python code subcribes to "/robot/base_scan" topics to get the sensor reading of the robot and publishes the speed and rotation to the topic "/robot/cmd_vel"

To run this simulation on one node(terminal) run "roslaunch ros_robot_race racetrack.launch" which opens the racetrack and on another node run "rosrun ros_robot_race tarun_rosrace.py" which makes the robot run the racetrack
