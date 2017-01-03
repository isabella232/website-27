# RTP H.264 streaming

In addition to the traditional [sensor_msgs/Image](http://docs.ros.org/indigo/api/sensor_msgs/html/msg/Image.html)
message to transmit camera frames,
the Parrot S.L.A.M.dunk offers 2 RTP H.264 streams, one for each camera.
Internally, this is implemented by a [Gstreamer](https://gstreamer.freedesktop.org/) pipeline.

On the client side, e.g. for rviz integration,
it's possible to use a [gscam](https://github.com/Parrot-Developers/gscam) fork
to get the frames as ROS messages.

It is also possible to directly access the video with a media player
such as [mplayer](http://www.mplayerhq.hu)
or [vlc](http://www.videolan.org/vlc/index.html).

Start streaming service,
using dynamic_reconfigure (c.f. [Dynamic reconfiguration](#dynamic-reconfiguration)):

    rosrun dynamic_reconfigure dynparam set /slamdunk_node service_trigger_streaming always

Create [SDP](https://en.wikipedia.org/wiki/Session_Description_Protocol) file for both cameras:

    cat <<'EOF' > cam0.sdp
    v=0
    m=video 5000 RTP/AVP 96
    c=IN IP4 192.168.45.1
    a=rtpmap:96 H264/90000
    EOF
    cat <<'EOF' > cam1.sdp
    v=0
    m=video 5100 RTP/AVP 96
    c=IN IP4 192.168.45.1
    a=rtpmap:96 H264/90000
    EOF

Visualize left camera with `mplayer`:

    mplayer cam0.sdp

Visualize right camera with `vlc`:

    vlc --network-caching=250 cam1.sdp

Finally, to reset the streaming service to its default state:

    rosrun dynamic_reconfigure dynparam set /slamdunk_node service_trigger_streaming ondemand
