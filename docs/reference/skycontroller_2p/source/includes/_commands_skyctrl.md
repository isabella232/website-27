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
- *SkyController 2P*<br/>


<br/>

<!-- SkyController-Settings-Reset-->
### <a name="SkyController-Settings-Reset">Reset all settings</a><br/>
> Reset all settings:

```c
deviceController->skyController->sendSettingsReset(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendSettingsReset(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendSettingsReset();
```

Reset all settings (i.e. everything except drone pairing).<br/>




Result:<br/>
All settings are reset.<br/>


*Supported by <br/>*

- *SkyController 2 since 1.0.5*<br/>
- *SkyController 2P*<br/>


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
- *SkyController 2P*<br/>


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
- *SkyController 2P*<br/>


<br/>

<!-- SkyController-Calibration-StartCalibration-->
### <a name="SkyController-Calibration-StartCalibration">Start magneto calibration</a><br/>
> Start magneto calibration:

```c
deviceController->skyController->sendCalibrationStartCalibration(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendCalibrationStartCalibration(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendCalibrationStartCalibration();
```

Asks the SkyController to start a magneto calibration.<br/>
If the calibration is already started, this command has no effect.<br/>




Result:<br/>
The SkyController will send a [MagnetoCalibrationStateV2](#SkyController-CalibrationState-MagnetoCalibrationStateV2) event.<br/>


*Supported by <br/>*

- *SkyController 2P*<br/>


<br/>

<!-- SkyController-Calibration-AbortCalibration-->
### <a name="SkyController-Calibration-AbortCalibration">Abort a running magneto calibration</a><br/>
> Abort a running magneto calibration:

```c
deviceController->skyController->sendCalibrationAbortCalibration(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendCalibrationAbortCalibration(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendCalibrationAbortCalibration();
```

Asks the SkyController to abort an in-progress magneto calibration.<br/>
If no calibration is in progress, this command has no effect.<br/>




Result:<br/>
The SkyController will send a [MagnetoCalibrationStateV2](#SkyController-CalibrationState-MagnetoCalibrationStateV2) event.<br/>


*Supported by <br/>*

- *SkyController 2P*<br/>


<br/>

<!-- SkyController-Factory-Reset-->
### <a name="SkyController-Factory-Reset">Reset the SkyController to its factory settings</a><br/>
> Reset the SkyController to its factory settings:

```c
deviceController->skyController->sendFactoryReset(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendFactoryReset(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendFactoryReset();
```

This command will request a factory reset from the SkyController. *The factory reset procedure implies an automatic reboot*, which will be done immediately after recieving this command.<br/>




Result:<br/>
The SkyController will reboot, all settings will be reset to their default values.<br/>
SkyController 2 that were paired in factory will **NOT** lose this pairing.<br/>
SkyController 1 will lose **ALL** pairing, including factory ones.<br/>


*Supported by <br/>*

- *SkyController 2*<br/>
- *SkyController 2P*<br/>


<br/>

