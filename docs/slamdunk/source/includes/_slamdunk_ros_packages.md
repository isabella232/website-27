# The slamdunk_ros packages

## Why build the slamdunk_ros packages?

For first-time users of ROS,
building the packages is a good way to get a first
hands-on experience on using the ROS tools
for building and running nodes.

These tools includes, but are not limited to, [catkin](http://wiki.ros.org/catkin)
and [rosrun](http://wiki.ros.org/rosbash#rosrun).

The slamdunk\_ros packages offer a few useful things
apart from the S.L.A.M.dunk node itself:

- slamdunk\_visualization: rqt and rviz configuration,
  rviz plugin to display Parrot S.L.A.M.dunk-specific data
- slamdunk\_msgs: custom messages
- slamdunk\_nodelets: some nodelets that can also be run outside
  of the Parrot S.L.A.M.dunk
- and a few other packages to work with the Bebop Drone

## System prerequisites

<aside class="notice">
Note if you work on the Parrot S.L.A.M.dunk itself,
you need to configure internet access:

<ul>
  <li>
    <a href="#usb-to-ethernet-adapter">Network setup: USB to Ethernet adapter</a>
  </li>
</ul>
</aside>

    sudo apt-get update
    sudo apt-get install build-essential git

## Prepare catkin workspace

In this step we create a new empty [catkin](http://wiki.ros.org/catkin)
workspace.

    source /opt/ros/indigo/setup.bash
    mkdir -p ~/slamdunk_catkin_ws/src
    cd ~/slamdunk_catkin_ws/src
    catkin_init_workspace
    cd ~/slamdunk_catkin_ws/
    catkin_make -j2

Once the workspace is configured, you can activate the environment by typing:

    source devel/setup.bash


## Get the source

The source code of the node is available on Github:

* [https://github.com/Parrot-Developers/slamdunk_ros](https://github.com/Parrot-Developers/slamdunk_ros)

To download the sources, type:

    git clone https://github.com/Parrot-Developers/slamdunk_ros.git src/slamdunk_ros
    git clone https://github.com/Parrot-Developers/gscam.git src/gscam


### Disable slamdunk_node unless you build on Parrot S.L.A.M.dunk

The `slamdunk_node` and `slamdunk_bebop_robot` depends on `kalamos-context`,
which is a S.L.A.M.dunk-specific library.
To build the `slamdunk_ros` package outside of the Parrot S.L.A.M.dunk,
they need to be disabled.

    touch src/slamdunk_ros/slamdunk_node/CATKIN_IGNORE
    touch src/slamdunk_ros/slamdunk_bebop_robot/CATKIN_IGNORE


## Install dependencies

    sudo rosdep init
    rosdep update
    rosdep install --from-paths src --ignore-src


## Build the node

To actually build the code, type:

    catkin_make -j2


## What to do next?

- [run the rviz configuration](#the-slamdunk_visualization-package)
- [run the S.L.A.M.dunk node](#the-s-l-a-m-dunk-node)
