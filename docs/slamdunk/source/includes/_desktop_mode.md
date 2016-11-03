# Desktop mode

It's possible to work on Parrot S.L.A.M.dunk directly,
as if it were a personal computer.
To do so, connect an HDMI monitor, a mouse, a keyboard,
most likely with the help of a USB hub.

You may also need network access,
for example to install packages,
refer to [Network setup: USB to Ethernet adapter](#usb-to-ethernet-adapter).

A few scripts are provided to install a desktop and a few ROS tools.
These scripts are provided as a convenience,
they are not required to work on the Parrot S.L.A.M.dunk itself.

To installs a desktop enviromnent:

```bash
sudo ~/scripts/install_desktop.sh
sudo start lightdm
```

To install a few ROS tools, such as rviz:

```bash
sudo scripts/install_ros_tools.sh
```

To run rviz,
source the Parrot S.L.A.M.dunk environment
(c.f. [ROS integration: Configure ROS environment](#configure-ros-environment))
and launch `rviz`:

```bash
source /opt/ros-slamdunk/setup.bash
rviz -d $(rospack find slamdunk_visualization)/rviz/slamdunk.rviz
```

<aside class="warning">
Please remember to backup your work when working directly
on the Parrot S.L.A.M.dunk.
If during testing you damage your product you can easily lose some of your work.
</aside>
