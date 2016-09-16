---
layout: post
title:  "ARSDK 3.10.0 release"
date:   2016-09-15 10:00:00
categories: sdk drones Disco Swing Mambo SkyController2
longtitle: "ARSDK, what's new in the 3.10.0 release"
author: Djavan Bertrand
description: Explanation of all the changes brought by the 3.10.0 release of the ARSDK
---

With all the [new products](https://www.parrot.com/) we have released recently, a new version of the SDK necessarily comes. 
This release brings support to: 

* SkyController 2
* Disco
* Swing
* Mambo

And still supports:

* Bebop
* Bebop 2
* JumpingSumo
* Jumping Night
* Jumping Race
* RollingSpider
* Airborne Night
* Airborne Cargo
* Hydrofoil
* SkyController

Wow, that's a lot of possibility right?!

For those who don't know yet, the sdk lets you build apps (iOS and Android) or Linux binaries to control the Parrot products previously mentioned.

**To update your app, your just have to change in the build.gradle of your Android app the version of the sdk: `compile 'com.parrot:arsdk:3.10.0'`.<br/>
In your iOS app, replace the libs with the one you can download [here](https://github.com/Parrot-Developers/arsdk_manifests/releases/download/ARSDK3_version_3_10_0/ARSDK3_iOS_3_10_0.zip).**

# Small compatibility break
 
Because we have added a new library called libmux, you will have to add to your application this new library:

For Android, in the settings.gradle:

```
include 'libmux'
project(':libmux').projectDir = new File('../../../../libmux/android')
```

For iOS, in the Other Linker Flags:

```
-lpomp -lmux
```

Then, on iOS, if you don't need to support the SkyController 2, change the `-lardiscovery` in Other Linker Flags by `-lardiscoverywithouteacc`. Otherwise you'll also need to add the External Accessory framework.

Also, for the Android Sample, we are now targetting Android 24. This will require you to update Android SDK version to 24 and to have Java 1.8 installed.

# SkyController 2 support

The SkyController 2 support brings a new network type to handle: USB. To communicate with the SkyController 2 through the USB wire, you'll have to use a mux, provided by the new [*libmux*](https://github.com/Parrot-Developers/libmux). 

The following instructions are modification to a already working codebase. If you want to start from the bottom, please read [the documentation](http://developer.parrot.com/docs/SDK3/) and have a look at the [samples](https://github.com/Parrot-Developers/Samples). You can find an implementation of these instructions in the commit that modifies the [ios](https://github.com/Parrot-Developers/Samples/commit/19b8c8029c25b721fa9b43d8d6ce36ba888fb3aa) and [Android](https://github.com/Parrot-Developers/Samples/commit/e8f320f0f17290b772b97d36bf4a4243aeeacdff) samples.

## Discovering a SkyController 2

### Android
To be notified when a SkyController 2 is plugged into an Android device, you should declare in the manifest the feature *usb accessory*:

```
<uses-feature android:name="android.hardware.usb.accessory" android:required="false"/>
```

Then, in the manifest declare an activity which will be created when the accessory is attached:

```
<activity android:name=".activity.UsbAccessoryActivityImpl"
    android:theme="@android:style/Theme.NoDisplay"
    android:noHistory="true"
    android:taskAffinity="com.parrot.sdk.usb">
    <intent-filter>
        <action 
            android:name="android.hardware.usb.action.USB_ACCESSORY_ATTACHED" />
    </intent-filter>
    <meta-data
        android:name="android.hardware.usb.action.USB_ACCESSORY_ATTACHED" 
        android:resource="@xml/usb_accessory_filter" />
</activity>
```

After that, create `usb_accessory_filter.xml` in res/xml:

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <usb-accessory manufacturer="Parrot" model="Skycontroller 2" />
</resources>
```

Then, create the UsbAccessoryActivityImpl: 

```
import com.parrot.arsdk.ardiscovery.UsbAccessoryActivity;

public class UsbAccessoryActivityImpl extends UsbAccessoryActivity {
    @Override
    protected Class getBaseActivity() {
        return DeviceListActivity.class;
    }
}
```

The class returned by the function `getBaseActivity()` is the activity that will be created or brought back to front.

After this step, you can check that you are seeing the SkyController 2 in the discovered devices when you plug it.

### iOS
The iOS case is a bit more complicated, as you will have to add the ExternalAccessory framework. To use this framework in production (on apps available on the AppStore), a special validation from Apple will be asked. You will need to send us details from your app. If this is your case, please send us a message on the [forum](http://forum.developer.parrot.com/).

So first of all, add the ExternalAccessory framework to your project. 

Then, declare in your info.plist the key `UISupportedExternalAccessoryProtocols` with the value `com.parrot.dronesdk` as stated in the [iOS documentation](https://developer.apple.com/reference/externalaccessory).

Nothing else to do, you'll be automatically informed by the discovery when a SkyController 2 is plugged/unplugged.


## Connection to a SkyController 2

### Android
Once you have an ARDiscoveryDeviceService with a product of the type `ARDISCOVERY_PRODUCT_SKYCONTROLLER_2` you can create a instance of ARDiscoveryDevice with:

```
ARDiscoveryDevice device = new ARDiscoveryDevice();
device.initUSB(productType, UsbAccessoryMux.get(mContext.getApplicationContext()).getMux());
```
After this step, you're ready to create your DeviceController.

### iOS
Once you have an ARService with a product of the type `ARDISCOVERY_PRODUCT_SKYCONTROLLER_2` you can create a instance of ARDISCOVERY_Device_t with:

```
ARDISCOVERY_Device_t *device = ARDISCOVERY_Device_New (&errorDiscovery);
if (errorDiscovery == ARDISCOVERY_OK) {
    errorDiscovery = ARDISCOVERY_Device_InitUSB(device, service.product, ((ARUSBService*)service.service).usbMux);
}
```

After this step, you're ready to create your DeviceController.

## After the connection

After the connection, you can use the SkyController 2 as you would use a SkyController. That means that you'll be notified by the callback extensionStateChanged when a drone is connected or disconnected from your SkyController 2.

# Disco

The Disco is the a brand new product. It is a fixed wing which flies up to 80km/h (50 mph). This drone uses quite the same API than the Bebop and Bebop 2. So you'll have to use the feature ARDrone3 (`deviceController.getFeatureARDrone3()` for Android and `deviceController->aRDrone3` for iOS).

Here is a small list of the differences:

### TakeOff process
As the Disco can't takeoff without the help of the user, the takeoff process is different from the quadcopters one.<br/>
You first have to prepare the drone to take off by sending the *userTakeOff* command:

On Android:

```
deviceController.getFeatureARDrone3().sendPilotingUserTakeOff((byte)1);
```

On iOS:

```
deviceController->aRDrone3->sendPilotingUserTakeOff(deviceController->aRDrone3, (uint8_t)1);
```

Then, the Disco will send back its flying state set at *motor ramping* and at the same time begin to arm its motors if they are not already armed.<br/>
Once the motors are armed, the flying state will be set at *user takeoff*. That means that the drone is ready to take off and wait to be thrown by the user.<br/>
As soon as the user throws it, it will take off and its flying state will be set at *taking off*.<br/>

### Piloting
Since the Disco is not a quadcopter, the piloting command differs from the one used by the Bebop. In fact, it is the same command but parameters are understood differently.

* flag (u8): Boolean flag: 1 if the roll and pitch values should be taken in consideration. 0 otherwise<br/>
* roll (i8): Roll angle expressed as signed percentage of the physical max roll of the wing, in range [-100, 100]<br/>
Negative value makes the plane fly to the left<br/>
Positive value makes the plane fly to the right<br/>
* pitch (i8): Pitch angle as signed percentage expressed as signed percentage of the physical max pitch of the wing, in range [-100, 100]<br/>
Negative value makes the plane fly in direction of the sky<br/>
Positive value makes the plane fly in direction of the ground<br/>
* yaw (i8): Giving more than a fixed value (75% for the moment) triggers a circle.
Positive value will trigger a clockwise circling<br/>
Negative value will trigger a counter-clockwise circling<br/>
* gaz (i8): Throttle as signed percentage expressed as signed percentage of the physical max throttle, in range [-100, 100]<br/>
Negative value makes the plane fly slower<br/>
Positive value makes the plane fly faster<br/>
* timestampAndSeqNum (u32): Command timestamp in milliseconds (low 24 bits) + command sequence number [0;255], (high 8 bits) (generated by libARController).<br/>

### New commands
With a new type of drone comes new commands:

* [Circle](http://developer.parrot.com/docs/SDK3/#a-name-ardrone3-piloting-circle-a): makes the drone circle (loiter).
* [Circle altitude](http://developer.parrot.com/docs/SDK3/#a-name-ardrone3-pilotingsettings-circlingaltitude-a): configure the circling altitude.
* [Circle radius](http://developer.parrot.com/docs/SDK3/#a-name-ardrone3-pilotingsettings-circlingradius-a): configure the circling radius.
* [Circle default direction](http://developer.parrot.com/docs/SDK3/#a-name-ardrone3-pilotingsettings-circlingdirection-a): configure the circling default direction.

# Mambo
The Mambo comes with accessories. This is the commands related to them:

You can get state of accessories with the event *ClawState* and *GunState*.
If the gun is ready, you can fire a shot with the command *GunControl* and action *fire*.

# Swing

The Swing brings a new way of piloting. You can choose between a plane and a quadcopter.

The take off is done the same way as the Mambo or the Airborne drones.

Once the Swing is flying you can change its flying mode with the command *PilotingFlyingMode* which lets you 3 mode:

- quadricopter: the default mode, the Swing flies as a quadcopter
- plane_forward: the Swing flies like a plane with its bottom directed to the floor
- plane_backward: the Swing flies like a plane with its top directed to the floor

Once you're in plane mode, you have access to a gear box that let's you specify the inclination (the speed of the drone is related to its inclination). The command to specify the gear box is *PilotingPlaneGearBox*. Also, in plane mode, the drone won't respond to the roll values you'll send to it.

<br/><br/><br/>

That's it for this release. Don't forget to read our [documentation](http://developer.parrot.com/docs/SDK3/) and if you have any questions, feel free to ask them on our [forum](http://forum.developer.parrot.com/) (if other devs haven't already asked/answered them).

Happy coding !