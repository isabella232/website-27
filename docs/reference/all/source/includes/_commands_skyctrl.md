<!-- SkyController-Wifi-RequestWifiList-->
### <a name="SkyController-Wifi-RequestWifiList">Request visible wifi list</a><br/>
> Request visible wifi list:

```c
deviceController->skyController->sendWifiRequestWifiList(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendWifiRequestWifiList(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendWifiRequestWifiList();
```

After recieving this command, the SkyController will do a network scan to get the wifi list.<br/>
Communication with the drone is stopped during the network scan, so the controller should avoid sending this command during flight.<br/>
The controller should clear the local wifi list before sending this command.<br/>




Result:<br/>
Event [WifiList](#SkyController-WifiState-WifiList) is triggered for each visible wifi networks.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-Wifi-RequestCurrentWifi-->
### <a name="SkyController-Wifi-RequestCurrentWifi">Request current wifi informations</a><br/>
> Request current wifi informations:

```c
deviceController->skyController->sendWifiRequestCurrentWifi(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendWifiRequestCurrentWifi(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendWifiRequestCurrentWifi();
```

This is a synchronization command. The SkyController will automatically send its current wifi info when any data changes, so this command should only be used when connecting, in order to get an initial state.<br/>




Result:<br/>
Event [wifi ConnectionChanged](#SkyController-WifiState-ConnexionChanged) is triggered.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-Wifi-ConnectToWifi-->
### <a name="SkyController-Wifi-ConnectToWifi">Connect the SkyController to a wifi network</a><br/>
> Connect the SkyController to a wifi network:

```c
deviceController->skyController->sendWifiConnectToWifi(deviceController->skyController, (char *)bssid, (char *)ssid, (char *)passphrase);
```

```objective_c
deviceController->skyController->sendWifiConnectToWifi(deviceController->skyController, (char *)bssid, (char *)ssid, (char *)passphrase);
```

```java
deviceController.getFeatureSkyController().sendWifiConnectToWifi((String)bssid, (String)ssid, (String)passphrase);
```

The network should be a visible network retrieved from the [WifiList](#SkyController-WifiState-WifiList) event.<br/>
If the network is secured, then the passphrase must be set. For non-secure network, the passphrase argument is ignored.<br/>


* bssid (string): Wifi bssid<br/>
* ssid (string): Wifi ssid<br/>
* passphrase (string): Wifi passphrase<br/>


Result:<br/>
The SkyController should connect to the network.<br/>
A [wifi ConnectionChanged](#SkyController-WifiState-ConnexionChanged) event is triggered.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-Wifi-ForgetWifi-->
### <a name="SkyController-Wifi-ForgetWifi">Forget a wifi network</a><br/>
> Forget a wifi network:

```c
deviceController->skyController->sendWifiForgetWifi(deviceController->skyController, (char *)ssid);
```

```objective_c
deviceController->skyController->sendWifiForgetWifi(deviceController->skyController, (char *)ssid);
```

```java
deviceController.getFeatureSkyController().sendWifiForgetWifi((String)ssid);
```

Removes the network from the saved network list.<br/>
If the network is the current network, then the SkyController will be disconnected first.<br/>


* ssid (string): Wifi ssid<br/>


Result:<br/>
The next [WifiList](#SkyController-WifiState-WifiList) event will report this network as not saved.<br/>
If the SkyController is connected to this network, a [wifi ConnectionChanged](#SkyController-WifiState-ConnexionChanged) event is triggered<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-Wifi-WifiAuthChannel-->
### <a name="SkyController-Wifi-WifiAuthChannel">Request the list of authorized channels</a><br/>
> Request the list of authorized channels:

```c
deviceController->skyController->sendWifiWifiAuthChannel(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendWifiWifiAuthChannel(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendWifiWifiAuthChannel();
```

Requests the list of authorized wifi channels for the current country/regulatory domain.<br/>
These channels are valid for the [AccessPointChannel](#SkyController-AccessPointSettings-AccessPointChannel) command.<br/>




Result:<br/>
A list of [WifiAuthChannelListChanged](#SkyController-WifiState-WifiAuthChannelListChanged) events will be sent, followed by an [AllWifiAuthChannelChanged](#SkyController-WifiState-AllWifiAuthChannelChanged) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-Device-RequestDeviceList-->
### <a name="SkyController-Device-RequestDeviceList">Request the list of visible devices (deprecated)</a><br/>
> Request the list of visible devices (deprecated):

```c
deviceController->skyController->sendDeviceRequestDeviceList(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendDeviceRequestDeviceList(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendDeviceRequestDeviceList();
```

*This message is deprecated.*<br/>

This command is deprecated (The SkyController can only see one device at a time, so a device list is not required), and should not be used.<br/>




Result:<br/>
This command is not implemented.<br/>


*Supported by <br/>*

- *no product*<br/>


<br/>

<!-- SkyController-Device-RequestCurrentDevice-->
### <a name="SkyController-Device-RequestCurrentDevice">Request current device informations (deprecated)</a><br/>
> Request current device informations (deprecated):

```c
deviceController->skyController->sendDeviceRequestCurrentDevice(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendDeviceRequestCurrentDevice(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendDeviceRequestCurrentDevice();
```

*This message is deprecated.*<br/>

This command is deprecated and should not be used.<br/>




Result:<br/>
This command is not implemented<br/>


*Supported by <br/>*

- *no product*<br/>


<br/>

<!-- SkyController-Device-ConnectToDevice-->
### <a name="SkyController-Device-ConnectToDevice">Connect the SkyController to a given device (deprecated)</a><br/>
> Connect the SkyController to a given device (deprecated):

```c
deviceController->skyController->sendDeviceConnectToDevice(deviceController->skyController, (char *)deviceName);
```

```objective_c
deviceController->skyController->sendDeviceConnectToDevice(deviceController->skyController, (char *)deviceName);
```

```java
deviceController.getFeatureSkyController().sendDeviceConnectToDevice((String)deviceName);
```

*This message is deprecated.*<br/>

This command is deprecated and should not be used.<br/>
The SkyController will automatically connect to the first visible device on the current wifi network.<br/>


* deviceName (string): Device name<br/>


Result:<br/>
This command is not implemented.<br/>


*Supported by <br/>*

- *no product*<br/>


<br/>

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

<!-- SkyController-AccessPointSettings-AccessPointSSID-->
### <a name="SkyController-AccessPointSettings-AccessPointSSID">Set access point SSID</a><br/>
> Set access point SSID:

```c
deviceController->skyController->sendAccessPointSettingsAccessPointSSID(deviceController->skyController, (char *)ssid);
```

```objective_c
deviceController->skyController->sendAccessPointSettingsAccessPointSSID(deviceController->skyController, (char *)ssid);
```

```java
deviceController.getFeatureSkyController().sendAccessPointSettingsAccessPointSSID((String)ssid);
```

Set the SkyController access point SSID.<br/>
The name will be checked, and can be modified before application. Use the [AccessPointSSIDChanged](#SkyController-AccessPointSettingsState-AccessPointSSIDChanged) event to get the applied network name.<br/>


* ssid (string): AccessPoint SSID<br/>


Result:<br/>
The network name will change (which will likely disconnect the controller), then an [AccessPointSSIDChanged](#SkyController-AccessPointSettingsState-AccessPointSSIDChanged) event will be sent<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AccessPointSettings-AccessPointChannel-->
### <a name="SkyController-AccessPointSettings-AccessPointChannel">Set access point channel (deprecated)</a><br/>
> Set access point channel (deprecated):

```c
deviceController->skyController->sendAccessPointSettingsAccessPointChannel(deviceController->skyController, (uint8_t)channel);
```

```objective_c
deviceController->skyController->sendAccessPointSettingsAccessPointChannel(deviceController->skyController, (uint8_t)channel);
```

```java
deviceController.getFeatureSkyController().sendAccessPointSettingsAccessPointChannel((byte)channel);
```

*This message is deprecated.*<br/>

Set the SkyController access point channel.<br/>
The channel will be checked, and can be modified before application. Use the [AccessPointChannelChanged](#SkyController-AccessPointSettingsState-AccessPointChannelChanged) event to get the applied channel.<br/>
The list of authorized channels for the current country can be retrived with the [WifiAuthChannel](#SkyController-Wifi-WifiAuthChannel) command.<br/>
This command is deprecated. Use the [WifiSelection](#SkyController-AccessPointSettings-WifiSelection) command instead.<br/>


* channel (u8): AccessPoint Channel<br/>


Result:<br/>
The network channel will change (which will likely disconnect the controller), then an [AccessPointChannelChanged](#SkyController-AccessPointSettingsState-AccessPointChannelChanged) event will be sent<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AccessPointSettings-WifiSelection-->
### <a name="SkyController-AccessPointSettings-WifiSelection">Set access point band/channel</a><br/>
> Set access point band/channel:

```c
deviceController->skyController->sendAccessPointSettingsWifiSelection(deviceController->skyController, (eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGS_WIFISELECTION_TYPE)type, (eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGS_WIFISELECTION_BAND)band, (uint8_t)channel);
```

```objective_c
deviceController->skyController->sendAccessPointSettingsWifiSelection(deviceController->skyController, (eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGS_WIFISELECTION_TYPE)type, (eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGS_WIFISELECTION_BAND)band, (uint8_t)channel);
```

```java
deviceController.getFeatureSkyController().sendAccessPointSettingsWifiSelection((ARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGS_WIFISELECTION_TYPE_ENUM)type, (ARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGS_WIFISELECTION_BAND_ENUM)band, (byte)channel);
```

Set the SkyController access point channel.<br/>
The channel will be checked, and can be modified before application. Use the [WifiSelectionChanged](#SkyController-AccessPointSettingsState-WifiSelectionChanged) event to get the applied channel/band.<br/>
The list of authorized channels for the current country can be retrived with the [WifiAuthChannel](#SkyController-Wifi-WifiAuthChannel) command.<br/>


* type (enum): The type of wifi selection (only manual at the moment)<br/>
   * manual: Manual selection<br/>
* band (enum): The allowed band : 2.4 Ghz or 5 Ghz<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
* channel (u8): The channel<br/>


Result:<br/>
The network channel will change (which will likely disconnect the controller), then a [WifiSelectionChanged](#SkyController-AccessPointSettingsState-WifiSelectionChanged) event will be sent<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AccessPointSettings-WifiSecurity-->
### <a name="SkyController-AccessPointSettings-WifiSecurity">Set access point security</a><br/>
> Set access point security:

```c
deviceController->skyController->sendAccessPointSettingsWifiSecurity(deviceController->skyController, (eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGS_WIFISECURITY_SECURITY_TYPE)security_type, (char *)key);
```

```objective_c
deviceController->skyController->sendAccessPointSettingsWifiSecurity(deviceController->skyController, (eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGS_WIFISECURITY_SECURITY_TYPE)security_type, (char *)key);
```

```java
deviceController.getFeatureSkyController().sendAccessPointSettingsWifiSecurity((ARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGS_WIFISECURITY_SECURITY_TYPE_ENUM)security_type, (String)key);
```

Set the SkyController access point security. The key will be checked, and can be refused by the product. In this case, the security will not be changed. Use the [WifiSecurityChanged](#SkyController-AccessPointSettingsState-WifiSecurityChanged) event to get the applied security settings.<br/>


* security_type (enum): The type of security for the network<br/>
   * open: Wifi is not protected (default)<br/>
   * wpa2: Wifi is protected by wpa2<br/>
* key (string): The security key (ignored if security_type is open)<br/>


Result:<br/>
The network security will change (which will likely disconnect the controller), then a [WifiSecurityChanged](#SkyController-AccessPointSettingsState-WifiSecurityChanged) event will be sent<br/>


*Supported by <br/>*

<br/>

<!-- SkyController-Camera-ResetOrientation-->
### <a name="SkyController-Camera-ResetOrientation">Reset the camera orientation (deprecated)</a><br/>
> Reset the camera orientation (deprecated):

```c
deviceController->skyController->sendCameraResetOrientation(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendCameraResetOrientation(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendCameraResetOrientation();
```

*This message is deprecated.*<br/>

This command is deprecated. The same effect can be achieved by sending a [CameraOrientation](#ARDrone3-Camera-Orientation) command with values retrieved from the [defaultCameraOrientation](#ARDrone3-CameraState-defaultCameraOrientation) event.<br/>




Result:<br/>
The drone will reset its camera orientation<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-GamepadInfos-getGamepadControls-->
### <a name="SkyController-GamepadInfos-getGamepadControls">Get the SkyController buttons and axis list</a><br/>
> Get the SkyController buttons and axis list:

```c
deviceController->skyController->sendGamepadInfosGetGamepadControls(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendGamepadInfosGetGamepadControls(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendGamepadInfosGetGamepadControls();
```

This commands allow the application to get a representation of all the mappable controls on the SkyController. Some physical controls might be absent from this list because their function can not be changed.<br/>




Result:<br/>
The SkyController will send a list of [GamepadControl](#SkyController-GamepadInfosState-gamepadControl) events, describing all available controls, followed by an [allGamepadControlsSent](#SkyController-GamepadInfosState-allGamepadControlsSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-ButtonMappings-getCurrentButtonMappings-->
### <a name="SkyController-ButtonMappings-getCurrentButtonMappings">Get the current button mappings</a><br/>
> Get the current button mappings:

```c
deviceController->skyController->sendButtonMappingsGetCurrentButtonMappings(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendButtonMappingsGetCurrentButtonMappings(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendButtonMappingsGetCurrentButtonMappings();
```

The SkyController will send its full button mapping. This command is mainly useful for initial synchronization, as every change to the button mapping (via the [setButtonMapping](#SkyController-ButtonMappings-setButtonMapping) command) will trigger [currentButtonMappings](#SkyController-ButtonMappingsState-currentButtonMappings) events.<br/>




Result:<br/>
The SkyController will send a full list of [currentButtonMappings](#SkyController-ButtonMappingsState-currentButtonMappings) events, followed by an [allCurrentButtonMappingsSent](#SkyController-ButtonMappingsState-allCurrentButtonMappingsSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-ButtonMappings-getAvailableButtonMappings-->
### <a name="SkyController-ButtonMappings-getAvailableButtonMappings">Get the available button mappings</a><br/>
> Get the available button mappings:

```c
deviceController->skyController->sendButtonMappingsGetAvailableButtonMappings(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendButtonMappingsGetAvailableButtonMappings(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendButtonMappingsGetAvailableButtonMappings();
```

The SkyController will send all the available action that can be mapped on buttons.<br/>
As this list is static, the controller only need to request this information once.<br/>




Result:<br/>
The SkyController will send a list of [availableButtonMappings](#SkyController-ButtonMappingsState-availableButtonMappings) events, followed by an [allAvailableButtonsMappingsSent](#SkyController-ButtonMappingsState-allAvailableButtonsMappingsSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-ButtonMappings-setButtonMapping-->
### <a name="SkyController-ButtonMappings-setButtonMapping">Set a mapping for a button</a><br/>
> Set a mapping for a button:

```c
deviceController->skyController->sendButtonMappingsSetButtonMapping(deviceController->skyController, (int32_t)key_id, (char *)mapping_uid);
```

```objective_c
deviceController->skyController->sendButtonMappingsSetButtonMapping(deviceController->skyController, (int32_t)key_id, (char *)mapping_uid);
```

```java
deviceController.getFeatureSkyController().sendButtonMappingsSetButtonMapping((int)key_id, (String)mapping_uid);
```

Any previous mapping for the given button will be removed, as a button can only be mapped to one action.<br/>
To unmap a button, a NO_ACTION mapping can be used (see the [availableButtonMappings](#SkyController-ButtonMappingsState-availableButtonMappings) event).<br/>
Some actions can not be mapped to two different buttons at the same time. In this case, the first button will automatically be set to NO_ACTION, and the corresponding [currentButtonMappings](#SkyController-ButtonMappingsState-currentButtonMappings) event will be fired.<br/>


* key_id (i32): The keycode to map<br/>
* mapping_uid (string): The mapping to associate with the key<br/>


Result:<br/>
The SkyController will send a list of [currentButtonMappings](#SkyController-ButtonMappingsState-currentButtonMappings) events, describing the changes to the mapping table, followed by an [allCurrentButtonMappingsSent](#SkyController-ButtonMappingsState-allCurrentButtonMappingsSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-ButtonMappings-defaultButtonMapping-->
### <a name="SkyController-ButtonMappings-defaultButtonMapping">Reset the button mappings to the default value</a><br/>
> Reset the button mappings to the default value:

```c
deviceController->skyController->sendButtonMappingsDefaultButtonMapping(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendButtonMappingsDefaultButtonMapping(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendButtonMappingsDefaultButtonMapping();
```

The default values can change between software versions.<br/>
The default values are different for Black Edition SkyControllers<br/>




Result:<br/>
The SkyController will send a list of [currentButtonMappings](#SkyController-ButtonMappingsState-currentButtonMappings) events, describing the changes to the mapping table, followed by an [allCurrentButtonMappingsSent](#SkyController-ButtonMappingsState-allCurrentButtonMappingsSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AxisMappings-getCurrentAxisMappings-->
### <a name="SkyController-AxisMappings-getCurrentAxisMappings">Get the current axis mappings</a><br/>
> Get the current axis mappings:

```c
deviceController->skyController->sendAxisMappingsGetCurrentAxisMappings(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendAxisMappingsGetCurrentAxisMappings(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendAxisMappingsGetCurrentAxisMappings();
```

The SkyController will send its full axis mapping. This command is mainly useful for initial synchronization, as every change to the axis mapping (via the [setAxisMapping](#SkyController-AxisMappings-setAxisMapping) command) will trigger [currentAxisMappings](#SkyController-AxisMappingsState-currentAxisMappings) events.<br/>




Result:<br/>
The SkyController will send a full list of [currentAxisMappings](#SkyController-AxisMappingsState-currentAxisMappings) events, followed by an [allCurrentAxisMappingsSent](#SkyController-AxisMappingsState-allCurrentAxisMappingsSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AxisMappings-getAvailableAxisMappings-->
### <a name="SkyController-AxisMappings-getAvailableAxisMappings">Get the available axis mappings</a><br/>
> Get the available axis mappings:

```c
deviceController->skyController->sendAxisMappingsGetAvailableAxisMappings(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendAxisMappingsGetAvailableAxisMappings(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendAxisMappingsGetAvailableAxisMappings();
```

The SkyController will send all the available action that can be mapped on axes.<br/>
As this list is static, the controller only need to request this information once.<br/>




Result:<br/>
The SkyController will send a list of [availableAxisMappings](#SkyController-AxisMappingsState-availableAxisMappings) events, followed by an [allAvailableAxissMappingsSent](#SkyController-AxisMappingsState-allAvailableAxisMappingsSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AxisMappings-setAxisMapping-->
### <a name="SkyController-AxisMappings-setAxisMapping">Set a mapping for a axis</a><br/>
> Set a mapping for a axis:

```c
deviceController->skyController->sendAxisMappingsSetAxisMapping(deviceController->skyController, (int32_t)axis_id, (char *)mapping_uid);
```

```objective_c
deviceController->skyController->sendAxisMappingsSetAxisMapping(deviceController->skyController, (int32_t)axis_id, (char *)mapping_uid);
```

```java
deviceController.getFeatureSkyController().sendAxisMappingsSetAxisMapping((int)axis_id, (String)mapping_uid);
```

Any previous mapping for the given axis will be removed, as a axis can only be mapped to one action.<br/>
To unmap a axis, a NO_ACTION mapping can be used (see the [availableAxisMappings](#SkyController-AxisMappingsState-availableAxisMappings) event).<br/>
Some actions can not be mapped to two different axes at the same time. In this case, the first axis will automatically be set to NO_ACTION, and the corresponding [currentAxisMappings](#SkyController-AxisMappingsState-currentAxisMappings) event will be fired.<br/>


* axis_id (i32): The axiscode to map<br/>
* mapping_uid (string): The mapping to associate with the axis<br/>


Result:<br/>
The SkyController will send a list of [currentAxisMappings](#SkyController-AxisMappingsState-currentAxisMappings) events, describing the changes to the mapping table, followed by an [allCurrentAxisMappingsSent](#SkyController-AxisMappingsState-allCurrentAxisMappingsSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AxisMappings-defaultAxisMapping-->
### <a name="SkyController-AxisMappings-defaultAxisMapping">Reset the axis mappings to the default value</a><br/>
> Reset the axis mappings to the default value:

```c
deviceController->skyController->sendAxisMappingsDefaultAxisMapping(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendAxisMappingsDefaultAxisMapping(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendAxisMappingsDefaultAxisMapping();
```

The default values can change between software versions.<br/>




Result:<br/>
The SkyController will send a list of [currentAxisMappings](#SkyController-AxisMappingsState-currentAxisMappings) events, describing the changes to the mapping table, followed by an [allCurrentAxisMappingsSent](#SkyController-AxisMappingsState-allCurrentAxisMappingsSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AxisFilters-getCurrentAxisFilters-->
### <a name="SkyController-AxisFilters-getCurrentAxisFilters">Get the current axis filters</a><br/>
> Get the current axis filters:

```c
deviceController->skyController->sendAxisFiltersGetCurrentAxisFilters(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendAxisFiltersGetCurrentAxisFilters(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendAxisFiltersGetCurrentAxisFilters();
```

The SkyController will send its full axis filters map. This command is mainly useful for initial synchronization, as every change to the filters map (via the [setAxisFilter](#SkyController-AxisFilters-setAxisFilter) command) will trigger [currentAxisFilters](#SkyController-AxisFiltersState-currentAxisFilters) events.<br/>




Result:<br/>
The SkyController will send a full list of [currentAxisFilters](#SkyController-AxisFiltersState-currentAxisFilters) events, followed by an [allCurrentFiltersSent](#SkyController-AxisFiltersState-allCurrentFiltersSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AxisFilters-getPresetAxisFilters-->
### <a name="SkyController-AxisFilters-getPresetAxisFilters">Get the available preset axis filters (deprecated)</a><br/>
> Get the available preset axis filters (deprecated):

```c
deviceController->skyController->sendAxisFiltersGetPresetAxisFilters(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendAxisFiltersGetPresetAxisFilters(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendAxisFiltersGetPresetAxisFilters();
```

*This message is deprecated.*<br/>

The preset list is empty and will never be filled, so this command is flagged as deprecated.<br/>




Result:<br/>
As the preset list is empty, the SkyController will just send an [allPresetFiltersSent](#SkyController-AxisFiltersState-allPresetFiltersSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AxisFilters-setAxisFilter-->
### <a name="SkyController-AxisFilters-setAxisFilter">Set a filter for an axis</a><br/>
> Set a filter for an axis:

```c
deviceController->skyController->sendAxisFiltersSetAxisFilter(deviceController->skyController, (int32_t)axis_id, (char *)filter_uid_or_builder);
```

```objective_c
deviceController->skyController->sendAxisFiltersSetAxisFilter(deviceController->skyController, (int32_t)axis_id, (char *)filter_uid_or_builder);
```

```java
deviceController.getFeatureSkyController().sendAxisFiltersSetAxisFilter((int)axis_id, (String)filter_uid_or_builder);
```

A filter modifies the response curve of an axis.<br/>
As the preset filters list is empty, all filters are to be sent using the builder syntax.<br/>
<br/>
The builder syntax supports two types of filters: Multilinear and Exponential.<br/>
<br/>
Multilinear filters create response curves made of multiple linear segments:<br/>
* The default filter (ARMF;) is purely linear and create a single segment from the two implicit `[-1; -1]` and `[1; 1]` points.<br/>
* Additionnal points can be added to the filter with the following syntax: `ARMF;x1>y1;...;xN>yN;`, where all numbers are floating point numbers in range `[-1; 1]`.<br/>
* Additionnal points **must** respect the following constraints : `x(N)>x(N-1)` and `y(N)>=y(N-1)`.<br/>
<br/>
Exponential filters:<br/>
* The syntax is `ARXF;CPx;CPy;`, where CPx and CPy are floating point numbers in range `[0; 1]`.<br/>
* Best results are achieved when `CPx + CPy == 1` and `CPx > CPy`.<br/>
* If the control point is on the diagonal (i.e. `CPx == CPy`), then the resulting filter will be linear.<br/>


* axis_id (i32): The axiscode to filter<br/>
* filter_uid_or_builder (string): The mapping preset to associate with the axis<br/>
(Or a string to build a new one)<br/>


Result:<br/>
The SkyController will send a list of [currentAxisFilters](#SkyController-AxisFiltersState-currentAxisFilters) events, describing the changes to the filters table, followed by an [allCurrentFiltersSent](#SkyController-AxisFiltersState-allCurrentFiltersSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


<br/>

<!-- SkyController-AxisFilters-defaultAxisFilters-->
### <a name="SkyController-AxisFilters-defaultAxisFilters">Reset the axis filters to the default value</a><br/>
> Reset the axis filters to the default value:

```c
deviceController->skyController->sendAxisFiltersDefaultAxisFilters(deviceController->skyController);
```

```objective_c
deviceController->skyController->sendAxisFiltersDefaultAxisFilters(deviceController->skyController);
```

```java
deviceController.getFeatureSkyController().sendAxisFiltersDefaultAxisFilters();
```

The default values can change between software versions.<br/>




Result:<br/>
The SkyController will send a list of [currentAxisFilters](#SkyController-AxisFiltersState-currentAxisFilters) events, describing the changes to the filters table, followed by an [allCurrentFiltersSent](#SkyController-AxisFiltersState-allCurrentFiltersSent) event.<br/>


*Supported by <br/>*

- *SkyController*<br/>


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

