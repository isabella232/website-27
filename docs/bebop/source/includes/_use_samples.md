## Use samples

To have a good overview of what you can do with the SDK, you can start by using and browsing the code of the samples we provide. 

For that, simply clone the Sample repository:<br/>
`git clone https://github.com/Parrot-Developers/Samples.git`

There is one example for iOS, one for Android and a few for Unix. 
The mobile samples use the following architecture:<br/> 
![alt mobile_uml](https://raw.githubusercontent.com/Parrot-Developers/Samples/master/Android/uml/mobile_uml_classes.png)

They are standalone, this means that you can clone the sample repo and use them without compiling the SDK. To enable this, they will use the precompiled SDK libraries.

The mobile samples show you how to connect, pilot, take pictures, display video stream if available, and download medias from the drone.

They support the following drones:

* Bebop 2
* Bebop 
* JumpingSumo 
* Jumping Race
* Jumping Night
* MiniDrone Rolling Spider
* Airborne Cargo
* Airborne Night
* Swing
* Mambo
* SkyController
* SkyController2


*What if you want to only build an app for the Bebop?
Simply delete other files than:*

* *DeviceListActivity*
* *DroneDiscoverer*
* *BebopActivity*
* *BebopVideoView*
* *BebopDrone*
* *SDCardModule*

As said before, each mobile sample can be used without having to build the SDK: it will use the precompiled libraries. But you can also use the sample with your own compiled SDK.

### iOS

**Use the precompiled SDK (hosted on Github)**:<br/>
Use the buildWithPrecompiledSDK configuration to use the precompiled libraries (Product->Scheme->Edit Scheme).
Please note that the first time you'll build with the precompiled SDK, it will download the precompiled libraries from Github, this might take a while.

**Use your own compiled SDK**:<br/>
You can build this sample with Alchemy. In your `<SDK>` execute this command:

`./build.sh -p arsdk-ios -t build-sample -j` for iOS
`./build.sh -p arsdk-ios_sim -t build-sample -j` for iOS simulator

If you prefer to build directly from XCode, use the buildWithLocalSDK configuration to use your localy compiled libraries (see [go deeper](#go-deeper) to first compile your own SDK). 

**Please note that there are two targets in the iOS sample: SDKSample and SDKSampleForSkyController2. The first one is using *-lardiscoverywithouteacc* in its Other Linker Flags list and does not include the ExternalAccessory framework. However SDKSampleForSkyController2 uses *-lardiscovery* and includes ExternalAccessory framework.**


### Android

**Use the precompiled SDK (hosted on JCenter)**:<br/>
With Android Studio, open the settings.gradle located in `SDKSample/buildWithPrecompiledSDK`. 

**Use your own compiled SDK**:<br/>
You can build this sample with Alchemy. In your `<SDK>` execute this command:

`./build.sh -p arsdk-android -t build-sample`

Otherwise, if you want to use Android Studio build, first execute this command in `<SDK>`:
`./build.sh -p arsdk-android -t build-jni`

Then, in Android Studio, open the settings.gradle located in `SDKSample/buildWithLocalSDK`.
