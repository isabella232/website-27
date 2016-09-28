<!-- debug-get_all_settings-->
### <a name="debug-get_all_settings">Cmd sent by controller to get all settings info (generate "settings_info" events).</a><br/>
> Cmd sent by controller to get all settings info (generate "settings_info" events).:

```c
deviceController->debug->sendGetAllSettings(deviceController->debug);
```

```objective_c
deviceController->debug->sendGetAllSettings(deviceController->debug);
```

```java
deviceController.getFeatureDebug().sendGetAllSettings();
```

Cmd sent by controller to get all settings info (generate "settings_info" events).<br/>


<br/>

<!-- debug-set_setting-->
### <a name="debug-set_setting">Change setting value.</a><br/>
> Change setting value.:

```c
deviceController->debug->sendSetSetting(deviceController->debug, (uint16_t)id, (char *)value);
```

```objective_c
deviceController->debug->sendSetSetting(deviceController->debug, (uint16_t)id, (char *)value);
```

```java
deviceController.getFeatureDebug().sendSetSetting((short)id, (String)value);
```

Change setting value.<br/>
Cmd sent by controller to change a writable setting.<br/>


* id (u16): Setting Id.<br/>
* value (string): New setting value (string encoded).<br/>
<br/>

