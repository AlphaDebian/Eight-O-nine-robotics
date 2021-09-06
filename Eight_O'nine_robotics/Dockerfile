FROM osrf/ros:melodic-desktop-full
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}

ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

RUN apt-get update && apt-get install -y apt-utils build-essential psmisc vim-gtk
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update && apt-get install -q -y python-catkin-tools
RUN apt-get update && apt-get install -q -y ros-melodic-hector-gazebo-plugins

# Required python packages for analysis
RUN \
  apt-get install -y python-pip && \
  pip install matplotlib==2.0.2 && \
  pip install numpy && \
  pip install scipy && \
  pip install jupyter && \
  pip install seaborn && \
  pip install pandas && \
  pip install bokeh && \
  pip install rosbag_pandas
CMD ["bash"]
