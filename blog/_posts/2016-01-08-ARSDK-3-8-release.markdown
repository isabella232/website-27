---
layout: post
title:  "ARSDK, what's new in the 3.8 release ?"
date:   2016-01-08 10:00:00
categories: sdk drones repo alchemy stream2 jcenter
longtitle: "ARSDK, what's new in the 3.8 release? TL;DR: a lot !"
author: Djavan Bertrand
description: Explanation of all the changes brought by the 3.8 release of the ARSDK
---
A new version of the Parrot drone SDK has recently been released. This SDK lets you control all Parrot's new drones (Bebop 2, Bebop, JumpingSumo and evos, Rolling Spider, Airbornes) from a remote station (could be an Android or iOS phone or even a Linux based controller).<br/>
This new release brings lots of new cool improvements. We will explain all of them in detail. <br/>
The majority of these changes have been made because we are trying to use more and more public, tried and tested tools.

#Repo
Repo is a repository management tool built on top of Git by the Android team. It uses Git to manage many Git repositories.<br/>
Download the Repo tool by following [these instructions][repo_download].<br/>
Then you can learn how to use it [here][repo_use].
The manifests needed by repo to locate all the SDK modules are available on [Github][github_manifests]. This repository contains two manifest files: 

-  *release.xml* lists the SHA1s of all modules corresponding of the latest release: **stable releases**
- *default.xml* doesn't mention any SHA1, so it will get the upstream of all modules: **unstable** but up to date.

To download the SDK sources, you'll need to type in a terminal (after having installed Repo):

- Download the SDK using *default.xml*:

{% highlight c %}
repo init -u https://github.com/Parrot-Developers/arsdk_manifests.git
{% endhighlight %}

- Download the latest release of the SDK (use *release.xml*):

{% highlight c %}
repo init -u https://github.com/Parrot-Developers/arsdk_manifests.git -m release.xml
{% endhighlight %}

Then you'll be able to type the following command in order to get all SDK sources:

{% highlight c %}
repo sync
{% endhighlight %}


#Alchemy
Alchemy is a build system inspired by the one used in Android. A central makefile instance scans a workspace to find user makefiles, includes them and
register modules to be built. Modules are described by a set of variables (`LOCAL_XXX`) specifying source files, custom compilation flags, include directories and some other more advanced stuff.

Modules can be libraries (static and shared), executable, prebuilt binaries of components built by another build system (like autotools suite for many linux packages). Build of external modules is similar to what is done in buildroot.

Alchemy is hence a mix of what can be done in Android (building source files without having to write complicated makefile/autoconf.ac) and buildroot (building open-source components having there own makefile/configure/cmake)

Alchemy supports:

* building static/shared libraries and executables from source code.
* building autotools/cmake from archives or source tree.
* building qmake applications.
* building for Linux/iOS/MacOS/Android/mingw32 targets.
* building on Linux/MacOS hosts.

Here is the [complete documentation][alchemy_documentation] about alchemy.

Alchemy uses gnu make and shell/python scripts to do the job. The configuration tool is kconfig (as on linux/buildroot/busybox) and prebuilt binaries are provided on linux/macos hosts.

A first working example is how kconfig binaries are built (see kconfig subdir and its atom.mk/build.sh).

Alchemy is also open sourced, you can find it on our [Github][alchemy].<br/>
When downloading the sources of the SDK, a *build.sh* symlink will be created in the root folder. This script will call the *alchemake* script in the Alchemy folder (<SDK>/build/alchemy) in order to build the whole project.<br/>
Once the libraries have been built, you can find them in <SDK>/out/.

The build is done by the *./build.sh* script. You can run *./build.sh --help* to know more about the building options.<br/>
The general way to build is:<br/>
{% highlight c %}
./build.sh -p PRODUCT-VARIANT -t TASK OTHER_ARGS
{% endhighlight %}

*OTHER_ARGS* will be passed to the compiler.

Products available are:

- iOS
- Android
- Unix

<br/>Here are, for each products, the different variants and task we support:

###Unix
Variants available are:

- base

<br/>Tasks available are:

- build-sdk

<br/>The command to build the SDK for Unix platform is:<br/>
{% highlight c %}
./build.sh -p Unix-forall -t build-sdk
{% endhighlight %}

Please note that if you want to compile for Unix, you might want to use the *final* keyword at the end of the instruction to have stripped libraries. They will be generated in the SDK/out/final folder.
{% highlight c %}
./build.sh -p Unix-forall -t build-sdk all final
{% endhighlight %}

###iOS
Variants available are:

- forall (build all variants)
- iphoneos
- iphonesimulator

<br/>Tasks available are:

- build-sdk (only build libraries)
- build-sample (build-sdk + execute xcodebuild in all samples)

<br/>The command to build the SDK for all iOS variants is:<br/>
{% highlight c %}
./build.sh -p iOS-forall -t build-sdk
{% endhighlight %}

###Android
Variants available are:

- forall (build all variants)
- armeabi
- armeabi_v7a
- mips
- x86

<br/>Tasks available are:

- build-sdk (only build libraries)
- build-jni (build-sdk + execute ndk-build in all samples)
- build-sample (build-jni + execute gradlew assembledebug in all samples)

<br/>The command to build the SDK for all Android variants is:<br/>
{% highlight c %}
./build.sh -p Android-forall -t build-sdk
{% endhighlight%}

<br/><br/>
Now that you have built for all products, here is how you SDK workspace should look like:

{% highlight c %}

+-SDK/
  |
  +-build/                      Build tools directory
  |    |
  |    +-alchemy/               Alchemy build system
  |
  +-build.sh                    Build script that can invoke everything (symlink)
  |
  +-out/                        Output folder containing the built packages
  |    |
  |    +-<PRODUCT>-<VARIANT>/
  |        |
  |        +-build/             Where packages are built
  |        |
  |        +-build-host/        Where packages for host are built
  |        |
  |        +-staging/           Where not stripped packages deliveries are installed
  |
  +-packages/
  |    |
  |    +-ARSDKBuildUtils/       Tools to create the autotools needed to build the SDK
  |    |
  |    +-ARSDKTools/            External libs used by the SDK
  |    |
  |    +-Docs/                  SDK doxygen
  |    |
  |    +-libARCommands/         Commands/Events you can send/receive to/from the drone
  |    |
  |    +-libARController/       Abstraction level to connect to the drone
  |    |
  |    +-libARDataTransfer/     Transfer data from or to the drone
  |    |
  |    +-libARDiscovery/        Discover from the network all supported drones
  |    |
  |    +-libARMavlink/          Generate an automated flight file
  |    |
  |    +-libARMedia/            Abstraction layer around the medias
  |    |
  |    +-libARNetwork/          Send and receive packets to/from the drone
  |    |
  |    +-libARNetworkAL/        Abstraction layer around the different networks
  |    | 
  |    +-libARSAL/              System abstraction layer
  |    |
  |    +-libARStream/           Pack/unpack streams
  |    |
  |    +-libARStream2/          Pack/unpack streams and deals with rtp streams
  |    |
  |    +-libARUpdater/          Help to update your drone
  |    |
  |    +-libARUtils/            Provide utilities classes
  |    |
  |    +-Samples/               Basic examples to test the SDK
  |
  |-products/                   Folder containing all available products
       | 
       +-common/
       | 
       +-<PRODUCT>/             Product specific config
           |  
           +-<VARIANT>/         Variant specific config

{% endhighlight %}

#Stream v2
One big improvement of this 3.8 release is the support the new video streaming used by the Bebop 2 which we call stream v2.<br/> 
Stream v2 improves a lot the quality of the video stream. As we said in introduction, we are trying to use more and more common tools and common protocols. Stream v2 is based on an H.264 video encoding streamed over the [RTP protocol][RTP] which means we are now compatible with common players supporting RTP such as VLC or mplayer. An article on how to start the video stream and use an external player will follow.<br/> 
The H.264 encoding now uses more advanced techniques: to have better error resilience the video frames are cut into multiple slices, so that if a slice is not received by the controller, we don't loose the entire frame but just part of it. Also instead of using a classic IPPPP[...] frame type pattern we use periodic intra refresh, which means we do not have I-frames in the stream any more, but instead we have I-slices spread across space and time to refresh the stream while maintaining almost constant frame sizes and avoid peaks in the bandwidth.<br/> 
**All these improvements make the stream smoother with less latency and less frames lost.** 

To be able to support this new stream, we had to **slightly** break the compatibility. That means that if you are updating your SDK from the version 3.7.5 to the 3.8, your code won't compile. You'll have to add some code, we'll give you hints [right after](#stream_code), but first, let's talk about the changes.

When you add yourself as a listener for the video stream, you will have to implement 3 callbacks:

- *configure decoder*: this callback will be called when you will need to configure your decoder. In parameter, you will find the codec information (see [codec information](#codec_information)). 
- *frame received*: this callback is called each time a frame is available to decode. This callback existed before but we added a return parameter, which indicates if an error occured during the decoding.
- *frame timed out*: this callback is called when receiving a frame has timed out. This callback will only be called if the stream type is v1.

Please note that if you're using a decoder that needs the stream to be MP4 compliant - that means that each video NAL units separator (0001) should be replaced with the length of the NALU - you will need to call the method *setMP4Compliant*. **This is needed for the iOS hardware decoder.**

<a name="codec_information">**Codec information**</a>:<br/>
The codec information indicate the type of codec and additional information about it.<br/>
The possible codec types are:

- H264
- MJPEG

And additional information are, for the moment, only for the H264. They contains:

- the SPS and its size
- the PPS and its size
- If the stream will be MP4 compliant

We will now list all the changes you'll have to do in your code to be able to receive the stream V2 and to compile your code.

<a name="stream_code"></a>
###Android
You can inspire you from the Samples we provide. Here is [one for the Bebop/Bebop2][Sample_Android_Bebop].

You will first need to implement *configureDecoder*. In this function you'll have to configure your decoder according to the codec and its additional information.

The *onFrameReceived* function has changed its return type. It was before a void, now it returns a *```ARCONTROLLER_ERROR_ENUM```*. In this function, you can decode and display the frame received.

Then, implement the function *onFrameTimeout*, handle the fact that the retrieval of a frame did time out.

###iOS and Unix
You can inspire you from the Samples we provide. There is [one for the Bebop/Bebop2 using the hardware decoder on iOS][Sample_iOS_Bebop], another [for the Bebop/Bebop2 on Unix][Sample_Unix_Bebop], and [one for the JumpingSumo on Unix][Sample_Unix_Jumping]. 

If you're using a decoder which is expecting a MP4 compliant stream, as the iOS hardware decoder is, you will have to add that line of code:<br/>
{% highlight c %}
error = ARCONTROLLER_Device_SetVideoStreamMP4Compliant(_deviceController, 1);
{% endhighlight %}

You will then need to change your *```ARCONTROLLER_Device_SetVideoReceiveCallback```* by *```ARCONTROLLER_Device_SetVideoStreamCallbacks```* and give to that function the three callbacks.

Then, in the *```configureDecoderCallback```*, configure your decoder according to the codec and its additionnal informations.

In the *```receiveFrameCallback```* you can decode and display the frame received.

In *```timeoutFrameCallback```*, handle the fact that the retrieval of a frame did time out.

#JCenter
Keeping the same target of using well-known tools and services, we've made the usage of the ARSDK Android libraries easier. <br/>
Indeed, you can now use the latest SDK release in your own projects by simply adding few lines in it!

In your module *build.gradle* file, add the following line in the dependencies list:<br/>
{% highlight java %}
compile 'com.parrot:arsdk:3.8'
{% endhighlight %}

Then, load the native ARSDK libraries by typing this code:<br/>
{% highlight java %}
ARSDK.loadSDKLibs();
{% endhighlight %}

We suggest you to put this code in a static block in the first activity that uses the ARSDK.

<br/><br/><br/>

That's it for this release. Don't forget to read our [documentation][documentation] and if you have any questions, feel free to ask them on our [forum][forum] (if other devs haven't already asked/answered them).

Happy coding !


[repo_download]: http://source.android.com/source/downloading.html#installing-repo
[repo_use]: https://source.android.com/source/using-repo.html
[github_manifests]: https://github.com/Parrot-Developers/arsdk_manifests
[alchemy]: https://github.com/Parrot-Developers/alchemy
[RTP]: https://en.wikipedia.org/wiki/Real-time_Transport_Protocol
[Sample_iOS_Bebop]: https://github.com/Parrot-Developers/Samples/tree/master/iOS/BebopPilotingNewAPI
[Sample_Unix_Bebop]: https://github.com/Parrot-Developers/Samples/tree/master/Unix/BebopPilotingNewAPI
[Sample_Unix_Jumping]: https://github.com/Parrot-Developers/Samples/tree/master/Unix/JSPilotingNewAPI
[Sample_Android_Bebop]: https://github.com/Parrot-Developers/Samples/tree/master/Android/BebopDronePilotingNewAPI
[documentation]: http://developer.parrot.com/docs/bebop/
[forum]: http://forum.developer.parrot.com/
[alchemy_documentation]: https://github.com/Parrot-Developers/alchemy/blob/master/doc/alchemy.mkd