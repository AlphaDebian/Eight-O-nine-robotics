FROM osrf/ros:melodic-desktop-full

RUN apt-get -y update && \
    apt-get install -y wget && \
    sh -c 'echo "deb http://package.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list' && \
    wget http://packages.ros.org/ros.key -O - | sudo apt-key add - && \
    apt-get -y update && \
    apt-get install -y tree \
    python-catkin-tools \
    ros-melodic-gazebo-plugins \
    ros-melodic-navigation \
    ros-melodic-rtabmap-ros \
    ros-melodic-turtlebot3-simulations \
    ros-melodic-turtlebot3-navigation \
    ros-melodic-dwa-local-planner \
    ros-melodic-move-base \
    ros-melodic-ros-control \
    ros-melodic-ros-controllers \
    ros-melodic-gmapping

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_COMPABILITIES,}graphics 

## nvidia-docker hooks
#LABEL com.nvidia.volumes.needed="nvidia_driver"
#ENV PATH /usr/local/nvidia/bin:${PATH}
#ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}

