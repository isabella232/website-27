<!-- SkyController-Settings-AllSettings-->
### <a name="SkyController-Settings-AllSettings">Ask for all controller's settings</a><br/>
> Ask for all controller's settings:

```c
deviceController->skyController->sendSettingsAllSettings(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendSettingsAllSettings(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendSettingsAllSettings();
```

Request the controller to send all its settings.<br/>




Result:<br/>
The controller will trigger all settings events and will finally trigger [AllSettingsChanged](#SkyController-SettingsState-AllSettingsChanged).<br/>


*Supported by <br/>*

- *SkyController*<br/>
- *SkyController 2*<br/>


<br/>

<!-- SkyController-Common-AllStates-->
### <a name="SkyController-Common-AllStates">Ask for all controller's states.</a><br/>
> Ask for all controller's states.:

```c
deviceController->skyController->sendCommonAllStates(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendCommonAllStates(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendCommonAllStates();
```

Request the controller to send all its states.<br/>




Result:<br/>
The controller will trigger all states events and will finally trigger [AllStatesChanged](#SkyController-CommonState-AllStatesChanged).<br/>


*Supported by <br/>*

- *SkyController*<br/>
- *SkyController 2*<br/>


<br/>

<!-- SkyController-CoPiloting-setPilotingSource-->
### <a name="SkyController-CoPiloting-setPilotingSource">Set piloting source</a><br/>
> Set piloting source:

```c
deviceController->skyController->sendCoPilotingSetPilotingSource(deviceController->skyController, (eARCOMMANDS_SKYCONTROLLER_COPILOTING_SETPILOTINGSOURCE_SOURCE)source);
```

```objective_c
deviceController->skyController->sendCoPilotingSetPilotingSource(deviceController->skyController, (eARCOMMANDS_SKYCONTROLLER_COPILOTING_SETPILOTINGSOURCE_SOURCE)source);
```

```java
deviceController.getFeatureSkyController().sendCoPilotingSetPilotingSource((ARCOMMANDS_SKYCONTROLLER_COPILOTING_SETPILOTINGSOURCE_SOURCE_ENUM)source);
```

Change who is piloting the drone.<br/>
By default, the SkyController is the source of piloting commands, and any connected application (i.e. FreeFlight) can not send [piloting commands](#ARDrone3-Piloting-PCMD) commands directly to the drone. When the piloting source is set to Controller, the SkyController will forward the controller commands to the drone, and won't send any commands itself.<br/>
The piloting source is automatically reset to SkyController when the controller is disconnected.<br/>


* source (enum): The new piloting source<br/>
   * SkyController: Use the SkyController joysticks<br/>
   * Controller: Use the Tablet (or smartphone, or whatever) controls<br/>
Disables the SkyController joysticks<br/>


Result:<br/>
The SkyController will sent a [pilotingSource](#SkyController-CoPilotingState-pilotingSource) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>
- *SkyController 2*<br/>


<br/>

<!-- SkyController-Calibration-enableMagnetoCalibrationQualityUpdates-->
### <a name="SkyController-Calibration-enableMagnetoCalibrationQualityUpdates">Enable Magneto calibration quality updates</a><br/>
> Enable Magneto calibration quality updates:

```c
deviceController->skyController->sendCalibrationEnableMagnetoCalibrationQualityUpdates(deviceController->skyController, (uint8_t)enable);
```

```objective_c
deviceController->skyController->sendCalibrationEnableMagnetoCalibrationQualityUpdates(deviceController->skyController, (uint8_t)enable);
```

```java
deviceController.getFeatureSkyController().sendCalibrationEnableMagnetoCalibrationQualityUpdates((byte)enable);
```

Asks the SkyController to send (or not) the magneto calibration quality updates.<br/>
The [MagnetoCalibrationState](#SkyController-CalibrationState-MagnetoCalibrationState) event will always be sent when the status parameters changes, regardless of this setting.<br/>


* enable (u8): Flag to enable the feature:<br/>
1 = Enable quality updates<br/>
0 = Disable quality updates<br/>


Result:<br/>
The SkyController will send a [MagnetoCalibrationQualityUpdatesState](#SkyController-CalibrationState-MagnetoCalibrationQualityUpdatesState) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>
- *SkyController 2*<br/>


<br/>

<!-- SkyController-Factory-Reset-->
### <a name="SkyController-Factory-Reset">Reset the SkyController 2 to its factory settings</a><br/>
> Reset the SkyController 2 to its factory settings:

```c
deviceController->skyController->sendFactoryReset(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendFactoryReset(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendFactoryReset();
```

This command will request a factory reset from the SkyController 2. *The factory reset procedure implies an automatic reboot*, which will be done immediately after recieving this command.<br/>




Result:<br/>
The SkyController 2 will reboot, all settings will be reset to their default values. Products that were paired in factory will **NOT** lose this pairing.<br/>


*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

