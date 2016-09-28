<!-- JumpingSumo-Piloting-PCMD-->
### <a name="JumpingSumo-Piloting-PCMD">Ask the JS speed and turn ratio.</a><br/>
> Ask the JS speed and turn ratio.:

```c
deviceController->jumpingSumo->sendPilotingPCMD(deviceController->jumpingSumo, (uint8_t)flag, (int8_t)speed, (int8_t)turn);
```

```objective_c
deviceController->jumpingSumo->sendPilotingPCMD(deviceController->jumpingSumo, (uint8_t)flag, (int8_t)speed, (int8_t)turn);
```

```java
deviceController.getFeatureJumpingSumo().sendPilotingPCMD((byte)flag, (byte)speed, (byte)turn);
```

Ask the JS speed and turn ratio.<br/>


* flag (u8): Boolean for "touch screen".<br/>
* speed (i8): Speed value [-100:100].<br/>
* turn (i8): Turn value. [-100:100]<br/>
<br/>

<!-- JumpingSumo-Piloting-Posture-->
### <a name="JumpingSumo-Piloting-Posture">Request a posture</a><br/>
> Request a posture:

```c
deviceController->jumpingSumo->sendPilotingPosture(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_PILOTING_POSTURE_TYPE)type);
```

```objective_c
deviceController->jumpingSumo->sendPilotingPosture(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_PILOTING_POSTURE_TYPE)type);
```

```java
deviceController.getFeatureJumpingSumo().sendPilotingPosture((ARCOMMANDS_JUMPINGSUMO_PILOTING_POSTURE_TYPE_ENUM)type);
```

Request a posture<br/>


* type (enum): Type of Posture<br/>
   * standing: Standing type<br/>
   * jumper: Jumper type<br/>
   * kicker: Kicker type<br/>
<br/>

<!-- JumpingSumo-Piloting-addCapOffset-->
### <a name="JumpingSumo-Piloting-addCapOffset">Add the specified offset to the current cap.</a><br/>
> Add the specified offset to the current cap.:

```c
deviceController->jumpingSumo->sendPilotingAddCapOffset(deviceController->jumpingSumo, (float)offset);
```

```objective_c
deviceController->jumpingSumo->sendPilotingAddCapOffset(deviceController->jumpingSumo, (float)offset);
```

```java
deviceController.getFeatureJumpingSumo().sendPilotingAddCapOffset((float)offset);
```

Add the specified offset to the current cap.<br/>


* offset (float): Offset value in radians.<br/>
<br/>

<!-- JumpingSumo-Animations-JumpStop-->
### <a name="JumpingSumo-Animations-JumpStop">Stop jump, emergency jump stop, stop jump motor and stay there.</a><br/>
> Stop jump, emergency jump stop, stop jump motor and stay there.:

```c
deviceController->jumpingSumo->sendAnimationsJumpStop(deviceController->jumpingSumo);
```

```objective_c
deviceController->jumpingSumo->sendAnimationsJumpStop(deviceController->jumpingSumo);
```

```java
deviceController.getFeatureJumpingSumo().sendAnimationsJumpStop();
```

Stop jump, emergency jump stop, stop jump motor and stay there.<br/>


<br/>

<!-- JumpingSumo-Animations-JumpCancel-->
### <a name="JumpingSumo-Animations-JumpCancel">Cancel jump and come back to previous state (if possible).</a><br/>
> Cancel jump and come back to previous state (if possible).:

```c
deviceController->jumpingSumo->sendAnimationsJumpCancel(deviceController->jumpingSumo);
```

```objective_c
deviceController->jumpingSumo->sendAnimationsJumpCancel(deviceController->jumpingSumo);
```

```java
deviceController.getFeatureJumpingSumo().sendAnimationsJumpCancel();
```

Cancel jump and come back to previous state (if possible).<br/>


<br/>

<!-- JumpingSumo-Animations-JumpLoad-->
### <a name="JumpingSumo-Animations-JumpLoad">Request jump loading</a><br/>
> Request jump loading:

```c
deviceController->jumpingSumo->sendAnimationsJumpLoad(deviceController->jumpingSumo);
```

```objective_c
deviceController->jumpingSumo->sendAnimationsJumpLoad(deviceController->jumpingSumo);
```

```java
deviceController.getFeatureJumpingSumo().sendAnimationsJumpLoad();
```

Request jump loading<br/>


<br/>

<!-- JumpingSumo-Animations-Jump-->
### <a name="JumpingSumo-Animations-Jump">Request a jump</a><br/>
> Request a jump:

```c
deviceController->jumpingSumo->sendAnimationsJump(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_ANIMATIONS_JUMP_TYPE)type);
```

```objective_c
deviceController->jumpingSumo->sendAnimationsJump(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_ANIMATIONS_JUMP_TYPE)type);
```

```java
deviceController.getFeatureJumpingSumo().sendAnimationsJump((ARCOMMANDS_JUMPINGSUMO_ANIMATIONS_JUMP_TYPE_ENUM)type);
```

Request a jump<br/>


* type (enum): Type of jump<br/>
   * long: Long jump.<br/>
   * high: High jump<br/>
<br/>

<!-- JumpingSumo-Animations-SimpleAnimation-->
### <a name="JumpingSumo-Animations-SimpleAnimation">Play a parameterless animation.</a><br/>
> Play a parameterless animation.:

```c
deviceController->jumpingSumo->sendAnimationsSimpleAnimation(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_ANIMATIONS_SIMPLEANIMATION_ID)id);
```

```objective_c
deviceController->jumpingSumo->sendAnimationsSimpleAnimation(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_ANIMATIONS_SIMPLEANIMATION_ID)id);
```

```java
deviceController.getFeatureJumpingSumo().sendAnimationsSimpleAnimation((ARCOMMANDS_JUMPINGSUMO_ANIMATIONS_SIMPLEANIMATION_ID_ENUM)id);
```

Play a parameterless animation.<br/>


* id (enum): Animation ID.<br/>
   * stop: Stop ongoing animation.<br/>
   * spin: Start a spin animation.<br/>
   * tap: Start a tap animation.<br/>
   * slowshake: Start a slow shake animation.<br/>
   * metronome: Start a Metronome animation.<br/>
   * ondulation: Start a standing dance animation.<br/>
   * spinjump: Start a spin jump animation.<br/>
   * spintoposture: Start a spin that end in standing posture, or in jumper if it was standing animation.<br/>
   * spiral: Start a spiral animation.<br/>
   * slalom: Start a slalom animation.<br/>
<br/>

<!-- JumpingSumo-MediaRecord-Picture-->
### <a name="JumpingSumo-MediaRecord-Picture">@deprecated</a><br/>
> @deprecated:

```c
deviceController->jumpingSumo->sendMediaRecordPicture(deviceController->jumpingSumo, (uint8_t)mass_storage_id);
```

```objective_c
deviceController->jumpingSumo->sendMediaRecordPicture(deviceController->jumpingSumo, (uint8_t)mass_storage_id);
```

```java
deviceController.getFeatureJumpingSumo().sendMediaRecordPicture((byte)mass_storage_id);
```

@deprecated<br/>
Take picture<br/>


* mass_storage_id (u8): Mass storage id to take picture<br/>
<br/>

<!-- JumpingSumo-MediaRecord-Video-->
### <a name="JumpingSumo-MediaRecord-Video">@deprecated</a><br/>
> @deprecated:

```c
deviceController->jumpingSumo->sendMediaRecordVideo(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_MEDIARECORD_VIDEO_RECORD)record, (uint8_t)mass_storage_id);
```

```objective_c
deviceController->jumpingSumo->sendMediaRecordVideo(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_MEDIARECORD_VIDEO_RECORD)record, (uint8_t)mass_storage_id);
```

```java
deviceController.getFeatureJumpingSumo().sendMediaRecordVideo((ARCOMMANDS_JUMPINGSUMO_MEDIARECORD_VIDEO_RECORD_ENUM)record, (byte)mass_storage_id);
```

@deprecated<br/>
Video record<br/>


* record (enum): Command to record video<br/>
   * stop: Stop the video recording<br/>
   * start: Start the video recording<br/>
* mass_storage_id (u8): Mass storage id to record<br/>
<br/>

<!-- JumpingSumo-MediaRecord-PictureV2-->
### <a name="JumpingSumo-MediaRecord-PictureV2">Take picture</a><br/>
> Take picture:

```c
deviceController->jumpingSumo->sendMediaRecordPictureV2(deviceController->jumpingSumo);
```

```objective_c
deviceController->jumpingSumo->sendMediaRecordPictureV2(deviceController->jumpingSumo);
```

```java
deviceController.getFeatureJumpingSumo().sendMediaRecordPictureV2();
```

Take picture<br/>


<br/>

<!-- JumpingSumo-MediaRecord-VideoV2-->
### <a name="JumpingSumo-MediaRecord-VideoV2">Video record</a><br/>
> Video record:

```c
deviceController->jumpingSumo->sendMediaRecordVideoV2(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_MEDIARECORD_VIDEOV2_RECORD)record);
```

```objective_c
deviceController->jumpingSumo->sendMediaRecordVideoV2(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_MEDIARECORD_VIDEOV2_RECORD)record);
```

```java
deviceController.getFeatureJumpingSumo().sendMediaRecordVideoV2((ARCOMMANDS_JUMPINGSUMO_MEDIARECORD_VIDEOV2_RECORD_ENUM)record);
```

Video record<br/>


* record (enum): Command to record video<br/>
   * stop: Stop the video recording<br/>
   * start: Start the video recording<br/>
<br/>

<!-- JumpingSumo-NetworkSettings-WifiSelection-->
### <a name="JumpingSumo-NetworkSettings-WifiSelection">Auto-select channel of choosen band</a><br/>
> Auto-select channel of choosen band:

```c
deviceController->jumpingSumo->sendNetworkSettingsWifiSelection(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_NETWORKSETTINGS_WIFISELECTION_TYPE)type, (eARCOMMANDS_JUMPINGSUMO_NETWORKSETTINGS_WIFISELECTION_BAND)band, (uint8_t)channel);
```

```objective_c
deviceController->jumpingSumo->sendNetworkSettingsWifiSelection(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_NETWORKSETTINGS_WIFISELECTION_TYPE)type, (eARCOMMANDS_JUMPINGSUMO_NETWORKSETTINGS_WIFISELECTION_BAND)band, (uint8_t)channel);
```

```java
deviceController.getFeatureJumpingSumo().sendNetworkSettingsWifiSelection((ARCOMMANDS_JUMPINGSUMO_NETWORKSETTINGS_WIFISELECTION_TYPE_ENUM)type, (ARCOMMANDS_JUMPINGSUMO_NETWORKSETTINGS_WIFISELECTION_BAND_ENUM)band, (byte)channel);
```

Auto-select channel of choosen band<br/>


* type (enum): The type of wifi selection (auto, manual)<br/>
   * auto: Auto selection<br/>
   * manual: Manual selection<br/>
* band (enum): The allowed band(s) : 2.4 Ghz, 5 Ghz, or all<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
   * all: Both 2.4 and 5 GHz bands<br/>
* channel (u8): The channel (not used in auto mode)<br/>
<br/>

<!-- JumpingSumo-Network-WifiScan-->
### <a name="JumpingSumo-Network-WifiScan">Launches wifi network scan</a><br/>
> Launches wifi network scan:

```c
deviceController->jumpingSumo->sendNetworkWifiScan(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_NETWORK_WIFISCAN_BAND)band);
```

```objective_c
deviceController->jumpingSumo->sendNetworkWifiScan(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_NETWORK_WIFISCAN_BAND)band);
```

```java
deviceController.getFeatureJumpingSumo().sendNetworkWifiScan((ARCOMMANDS_JUMPINGSUMO_NETWORK_WIFISCAN_BAND_ENUM)band);
```

Launches wifi network scan<br/>


* band (enum): The band(s) : 2.4 Ghz, 5 Ghz, or both<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
   * all: Both 2.4 and 5 GHz bands<br/>
<br/>

<!-- JumpingSumo-Network-WifiAuthChannel-->
### <a name="JumpingSumo-Network-WifiAuthChannel">Controller inquire the list of authorized wifi channels.</a><br/>
> Controller inquire the list of authorized wifi channels.:

```c
deviceController->jumpingSumo->sendNetworkWifiAuthChannel(deviceController->jumpingSumo);
```

```objective_c
deviceController->jumpingSumo->sendNetworkWifiAuthChannel(deviceController->jumpingSumo);
```

```java
deviceController.getFeatureJumpingSumo().sendNetworkWifiAuthChannel();
```

Controller inquire the list of authorized wifi channels.<br/>


<br/>

<!-- JumpingSumo-AudioSettings-MasterVolume-->
### <a name="JumpingSumo-AudioSettings-MasterVolume">Master volume control.</a><br/>
> Master volume control.:

```c
deviceController->jumpingSumo->sendAudioSettingsMasterVolume(deviceController->jumpingSumo, (uint8_t)volume);
```

```objective_c
deviceController->jumpingSumo->sendAudioSettingsMasterVolume(deviceController->jumpingSumo, (uint8_t)volume);
```

```java
deviceController.getFeatureJumpingSumo().sendAudioSettingsMasterVolume((byte)volume);
```

Master volume control.<br/>


* volume (u8): Master audio volume [0:100].<br/>
<br/>

<!-- JumpingSumo-AudioSettings-Theme-->
### <a name="JumpingSumo-AudioSettings-Theme">Audio Theme.</a><br/>
> Audio Theme.:

```c
deviceController->jumpingSumo->sendAudioSettingsTheme(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_AUDIOSETTINGS_THEME_THEME)theme);
```

```objective_c
deviceController->jumpingSumo->sendAudioSettingsTheme(deviceController->jumpingSumo, (eARCOMMANDS_JUMPINGSUMO_AUDIOSETTINGS_THEME_THEME)theme);
```

```java
deviceController.getFeatureJumpingSumo().sendAudioSettingsTheme((ARCOMMANDS_JUMPINGSUMO_AUDIOSETTINGS_THEME_THEME_ENUM)theme);
```

Audio Theme.<br/>


* theme (enum): The audio theme to set.<br/>
   * default: Default audio theme (depends on the product color)<br/>
   * robot: Robot audio theme.<br/>
   * insect: Insect audio theme.<br/>
   * monster: Monster audio theme.<br/>
<br/>

<!-- JumpingSumo-RoadPlan-AllScriptsMetadata-->
### <a name="JumpingSumo-RoadPlan-AllScriptsMetadata">Command to ask device all metadata scripts.</a><br/>
> Command to ask device all metadata scripts.:

```c
deviceController->jumpingSumo->sendRoadPlanAllScriptsMetadata(deviceController->jumpingSumo);
```

```objective_c
deviceController->jumpingSumo->sendRoadPlanAllScriptsMetadata(deviceController->jumpingSumo);
```

```java
deviceController.getFeatureJumpingSumo().sendRoadPlanAllScriptsMetadata();
```

Command to ask device all metadata scripts.<br/>


<br/>

<!-- JumpingSumo-RoadPlan-ScriptUploaded-->
### <a name="JumpingSumo-RoadPlan-ScriptUploaded">Notify device that a new file has been uploaded.</a><br/>
> Notify device that a new file has been uploaded.:

```c
deviceController->jumpingSumo->sendRoadPlanScriptUploaded(deviceController->jumpingSumo, (char *)uuid, (char *)md5Hash);
```

```objective_c
deviceController->jumpingSumo->sendRoadPlanScriptUploaded(deviceController->jumpingSumo, (char *)uuid, (char *)md5Hash);
```

```java
deviceController.getFeatureJumpingSumo().sendRoadPlanScriptUploaded((String)uuid, (String)md5Hash);
```

Notify device that a new file has been uploaded.<br/>


* uuid (string): UUID of uploaded file.<br/>
* md5Hash (string): MD5 hash code computed over file.<br/>
<br/>

<!-- JumpingSumo-RoadPlan-ScriptDelete-->
### <a name="JumpingSumo-RoadPlan-ScriptDelete">Ask the device to delete a script.</a><br/>
> Ask the device to delete a script.:

```c
deviceController->jumpingSumo->sendRoadPlanScriptDelete(deviceController->jumpingSumo, (char *)uuid);
```

```objective_c
deviceController->jumpingSumo->sendRoadPlanScriptDelete(deviceController->jumpingSumo, (char *)uuid);
```

```java
deviceController.getFeatureJumpingSumo().sendRoadPlanScriptDelete((String)uuid);
```

Ask the device to delete a script.<br/>


* uuid (string): UUID of the file to delete.<br/>
<br/>

<!-- JumpingSumo-RoadPlan-PlayScript-->
### <a name="JumpingSumo-RoadPlan-PlayScript">Ask the device to play a script.</a><br/>
> Ask the device to play a script.:

```c
deviceController->jumpingSumo->sendRoadPlanPlayScript(deviceController->jumpingSumo, (char *)uuid);
```

```objective_c
deviceController->jumpingSumo->sendRoadPlanPlayScript(deviceController->jumpingSumo, (char *)uuid);
```

```java
deviceController.getFeatureJumpingSumo().sendRoadPlanPlayScript((String)uuid);
```

Ask the device to play a script.<br/>


* uuid (string): UUID of the file to play.<br/>
<br/>

<!-- JumpingSumo-SpeedSettings-Outdoor-->
### <a name="JumpingSumo-SpeedSettings-Outdoor">@deprecated</a><br/>
> @deprecated:

```c
deviceController->jumpingSumo->sendSpeedSettingsOutdoor(deviceController->jumpingSumo, (uint8_t)outdoor);
```

```objective_c
deviceController->jumpingSumo->sendSpeedSettingsOutdoor(deviceController->jumpingSumo, (uint8_t)outdoor);
```

```java
deviceController.getFeatureJumpingSumo().sendSpeedSettingsOutdoor((byte)outdoor);
```

@deprecated<br/>
Outdoor property<br/>


* outdoor (u8): 1 if outdoor, 0 if indoor<br/>
<br/>

<!-- JumpingSumo-MediaStreaming-VideoEnable-->
### <a name="JumpingSumo-MediaStreaming-VideoEnable">Enable/disable video streaming.</a><br/>
> Enable/disable video streaming.:

```c
deviceController->jumpingSumo->sendMediaStreamingVideoEnable(deviceController->jumpingSumo, (uint8_t)enable);
```

```objective_c
deviceController->jumpingSumo->sendMediaStreamingVideoEnable(deviceController->jumpingSumo, (uint8_t)enable);
```

```java
deviceController.getFeatureJumpingSumo().sendMediaStreamingVideoEnable((byte)enable);
```

Enable/disable video streaming.<br/>


* enable (u8): 1 to enable, 0 to disable.<br/>
<br/>

<!-- JumpingSumo-VideoSettings-Autorecord-->
### <a name="JumpingSumo-VideoSettings-Autorecord">Set video automatic recording state.</a><br/>
> Set video automatic recording state.:

```c
deviceController->jumpingSumo->sendVideoSettingsAutorecord(deviceController->jumpingSumo, (uint8_t)enabled);
```

```objective_c
deviceController->jumpingSumo->sendVideoSettingsAutorecord(deviceController->jumpingSumo, (uint8_t)enabled);
```

```java
deviceController.getFeatureJumpingSumo().sendVideoSettingsAutorecord((byte)enabled);
```

Set video automatic recording state.<br/>


* enabled (u8): 0: Disabled 1: Enabled.<br/>
<br/>

