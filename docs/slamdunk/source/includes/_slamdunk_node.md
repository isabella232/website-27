# The S.L.A.M.dunk node

The Parrot S.L.A.M.dunk comes with this ROS node preinstalled.
This makes it possible to run [rviz](http://wiki.ros.org/rviz)
and other ROS tools out of the box.

This how-to describes the process of building and running
your own SLAM.d.u.n.k. node.


## Why rebuild the node?

Rebuilding the node can be useful for a few reasons:

- You need it for performance reasons.
  In the node's process you can reduce copies, serializations and deserializations.

- There is a bug, or a missing feature that can only be accessed from the node.
  In this case it's recommended to open an issue on Github,
  so everyone can benefit from it:

  - https://github.com/Parrot-Developers/slamdunk_ros/issues


That said, if you don't need it, don't do it.

What we recommend is to subscribe to the node's topics in a new node
and integrate your algorithm(s) in this node (or nodelet).
The code of the node is not guaranteed to be stable
whereas the topics it exports have stronger stability guarantees.


## Build the slamdunk_ros packages

Please note that building and running S.L.A.M.dunk node
happens on the Parrot S.L.A.M.dunk itself.

This is necessary because the node uses
an unofficial SDK<sup id="slamdunk_node-unnoficial-sdk">[1](#slamdunk_node-fn1)</sup>.

Instructions to build the `slamdunk_ros` packages
are available in a dedicated section:

- [The slamdunk_ros package](#the-slamdunk_ros-packages).


## Stop and disable the system node

A slamdunk\_node is running by default on the product.

This node will conflict with the custom built node for 2 reasons:

1. the sensors API that the node uses can only be opened once,
   a second open will fail with an error similar to "Device or resource busy".
2. the topics exposed by the node will clash with the one of the system node.

To disable the node, type:

    sudo stop slamdunk_ros_node

More details on how to disable permanently and to restart it
is available in the [slamdunk_node](#slamdunk_node) section.


## Run the node

The node needs to be run as root,
this is required by the sensors API used by the node.

To start a shell session as root, type:

    sudo su

Activate the environement:

    # source devel/setup.bash

Export the node's name
so that other nodes can contact it<sup id="slamdunk_node-ros-network-setup">[2](#slamdunk_node-fn2)</sup>:

    # export ROS_HOSTNAME=$(hostname).local

To run the node, type:

    # roslaunch slamdunk_node slamdunk.launch


## Test the node

Open another shell as a simple user on Parrot S.L.A.M.dunk.

Setup the environment:

    source /opt/ros/indigo/setup.bash

To test the node, type:

    rostopic echo -n 3 /pose

This command output (values can vary):

    header:
      seq: 0
      stamp:
        secs: 1478180691
        nsecs: 224341794
      frame_id: map
    pose:
      position:
        x: 0.0
        y: 0.0
        z: 0.0
      orientation:
        x: -0.000348195433617
        y: -3.23653111991e-05
        z: 0.000101313009509
        w: 0.999999940395
    ---
    ...


## Cleanup

To stop the `slamdunk.launch` node, hit `^C`.

To restart the system node:

    sudo start slamdunk_ros_node

For more information,
refer to the section [slamdunk_node](#slamdunk_node).


## Final words

Now that the workspace is configured,
to work again on the project,
the steps to remember are the following:

First, you need to activate the environment once:

    source devel/setup.bash

Then you can proceed to the edit, compile and test cycle.
The command to compile is:

    catkin_make -j2

<aside class="notice">
Please remember to backup your code using version control or equivalent system.
</aside>


## Footnotes

<b id="slamdunk_node-fn1">1</b>
This SDK cannot be considered stable and API may change in the future,
the ROS SDK on the other hand will try to maintain backward compability.
[↩](#slamdunk_node-unnoficial-sdk)

<b id="slamdunk_node-fn2">2</b>
More information in the [Network Setup](#network-setup) section.
[↩](#slamdunk_node-ros-network-setup)
