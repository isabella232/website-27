<!-- drone_manager-discover_drones-->
### <a name="drone_manager-discover_drones">Request the drone list</a><br/>
> Request the drone list:

```c
deviceController->drone_manager->sendDiscoverDrones(deviceController->drone_manager);
```

```objective_c
deviceController->drone_manager->sendDiscoverDrones(deviceController->drone_manager);
```

```java
deviceController.getFeatureDroneManager().sendDiscoverDrones();
```

The list will contain:<br/>
* known drones not currently visible. * known drones currently visible. * unknown drones currently visible.<br/>




Result:<br/>
The drone manager will answer with a list of [drone\_list\_item](#drone_manager-drone_list_item)<br/>


*Supported by <br/>*

- *SkyController 2*<br/>
- *SkyController 2P*<br/>


<br/>

<!-- drone_manager-connect-->
### <a name="drone_manager-connect">Connect to a drone</a><br/>
> Connect to a drone:

```c
deviceController->drone_manager->sendConnect(deviceController->drone_manager, (char *)serial, (char *)key);
```

```objective_c
deviceController->drone_manager->sendConnect(deviceController->drone_manager, (char *)serial, (char *)key);
```

```java
deviceController.getFeatureDroneManager().sendConnect((String)serial, (String)key);
```

Request connection to a specific drone. Override the auto-selected drone.<br/>


* serial (string): Serial number of the drone.<br/>
* key (string): Security key (passphrase) to use.<br/>
This arg is ignored if the drone security is 'none'.<br/>
If the drone manager has a saved key for the drone, pass an empty string to use it<br/>


Result:<br/>
The drone manager will send an update of its [connection_state](#drone_manager-connection_state), if relevant<br/>


*Supported by <br/>*

- *SkyController 2*<br/>
- *SkyController 2P*<br/>


<br/>

<!-- drone_manager-forget-->
### <a name="drone_manager-forget">Forget a drone</a><br/>
> Forget a drone:

```c
deviceController->drone_manager->sendForget(deviceController->drone_manager, (char *)serial);
```

```objective_c
deviceController->drone_manager->sendForget(deviceController->drone_manager, (char *)serial);
```

```java
deviceController.getFeatureDroneManager().sendForget((String)serial);
```

Forget the given drone. If the drone is the selected one, the auto-selection will run again.<br/>


* serial (string): Serial number of the drone to forget.<br/>


Result:<br/>
If the drone was the active one, a new one will be autoselected, and [connection_state](#drone_manager-connection_state) update will be sent as needed. Otherwise, no answer will be sent from the drone manager<br/>


*Supported by <br/>*

- *SkyController 2*<br/>
- *SkyController 2P*<br/>


<br/>

