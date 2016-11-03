# Dynamic reconfiguration

Some of the Parrot S.L.A.M.dunk node parameters can be reconfigured dynamically.
The [dynamic_reconfigure](http://wiki.ros.org/dynamic_reconfigure) ROS tool is used
to modify these parameters.

To start `dynamic_reconfigure`,
first configure your environmnent
(also described in [Getting started](#getting-started)):

    source /opt/ros/indigo/setup.bash
    export ROS_HOSTNAME=$(hostname).local
    export ROS_MASTER_URI="http://192.168.45.1:11311"

Then type:

    rosrun rqt_reconfigure rqt_reconfigure slamdunk_node


## Change camera resolution and framerate

To change the camera resolution and FPS of the Parrot S.L.A.M.dunk,
use the **video_mode** drop-down list, and select the mode of your choice.

For example, to select a camera resolution of 1500x1500, and a framerate of 60 FPS do:

![dynamic_reconfigure 1500x1500](../images/dynamic_reconfigure_1500x1500.png "dynamic_reconfigure 1500x1500")

<aside class="notice">
If the cameras are already running,
you may need to restart the capture for the change to take effect.
</aside>

<aside class="warning">
Please note that, the "900x700 120 FPS" video mode is experimental.
Some tools, such as rviz might not work reliably in this setup
(depdending on the configuration in use).
The SLAM algorithm has not been tested for this mode.
Do not use this setting if you need any output of the SLAM such as the pose,
the keyframes, etc.
</aside>
