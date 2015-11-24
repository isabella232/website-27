---
layout: post
title:  "Running Ardupilot on Bebop Drone"
date:   2015-11-24 07:20:00
categories: bebop apm C linux opensource
longtitle: "Complete Tutorial on running APM on Bebop drone"
author: Julien Beraud
description: Running Ardupilot on Bebop Drone
---

These instructions clarify how to build ArduPilot for the Bebop flight controller board on a Linux machine. More details on the Bebop can be found [here](http://copter.ardupilot.com/wiki/parrot-bebop-autopilot/).

##### Bebop support was added in Copter-3.3

##### Bebop 2 is not supported yet, this tutorial covers Bebop 1 only

###### Making the changes described in this article will void your warranty!
######Parrot’s technical support will not help you with this hack or to recover your original software.
######Hacking a commercial product is risky! This software is still evolving, and you may well find issues with the vehicle ranging from poor flight to complete software freeze.
######That said, it is almost always possible to recover a drone and members of the ardupilot dev team can likely help people hacking or recovering their Bebop. Prepare to spend some time, patience and develop some hardware/software skills.


#Upgrading the firmware
As of Nov 2015, the Bebop ships with a version of Linux that cannot run ArduPilot and must be upgraded. In order to upgrade it, you will need to download a custom version [here](https://github.com/Parrot-Developers/ardupilot/releases/download/bebop-v0.0/bebopdrone_update.plf).

In order to upgrade to this version:

1- Power up your Bebop

2- Connect to its Wi-Fi network (BebopDrone-XXXX)

3- Connect to it via ftp

	ftp 192.168.42.1

4- Go to the eMMC directory

	cd internal_000

5- Upload the update file

	put bebopdrone_update.plf

6- Connect to the Bebop by telnet

	telnet 192.168.42.1

7- Sync and reboot

	sync
	reboot

8- Wait for the Bebop to perform the update (this could take several minutes)

**Don’t shutdown your Bebop during this time**

9- When the update is complete you can connect again via Wi-Fi and telnet and verify the update by checking the software version indicates 0.0.0 (not an official release)

	cat version.txt

# Build ArduCopter for Bebop
The following steps show how to build a custom version of the Copter software for Bebop:

##Install armhf toolchain
###On Ubuntu from 12.04
1- Install the official arm-linux-gnueabihf toolchain

	sudo apt-get install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf


###On other Linux distributions

1- Install the arm-gnueabihf tool chain that can be downloaded from [here](https://releases.linaro.org/14.07/components/toolchain/binaries/gcc-linaro-arm-linux-gnueabihf-4.9-2014.07_linux.tar.bz2)

2- Extract the tar archive (for instance in /opt)

	sudo tar -xjvf gcc-linaro-arm-linux-gnueabihf-4.9-2014.07_linux.tar.bz2 -C /opt/

3- Add the path to the toolchain to the PATH variable

	export PATH=/opt/gcc-linaro-arm-linux-gnueabihf-4.9-2014.07_linux/bin:$PATH

##Download and compile ArduCopter

1- You need to install git first (see instructions[ here](https://git-scm.com/book/fr/v1/Démarrage-rapide-Installation-de-Git))

2- Clone ardupilot repository

	git clone https://github.com/diydrones/ardupilot.git

3- Building the flight control firmware is nearly identical for building for the Pixhawk except the make command is:

	cd ardupilot/ArduCopter
	make bebop

4- Strip the binary to reduce the memory footprint:

	arm-linux-gnueabihf-strip ArduCopter.elf -o arducopter

##Uploading the firmware

1- If you haven’t built the firmware as described in the previous steps you can download a binary version [here](https://github.com/Parrot-Developers/ardupilot/releases/download/bebop-v0.0/arducopter)

2- Connect again by ftp and go to the eMMC directory

3- Put the arducopter binary

	put arducopter

4- Connect to the Bebop via telnet

5- Copy arducopter to /usr/bin and change permissions

	cp /data/ftp/internal_000/arducopter /usr/bin
	chmod +x /usr/bin/arducopter

##Starting ArduPilot

1- Connect via telnet

2- Kill the regular autopilot

	kk

3- Launch Copter

	arducopter -A udp:192.168.42.255:14550:bcast -B /dev/ttyPA1 -C udp:192.168.42.255:14551:bcast -l /data/ftp/internal_000/APM/logs -t /data/ftp/internal_000/APM/terrain

##Changing the GPS configuration
In order to get Bebop’s GPS to send the NMEA frames that APM’s NMEA driver understands, you need to change its configuration. To achieve this you will need to stop the in-build autopilot as described previously (and don’t launch Copter yet):


1- Download the gps_config file [here](https://github.com/Parrot-Developers/ardupilot/releases/download/bebop-v0.0/gps_config.txt)

2- Connect to the Bebop via ftp and go to the eMMC directory as indicated in the “Upgrading the firmware” section above

3- Put the config file

	put gps_config.txt

4- Connect to the Bebop via telnet

5- Copy gps_config.txt in /etc/

	cp /data/ftp/internal_000/gps_config.txt /etc/

6- Launch the GPS config updater

	libgps_cli

7- Wait for NMEA messages to be displayed in the console

8- Stop libgps_cli by typing Ctrl-C

##Launch Copter at startup

It is a lot more convenient to automatically execute Copter startup than connect and do this manually. In order to do so, the startup scripts need to be hacked in the following way.


######This part is critical since you have to edit the startup script. If you do something wrong here, you could end up with a Bebop that can no longer boot properly. If this happens you will have to get a UART cable to recover.


The startup script is located at /etc/init.d/rcS. You will need to edit it to remove the lines launching the regular autopilot and replace them by launching Copter. The line in question is the following:

	echo "Launching Dragon" | logger -s -t "rcS" -p user.info

Replace this with:

	arducopter -A udp:192.168.42.255:14550:bcast -B /dev/ttyPA1 -C udp:192.168.42.255:14551:bcast -l /data/ftp/internal_000/APM/logs -t data/ftp/internal_000/APM/terrain &

In order to avoid editing the file manually, download this rcS file [here](https://github.com/Parrot-Developers/ardupilot/releases/download/bebop-v0.0/rcS).

1- Make a copy of the original rcS file for recovery purpose

	cp /etc/init.d/rcS /etc/rcS_backup

2- Connect to the Bebop via ftp and put the rcS file in the eMMC as described before for the other files.

3- Then copy it manually to overwrite /etc/init.d/rcS and change permissions

	cp /data/ftp/internal_000/rcS /etc/init.d/rcS
	chmod +x /etc/init.d/rcS

4- Sync and reboot

	sync
	reboot

5- In case you want to put your Bebop back to normal and use the normal autopilot and app again, just replace /etc/init.d/rcS with the backup file, sync and reboot

	cp /etc/rcS_backup /etc/init.d/rcS
	sync
	reboot



#####If you put your software back to normal and use your Bebop with FreeFlight smartphone App, you might be asked to upgrade your software version. If you do so, you will have to repeat some of the previous steps, at least for the GPS config, copying arducopter and modifying the init scripts. Regarding the need to upgrade to a custom version, it will depend on whether some options will or won’t be available in the following release. Informations to follow…

##Recovery

1- In case something went wrong and you are not able to boot your Bebop anymore

2- The UART port is located under the Bebop’s neck on the right side (facing the front camera)

![uart](http://developer.parrot.com/blog/assets/images/apm1.jpg)

3- You will have to pull back the polystyrene a bit but it shouldn’t cause much damage

4- Get a UART cable like [this one](http://www.digikey.com/product-detail/en/TTL-232R-RPI/768-1204-ND/4382044) or any FTDI 3 pin cable (GND TXD RXD)

5- Get headers like [these ones](https://www.aimagin.com/2-54-mm-straight-male-single-pin-header-connectors.html) and plug them into the cable like this:

![cable](http://developer.parrot.com/blog/assets/images/apm2.jpg)

The color codes for the cable are usually:

	black = GND
	yellow = RXD
	orange = TXD

6- Plug the cable into the Bebop like this:

![orientation](http://developer.parrot.com/blog/assets/images/apm3.jpg)


Be careful about the pinout:

	black: front
	yellow: middle
	orange: back

7- Install a UART terminal emulator like minicom and connect to a Bebop once it is powered up

8- Copy the backup rcS file back to its original place, sync and reboot:

	mount -o remount,rw /
	cp /etc/rcS_backup /etc/init.d/rcS
	sync
	reboot


##Flying

FreeFlight 3 is not compatible with ArduPilot and you will therefore have to use [one of the supported GCS](http://copter.ardupilot.com/wiki/common-choosing-a-ground-station/). Connect to the Bebop via Wi-Fi and just start your GCS, it should connect automatically if you setup the link to UDP (in case it is needed).

The SkyController is not compatible with apm with its regular firmware. You would need to flash an alternative version in order to be able to control your Bebop with it (information about that is coming soon…).

In order to pilot the Bebop manually, Mission Planner GCS users can use a gamepad [as described here](http://copter.ardupilot.com/wiki/flying-with-a-joystickgamepad-instead-of-rc-controller/).  Alternatively use the RCOutput UDP interface on port 777 on the Bebop, with a Linux PC (or board type Raspberry Pi) and a USB gamepad.

##Controlling the Bebop via RC over UDP on Linux

1- In order to control the arducopter for Bebop via RC over UDP, you can either write an application using [this protocol](https://github.com/diydrones/ardupilot/blob/master/libraries/AP_HAL_Linux/RCInput_UDP_Protocol.h) and sending a packet every 10ms

2- Or use [joystick_remote](https://github.com/jberaud/joystick_remote) Linux application

3- In order to do so, clone the git repository:

	git clone https://github.com/jberaud/joystick_remote.git


4- Build it

	cd joystick_remote
	make

5- Plug a USB gamepad (the list of supported gamepads is explained if you type joystick_remote –help)

6- In case your gamepad is not supported you can easily add support for it if you know its mapping

7- Connect to the Bebop via Wi-FI and launch the application:

	./joystick_remote -d /dev/input/js[X] -t [gamepad] -r 192.168.42.1:777

where [X] is the device number of your joystick that you can easily find, usually 0 but sometimes 1 if your laptop already includes an input device like an accelerometer and [gamepad] is one of the supported gamepads.

8- so for an XBox 360 gamepad mapped on /dev/input/js0 the command line becomes

	./joystick_remote -d/dev/input/js0 -t xbox_360 -r 192.168.42.1:777

9- The flight modes have to be set in Copter’s parameters in order to use the buttons to set the flight modes


##Basic configuration and frame parameters

1- In order to do the basic configuration and calibration, you can use any of the GCSs and perform

	Magnetometer Calibration
	RC Calibration
	Accelerometer Calibration

2- Thanks to Leonard Hall, we have a very good set of tuning parameters that you can find [here](https://github.com/diydrones/ardupilot/blob/master/Tools/Frame_params/Parrot_Bebop.param)

##Known limitations

-The GPS of the Bebop isn’t very good compared to a UBlox GPS and therefore the Bebop drifts significantly in Loiter, PosHold and
other GPS modes

-Mission run in Auto mode work reasonably well but we recommend you takeoff and land in a non-GPS mode such as AltHold or Stabilize.

-Some work will be done to improve support for this GPS

-The optical flow is currently under development

-There is currently no support for video streaming and capture
