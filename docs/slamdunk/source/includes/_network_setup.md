# Network setup

In this section we describe the network setup of the Parrot S.L.A.M.dunk.

ROS being a distributed system,
it is useful to know how the different machines can communicate together.

Regarding this subject, the ROS Network Setup wiki page is a good read:

- http://wiki.ros.org/ROS/NetworkSetup


## USB Ethernet Gadget/RNDIS

A DHCP server is listening to connection on the Micro-USB 2.0 OTG port.
When a device connects to the port, the Parrot S.L.A.M.dunk
will offer an IP adress to the device.

- the Parrot S.L.A.M.dunk address is 192.168.45.1
- the addresses offered are of the form 192.168.45.XX

After connecting the Parrot S.L.A.M.dunk to a computer,
to test the connection, type:

    ping -c 1 192.168.45.1

To get your address:

    $ hostname -I | grep -o '192\.168\.45\...'
    192.168.45.48


## Wi-Fi USB dongle

Parrot S.L.A.M.dunk can also serve as a wireless access point
when a Wi-Fi USB dongle is plugged in.

- SSID: SLAMDunk-XXXXXX

  Where `XXXXXX` is the relevant part of the equivalent
  Parrot S.L.A.M.dunk hostname:

        $ hostname
        slamdunk-XXXXXX

- the Parrot S.L.A.M.dunk address is 192.168.44.1
- the addresses offered are of the form 192.168.44.XX

After connecting to the Parrot S.L.A.M.dunk via Wi-Fi,
to test the connection, type:

    ping -c 1 192.168.44.1

To get your address:

    $ hostname -I | grep -o '192\.168\.44\...'
    192.168.44.27


## USB to Ethernet adapter

When an USB to Ethernet adapter is plugged to the USB 3 host port,
the Parrot S.L.A.M.dunk will emit a DHCP request.
It's not a DHCP server, this time it's a client.

This is useful to install packages from the internet.
Just plug an USB to Ethernet adapter,
plug the Parrot S.L.A.M.dunk to your network and install packages.

To verify the network access, type:

    ping -c 1 google.com


## Bonjour/Zeroconf

The Parrot S.L.A.M.dunk also offers Bonjour/Zeroconf symbolic names.

First there is the `$(hostname).local` name (e.g: `slamdunk-000042.local`).
This one is useful to communicate with the Parrot S.L.A.M.dunk
regardless of the interface used.

For example,
the Parrot S.L.A.M.dunk roscore node is launched with the `ROS_HOSTNAME`
variable set to this value.

    export ROS_HOSTNAME=$(hostname).local

And in a multi Parrot S.L.A.M.dunk setup,
where one of the device is the master,
it would make sense to specify the `ROS_MASTER_URI` to this value:

    $ export ROS_MASTER_URI=http://kalamos-000042.local:11311

Then there is one symbolic name for the USB host interface
and one for the wireless access point interface.

- USB: `slamdunk-usb.local` (192.168.45.1)
- WLAN: `slamdunk-wifi.local` (192.168.44.1)
