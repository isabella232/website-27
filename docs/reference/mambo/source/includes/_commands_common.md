<!-- common-Settings-AllSettings-->
### <a name="common-Settings-AllSettings">Ask for all settings</a><br/>
> Ask for all settings:

```c
deviceController->common->sendSettingsAllSettings(deviceController->common);
```

```objective_c
deviceController->common->sendSettingsAllSettings(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendSettingsAllSettings();
```

Ask for all settings.<br/>
<br/>
**Please note that you should not send this command if you are using the<br/>
libARController API as this library is handling the connection process for you.**<br/>




Result:<br/>
The product will trigger all settings events (such as [CameraSettings](#common-CameraSettingsState-CameraSettingsChanged), or product specific settings as the [MaxAltitude](#ARDrone3-PilotingSettingsState-MaxAltitudeChanged) for the Bebop).<br/>
Then, it will trigger [AllSettingsEnd](#common-SettingsState-AllSettingsChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Settings-Reset-->
### <a name="common-Settings-Reset">Reset all settings</a><br/>
> Reset all settings:

```c
deviceController->common->sendSettingsReset(deviceController->common);
```

```objective_c
deviceController->common->sendSettingsReset(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendSettingsReset();
```

Reset all settings.<br/>




Result:<br/>
It will trigger [ResetChanged](#common-SettingsState-ResetChanged).<br/>
Then, the product will trigger all settings events (such as [CameraSettings](#common-CameraSettingsState-CameraSettingsChanged), or product specific settings as the [MaxAltitude](#ARDrone3-PilotingSettingsState-MaxAltitudeChanged) for the Bebop) with factory values.<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Settings-ProductName-->
### <a name="common-Settings-ProductName">Set product name</a><br/>
> Set product name:

```c
deviceController->common->sendSettingsProductName(deviceController->common, (char *)name);
```

```objective_c
deviceController->common->sendSettingsProductName(deviceController->common, (char *)name);
```

```java
deviceController.getFeatureCommon().sendSettingsProductName((String)name);
```

Set the product name.<br/>
It also sets the name of the SSID for Wifi products and advertisement name for BLE products (changed after a reboot of the product).<br/>


* name (string): Product name<br/>


Result:<br/>
Name is changed.<br/>
Then, it will trigger [NameChanged](#common-SettingsState-ProductNameChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Common-AllStates-->
### <a name="common-Common-AllStates">Ask for all states</a><br/>
> Ask for all states:

```c
deviceController->common->sendCommonAllStates(deviceController->common);
```

```objective_c
deviceController->common->sendCommonAllStates(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendCommonAllStates();
```

Ask for all states.<br/>
<br/>
**Please note that you should not send this command if you are using the<br/>
libARController API as this library is handling the connection process for you.**<br/>




Result:<br/>
The product will trigger all states events (such as [FlyingState](#ARDrone3-PilotingState-FlyingStateChanged) for the Bebop).<br/>
Then, it will trigger [AllStatesEnd](#common-CommonState-AllStatesChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Common-CurrentDate-->
### <a name="common-Common-CurrentDate">Set the date</a><br/>
> Set the date:

```c
deviceController->common->sendCommonCurrentDate(deviceController->common, (char *)date);
```

```objective_c
deviceController->common->sendCommonCurrentDate(deviceController->common, (char *)date);
```

```java
deviceController.getFeatureCommon().sendCommonCurrentDate((String)date);
```

Set the date.<br/>
This date is taken by the drone as its own date.<br/>
So medias and other files will be dated from this date<br/>
<br/>
**Please note that you should not send this command if you are using the<br/>
libARController API as this library is handling the connection process for you.**<br/>


* date (string): Date with ISO-8601 format<br/>


Result:<br/>
The date of the product is set.<br/>
Then, it will trigger [DateChanged](#common-CommonState-CurrentDateChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Common-CurrentTime-->
### <a name="common-Common-CurrentTime">Set the time</a><br/>
> Set the time:

```c
deviceController->common->sendCommonCurrentTime(deviceController->common, (char *)time);
```

```objective_c
deviceController->common->sendCommonCurrentTime(deviceController->common, (char *)time);
```

```java
deviceController.getFeatureCommon().sendCommonCurrentTime((String)time);
```

Set the time.<br/>
This time is taken by the drone as its own time.<br/>
So medias and other files will be dated from this time<br/>
<br/>
**Please note that you should not send this command if you are using the<br/>
libARController API as this library is handling the connection process for you.**<br/>


* time (string): Time with ISO-8601 format<br/>


Result:<br/>
The time of the product is set.<br/>
Then, it will trigger [TimeChanged](#common-CommonState-CurrentTimeChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Common-Reboot-->
### <a name="common-Common-Reboot">Reboot</a><br/>
> Reboot:

```c
deviceController->common->sendCommonReboot(deviceController->common);
```

```objective_c
deviceController->common->sendCommonReboot(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendCommonReboot();
```

Reboot the product.<br/>
The product will accept this command only if is not flying.<br/>




Result:<br/>
The product will reboot if it can.<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Controller-isPiloting-->
### <a name="common-Controller-isPiloting">Inform about hud entering</a><br/>
> Inform about hud entering:

```c
deviceController->common->sendControllerIsPiloting(deviceController->common, (uint8_t)piloting);
```

```objective_c
deviceController->common->sendControllerIsPiloting(deviceController->common, (uint8_t)piloting);
```

```java
deviceController.getFeatureCommon().sendControllerIsPiloting((byte)piloting);
```

Inform about hud entering.<br/>
Tell the drone that the controller enters/leaves the piloting hud.<br/>
On a non-flying products it is used to know when a run begins.<br/>


* piloting (u8): 0 when the application is not in the piloting HUD, 1 when it enters the HUD.<br/>


Result:<br/>
If yes, the product will begin a new session (so it should send a new [runId](#common-RunState-RunIdChanged)).<br/>
Also, on the JumpingSumos, if the video is in autorecord mode, it will start recording.<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

