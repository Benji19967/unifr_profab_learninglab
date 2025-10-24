# Prototyping and Fabrication in the Learning Lab

Exercises for the course Prototyping and Fabrication in the Learning Lab at the University of Fribourg

Official course repo: https://github.com/nembrinj/protofablab/tree/main

## Creating a package

```bash
cd src/
catkin_create_pkg turtlebot3_profab std_msgs turtlebot3_msgs sensor_msgs geometry_msgs rospy
```

## Finding the IP address of the Raspberry Pi

Make sure the Raspberry is connected to the same local network as 
your laptop/PC (e.g. use ethernet cable for the Raspberry Pi)

```shell
hostname -I
sudo nmap -sn <hostname>/24
```
find ubuntu entry
## Git user isolation on bot (not great, separate HOMEs)

```shell
sudo adduser <name>
git config --global user.name "<name>"
git config --global user.email "<email>"
```

## Using ssh key of laptop

```shell
ssh -A <user>@<ip>
```
