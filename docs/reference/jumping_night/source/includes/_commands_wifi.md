<!-- wifi-scan-->
### <a name="wifi-scan">Scan wifi network</a><br/>
> Scan wifi network:

```c
deviceController->wifi->sendScan(deviceController->wifi, (uint8_t)band);
```

```objective_c
deviceController->wifi->sendScan(deviceController->wifi, (uint8_t)band);
```

```java
deviceController.getFeatureWifi().sendScan((byte)band);
```

Launches wifi network scan for a given band to get a list of all wifi networks found by the drone.<br/>


* band (bitfield as u8): The band : 2.4 Ghz or 5 Ghz<br/>
   * 2_4_ghz: 2.4 GHz band<br/>
   * 5_ghz: 5 GHz band<br/>


Result:<br/>
Event [WifiScanListChanged](#wifi-scanned_item) is triggered with all networks found.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

<!-- wifi-update_authorized_channels-->
### <a name="wifi-update_authorized_channels">Get all available Wifi channels</a><br/>
> Get all available Wifi channels:

```c
deviceController->wifi->sendUpdateAuthorizedChannels(deviceController->wifi);
```

```objective_c
deviceController->wifi->sendUpdateAuthorizedChannels(deviceController->wifi);
```

```java
deviceController.getFeatureWifi().sendUpdateAuthorizedChannels();
```

Get all available Wifi channels.<br/>
The list of available Wifi channels is related to the country of the drone. You can get this country with the event [WifiCountryChanged](#wifi-CountryChanged).<br/>




Result:<br/>
Event [AvailableChannelListChanged](#wifi-authorized_channel) is triggered with all authorized channels.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

<!-- wifi-set_ap_channel-->
### <a name="wifi-set_ap_channel">Wifi selection</a><br/>
> Wifi selection:

```c
deviceController->wifi->sendSetApChannel(deviceController->wifi, (eARCOMMANDS_WIFI_SELECTION_TYPE)type, (eARCOMMANDS_WIFI_BAND)band, (uint8_t)channel);
```

```objective_c
deviceController->wifi->sendSetApChannel(deviceController->wifi, (eARCOMMANDS_WIFI_SELECTION_TYPE)type, (eARCOMMANDS_WIFI_BAND)band, (uint8_t)channel);
```

```java
deviceController.getFeatureWifi().sendSetApChannel((ARCOMMANDS_WIFI_SELECTION_TYPE_ENUM)type, (ARCOMMANDS_WIFI_BAND_ENUM)band, (byte)channel);
```

Select channel of choosen band to put the drone's access point on this channel.<br/>


* type (enum): The wifi selection type available<br/>
   * auto_all: Auto selection on all channels<br/>
   * auto_2_4_ghz: Auto selection 2.4ghz<br/>
   * auto_5_ghz: Auto selection 5 ghz<br/>
   * manual: manual selection<br/>
* band (enum): The band : 2.4 Ghz or 5 Ghz<br/>
   * 2_4_ghz: 2.4 GHz band<br/>
   * 5_ghz: 5 GHz band<br/>
* channel (u8): The channel you want to select. Used only when type is manual.<br/>


Result:<br/>
The wifi channel changes according to given parameters. Watch out, a disconnection might appear.<br/>
Then, event [WifiSelectionChanged](#wifi-ap_channel_changed) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

<!-- wifi-set_security-->
### <a name="wifi-set_security">Set the wifi security</a><br/>
> Set the wifi security:

```c
deviceController->wifi->sendSetSecurity(deviceController->wifi, (eARCOMMANDS_WIFI_SECURITY_TYPE)type, (char *)key, (eARCOMMANDS_WIFI_SECURITY_KEY_TYPE)key_type);
```

```objective_c
deviceController->wifi->sendSetSecurity(deviceController->wifi, (eARCOMMANDS_WIFI_SECURITY_TYPE)type, (char *)key, (eARCOMMANDS_WIFI_SECURITY_KEY_TYPE)key_type);
```

```java
deviceController.getFeatureWifi().sendSetSecurity((ARCOMMANDS_WIFI_SECURITY_TYPE_ENUM)type, (String)key, (ARCOMMANDS_WIFI_SECURITY_KEY_TYPE_ENUM)key_type);
```

Set the wifi security.<br/>
The security is changed on the next boot.<br/>


* type (enum): The type of wifi security (open, wpa2)<br/>
   * open: Wifi is not protected by any security (default)<br/>
   * wpa2: Wifi is protected by wpa2<br/>
* key (string): The key to secure the network. Not used if type is open<br/>
* key_type (enum): Type of the key sent<br/>
   * plain: Key is plain text, not encrypted<br/>


Result:<br/>
The wifi security is set.<br/>
Then, event [WifiSecurityChanged](#wifi-security_changed) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2 since 3.1.0*<br/>


<br/>

<!-- wifi-set_country-->
### <a name="wifi-set_country">Set the wifi country</a><br/>
> Set the wifi country:

```c
deviceController->wifi->sendSetCountry(deviceController->wifi, (eARCOMMANDS_WIFI_COUNTRY_SELECTION)selection_mode, (char *)code);
```

```objective_c
deviceController->wifi->sendSetCountry(deviceController->wifi, (eARCOMMANDS_WIFI_COUNTRY_SELECTION)selection_mode, (char *)code);
```

```java
deviceController.getFeatureWifi().sendSetCountry((ARCOMMANDS_WIFI_COUNTRY_SELECTION_ENUM)selection_mode, (String)code);
```

Set the wifi country.<br/>


* selection_mode (enum): Type of country selection<br/>
   * manual: Manual selection.<br/>
   * auto: Automatic selection.<br/>
* code (string): Country code with ISO 3166 format. Not used if automatic is 1.<br/>


Result:<br/>
The country of the product is changed.<br/>
Then, it will trigger [CountryChanged](#wifi-country_changed).<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

<!-- wifi-set_environment-->
### <a name="wifi-set_environment">Set indoor/outdoor wifi settings</a><br/>
> Set indoor/outdoor wifi settings:

```c
deviceController->wifi->sendSetEnvironment(deviceController->wifi, (eARCOMMANDS_WIFI_ENVIRONMENT)environment);
```

```objective_c
deviceController->wifi->sendSetEnvironment(deviceController->wifi, (eARCOMMANDS_WIFI_ENVIRONMENT)environment);
```

```java
deviceController.getFeatureWifi().sendSetEnvironment((ARCOMMANDS_WIFI_ENVIRONMENT_ENUM)environment);
```

Set indoor or outdoor wifi settings.<br/>


* environment (enum): Type of environment<br/>
   * indoor: indoor environment<br/>
   * outdoor: outdoor environment<br/>


Result:<br/>
The product change its indoor/outdoor wifi settings.<br/>
Then, it will trigger [OutdoorChanged](#wifi-environment_changed).<br/>
According to the country (defined by [SetAutoCountry](#wifi-AutoCountry) or [SetCountry](#wifi-Country)) laws the drone might change its wifi band and channel. So a disconnection might appear.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

