<!-- thermal_cam-activate-->
### <a name="thermal_cam-activate">Activate a thermal camera</a><br/>
> Activate a thermal camera:

```c
deviceController->thermal_cam->sendActivate(deviceController->thermal_cam, (uint8_t)cam_id);
```

```objective_c
deviceController->thermal_cam->sendActivate(deviceController->thermal_cam, (uint8_t)cam_id);
```

```java
deviceController.getFeatureThermalCam().sendActivate((byte)cam_id);
```

Activate a given thermal camera.<br/>
Activating a camera may deactivate others on some drones.<br/>


* cam_id (u8): Thermal camera id, as given in the [connected accessories](#1-33-0) event.<br/>


Result:<br/>
Camera is activated and [CameraState](#thermal_cam-camera_state) is changed to activated.<br/>


*Supported by <br/>*

- *no product*<br/>


<br/>

<!-- thermal_cam-deactivate-->
### <a name="thermal_cam-deactivate">Deactivate a thermal camera</a><br/>
> Deactivate a thermal camera:

```c
deviceController->thermal_cam->sendDeactivate(deviceController->thermal_cam, (uint8_t)cam_id);
```

```objective_c
deviceController->thermal_cam->sendDeactivate(deviceController->thermal_cam, (uint8_t)cam_id);
```

```java
deviceController.getFeatureThermalCam().sendDeactivate((byte)cam_id);
```

Deactivate a given thermal camera.<br/>


* cam_id (u8): Thermal camera id, as given in the [connected accessories](#1-33-0) event.<br/>


Result:<br/>
Camera is deactivated and [CameraState](#thermal_cam-camera_state) is changed to deactivated.<br/>


*Supported by <br/>*

- *no product*<br/>


<br/>

<!-- thermal_cam-set_sensitivity-->
### <a name="thermal_cam-set_sensitivity">Set the thermal cam sensitivity</a><br/>
> Set the thermal cam sensitivity:

```c
deviceController->thermal_cam->sendSetSensitivity(deviceController->thermal_cam, (uint8_t)cam_id, (eARCOMMANDS_THERMAL_CAM_RANGE)range);
```

```objective_c
deviceController->thermal_cam->sendSetSensitivity(deviceController->thermal_cam, (uint8_t)cam_id, (eARCOMMANDS_THERMAL_CAM_RANGE)range);
```

```java
deviceController.getFeatureThermalCam().sendSetSensitivity((byte)cam_id, (ARCOMMANDS_THERMAL_CAM_RANGE_ENUM)range);
```

Set the thermal camera sensitivity range.<br/>


* cam_id (u8): Thermal camera id, as given in the [connected accessories](#1-33-0) event.<br/>
* range (enum): Thermal range<br/>
   * high: High range (from 0 to 400°C)<br/>
   * low: Low range (from 0 to 120°C)<br/>


Result:<br/>
Sensitivity range of the camera is changed, and event [Sensitivity](#thermal_cam-sensitivity) is sent accordingly.<br/>


*Supported by <br/>*

- *no product*<br/>


<br/>

