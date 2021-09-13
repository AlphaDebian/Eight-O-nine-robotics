# Team eight_onine_robotics

The following command sequence and instructions associated with it will help in simulating robot performing various tasks.
[Note: It is assumed that the docker is configured to run as user]
## Initiating repository

```
git clone https://github.com/artpark-robotics-challenge/team_eightonine.git
```
## Initiating Docker
Building the docker container
```
docker build -t eight_o_nine_robotics:test1 .
```
Initialising the docker container
```
docker run -it --name test-1 -v /home/mh/eight_o_nine_robotics/catkin_ws:/home/user/container_ws -v /tmp/.X11-unix:/tmp/.X11-unix:rw -w /home/user/container_ws -e DISPLAY="$DISPLAY" --runtime=nvidia --user=root artpark:test1 bash
```
## Initialising Project

```
roslaunch artpark spawn_urdf.launch
```
Open new terminal space using ``` docker exec -it test-1 bash ```and run

[Note: Make the file executable before launching using the following command]
```
rosrun laser_scan.py
```
