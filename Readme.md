# Team eight_onine_robotics

The following command sequence and instructions associated with it will help in simulating *Janatics* performing various tasks.

## Initiating repository

```
git clone https://github.com/artpark-robotics-challenge/team_eightonine.git
```
## Initiating Docker

```
docker build -t eight_onine_robotics
Open a new terminal and run
sudo docker exec -it  artpark_workspace_sim_container bash

docker run -it --name eight_onine_robotics -v /tmp/.X11-unix:/tmp/.X11-unix:rw -e DISPLAY="$DISPLAY" --runtime=nvidia --user=root artpark:final bash
```

## ALTERNATIVELY: if the Dockerfile somehow fails

```
catkin build

source ~/catkin_ws/devel/setup.bash

```

The only pre-requisites for this project are:

- Ubuntu 18.04
- ROS Melodic
- Gazebo 9



