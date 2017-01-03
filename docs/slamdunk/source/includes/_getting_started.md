# Getting started

The Parrot S.L.A.M.dunk is powered by the following technologies:

- Ubuntu Trusty (14.04)
- ROS Indigo

To interact with it, you need a ROS Indigo compatible platform.
We recommend using Ubuntu 14.04,
which is the platform of reference the product has been tested against.
Refer to the ROS wiki for installation instructions:

- http://wiki.ros.org/indigo/Installation

It is also possible to develop on the Parrot S.L.A.M.dunk directly,
this may be convenient to get started quickly.

Once the ROS tools are installed,
it's possible to test the communication with the Parrot S.L.A.M.dunk node.

First step is to make sure the ROS environment is configured:

    source /opt/ros/indigo/setup.bash

Then you need to export the `ROS_MASTER_URI` to point to the ROS master.

A `roscore` node is running on the Parrot S.L.A.M.dunk,
this is documented in the [ROS Integration: roscore](#roscore) section.

<aside class="notice">
When working on the Parrot S.L.A.M.dunk itself (cf. <a href="#desktop-mode">Desktop Mode</a>),
it's not necessary to specify the <code class="prettyprint">ROS_MASTER_URI</code>
and <code class="prettyprint">ROS_HOSTNAME</code> variables below.
When not specified, the default value <code class="prettyprint">localhost</code> is used.
</aside>

When connected to the Parrot S.L.A.M.dunk on the Micro-USB 2.0 OTG port,
the `ROS_MASTER_URI` environement variable can be set to:

    export ROS_MASTER_URI=http://192.168.45.1:11311

You also need to export `ROS_HOSTNAME`.
This should be a name the Parrot S.L.A.M.dunk can contact.
If Bonjour/Zeroconf is supported, a possible value is:

    export ROS_HOSTNAME=$(hostname).local

<aside class="notice">
For more information, refer to the <a href="#network-setup">Network Setup</a> section.
</aside>

Now, to verify the setup is working,
we can list the nodes.
If everything is setup properly,
`/slamdunk_node` should appear in the output.

    $ rosnode list
    /rosout
    /slamdunk_node

And the product's firmware version should be printed when typing:

    $ rosparam get /properties/ro_parrot_build_version
    1.0.0

To list all the available topics:

    $ rostopic list
    ...
