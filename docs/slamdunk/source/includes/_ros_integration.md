# ROS integration

## Configure ROS environment

When working on the Parrot S.L.A.M.dunk,
there are two ROS setup scripts available.

The first one,
brings the standard ROS packages:

    source /opt/ros/indigo/setup.bash

The second one,
specific to the Parrot S.L.A.M.dunk,
brings both the standard ROS environment
and the S.L.A.M.dunk node environment.

    source /opt/ros-slamdunk/setup.bash

With this environment,
you can access the Parrot S.L.A.M.dunk messages,
for example:

    $ rosmsg list | grep slamdunk_msgs
    slamdunk_msgs/BoolStamped
    slamdunk_msgs/Quality
    slamdunk_msgs/QualityStamped
    ...


## Conventions for units and coordinate systems

When working with the Parrot S.L.A.M.dunk topics,
you may be wondering what are the units are,
what the frames of reference are,
etc.

We strive to be compliant to the ROS REPs:

- http://www.ros.org/reps/rep-0000.html

This means the depth images follows
the [REP 117](http://www.ros.org/reps/rep-0117.html)
& [REP 118](http://www.ros.org/reps/rep-0118.html),
the SLAM pose, follows [REP 105](http://www.ros.org/reps/rep-0105.html),
etc.


## roscore

The Parrot S.L.A.M.dunk runs a roscore
([wiki.ros.org/roscore](http://wiki.ros.org/roscore)) by default,
this is offered as a convenience.

Howewer, in a distributed setup, when multiple robots are involved,
the role of the master node may be entrusted to another machine.
Thus, the roscore running on the Parrot S.L.A.M.dunk needs to be shut down.

The roscore runs as a system service, using Ubuntu 14.04 init system:
[upstart](http://upstart.ubuntu.com).
The service configuration file is located at: `/etc/init/roscore.conf`.

To stop the roscore temporarily (until next reboot), type:

    sudo stop roscore

To start it, type:

    sudo start roscore

To disable the roscore permanently (across reboots)<sup id="ros-integration-upstart-manual-override">[1](#ros-integration-fn1)</sup>,
use:

    echo manual | sudo tee /etc/init/roscore.override

If you want the roscore back, just delete the override file and start the service:

    sudo rm /etc/init/roscore.override
    sudo start roscore


## slamdunk_node

The `slamdunk_node`<sup id="ros-integration-slamdunk-node">[2](#ros-integration-fn2)</sup>,
is also running by default on the product.

The service configuration file is located at: `/etc/init/slamdunk_ros_node.conf`.

To stop the node temporarily (until next reboot), type:

    sudo stop slamdunk_ros_node

To start it, type:

    sudo start slamdunk_ros_node

To disable the node permanently (across reboots)<sup id="ros-integration-upstart-manual-override">[1](#ros-integration-fn1)</sup>,
use:

    echo manual | sudo tee /etc/init/slamdunk_ros_node.override

If you want the node back, just delete the override file and start the service:

    sudo rm /etc/init/slamdunk_ros_node.override
    sudo start slamdunk_ros_node


## Footnotes

<b id="ros-integration-fn1">1</b>
More information on disabling a job can be found here:
http://upstart.ubuntu.com/cookbook/#disabling-a-job-from-automatically-starting
[↩](#ros-integration-upstart-manual-override)

<b id="ros-integration-fn2">2</b>
This node is available on Github (https://github.com/Parrot-Developers/slamdunk_ros)
and is described in the [S.L.A.M.dunk node](#the-s-l-a-m-dunk-node) section.
[↩](#ros-integration-slamdunk-node)
