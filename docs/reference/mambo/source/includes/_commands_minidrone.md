<!-- MiniDrone-PilotingSettings-BankedTurn-->
### <a name="MiniDrone-PilotingSettings-BankedTurn">Set banked turn mode</a><br/>
> Set banked turn mode:

```c
deviceController->miniDrone->sendPilotingSettingsBankedTurn(deviceController->miniDrone, (uint8_t)value);
```

```objective_c
deviceController->miniDrone->sendPilotingSettingsBankedTurn(deviceController->miniDrone, (uint8_t)value);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingSettingsBankedTurn((byte)value);
```

Set banked turn mode.<br/>
When banked turn mode is enabled, the drone will use yaw values from the piloting command to infer with roll and pitch on the drone when its horizontal speed is not null.<br/>


* value (u8): 1 to enable, 0 to disable<br/>


Result:<br/>
The banked turn mode is enabled or disabled.<br/>
Then, event [BankedTurnMode](#MiniDrone-PilotingSettingsState-BankedTurnChanged) is triggered.<br/>


*Supported by <br/>*

- *Mambo since 3.0.6*<br/>


<br/>

