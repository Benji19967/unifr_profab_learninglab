sim_collavoidance:
	roslaunch turtlebot3_profab sim_collavoid.launch


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

teleop:
	roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

gazebo:
	roslaunch turtlebot3_gazebo turtlebot3_world.launch
