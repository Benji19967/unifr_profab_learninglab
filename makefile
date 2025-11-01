sim_collavoidance:
	roslaunch turtlebot3_profab sim_collavoid.launch

sim_goal:
	rosrun turtlebot3_profab goal_controller.py


# Control robot
#
# 1.) local-1: roscore
# 2.) local-2: make ssh_robot
# 3.) robot-1: roslaunch turtlebot3_bringup turtlebot3_robot.launch

# 4.a) local-3: make teleop
# 4.b) local-3: rosrun turtlebot3_profab ca_controller.py

# To see the real robot in simulation
# 5.) Optional: make gazebo 

ssh_robot:
	ssh ${TURTLEBOT3_HOSTNAME}

robot:
	roslaunch turtlebot3_bringup turtlebot3_robot.launch

teleop:
	roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

gazebo:
	roslaunch turtlebot3_gazebo turtlebot3_world.launch

slam:
	roslaunch turtlebot3_slam turtlebot3_slam.launch

navigation:
	roslaunch turtlebot3_navigation turtlebot3_navigation.launch

navigation_map:
	roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/ubuntu/profab_ws/map/simulation.yaml

# CAMERA
# 1.) On computer:
# make navigation (launches rviz)
# 2.) On robot:
camera:
	roslaunch turtlebot3_profab turtlebot3_robot_usbcam.launch
# Check it works:
# rostopic echo /usb_cam/camera_info
# rostopic echo /usb_cam/camera_info
# Otherwise: pgrep video and pkill -9 <video-process-id>

light_node:
	rosrun rosserial_python serial_node.py tcp 11511

server:
	roslaunch rosbridge_server rosbridge_websocket.launch

rqt:
	rqt
