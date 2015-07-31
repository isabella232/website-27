#How to use

## Creating a project

To use the sdk, you will need to add the libraries to your project. To get the libraries, you can either download the released ones, or build your own with the sources (see [how to build the SDK](#how-to-build-the-sdk)).

### iOS

1. First, download the binaries : [SDK version 3.5 frameworks](https://github.com/Parrot-Developers/ARSDKBuildUtils/releases/download/ARSDK3_version_3_5/ARSDK3_iOS_3_5.zip)
2. Unzip it and rename it (for example rename it SDK3Frameworks).
3. Drag and drop the folder into your project
![alt text](../images/ios_drag_drop_frameworks.jpg "Drag and drop the framework folder")
4. Click on finish
![alt text](../images/ios_choose_copy.png "Click on finish")
5. You're all set !
![alt text](../images/ios_all_set.png "Let start coding !")

[Let's start coding](#start-coding) !

### Android

1. First, download the binaries : [SDK version 3.5 jars](https://github.com/Parrot-Developers/ARSDKBuildUtils/releases/download/ARSDK3_version_3_5/ARSDK3_Android_3_5.zip)
2. Unzip it.
3. Drag and drop the jars to your project libs folder. (Watch out, this will move the jars into your project).
   ![alt text](../images/android_drag_drop_jars.jpg "Drag and drop the jars")
4. Accept to move files
   ![alt text](../images/android_move_files.png "Click on Ok")
5. Accept the access to non-project files
   ![alt text](../images/android_non_project_file.png "Click on Ok")
6. Add permissions in your manifest file

7. Declare ARDiscoveryService in your manifest file

8. And finally load the native libraries in your Application or in the main activity (and every other activity that can be launched by an external intent).

<!-- Put code samples after the list to avoid going back to 1. -->

> Add permissions in your manifest file

```c
// Not needed in C
```

```objective_c
// Not needed in Objective C
```

```java
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.BLUETOOTH"/>
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_MULTICAST_STATE"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

> Declare ARDiscoveryService in your manifest file

```c
// Not needed in C
```

```objective_c
// Not needed in Objective C
```

```java
    <service android:name="com.parrot.arsdk.ardiscovery.ARDiscoveryService" />
```

> load the native libraries

```c
// Not needed in C
```

```objective_c
// Not needed in Objective C
```

```java
static
{
   try
   {
       System.loadLibrary("arsal");
       System.loadLibrary("arsal_android");
       System.loadLibrary("arnetworkal");
       System.loadLibrary("arnetworkal_android");
       System.loadLibrary("arnetwork");
       System.loadLibrary("arnetwork_android");
       System.loadLibrary("arcommands");
       System.loadLibrary("arcommands_android");
       System.loadLibrary("ardiscovery");
       System.loadLibrary("ardiscovery_android");
   }
   catch (Exception e)
   {
       Log.e(TAG, "Problem occured during native library loading", e);
   }
}
```
You're all set, [let's start coding](#start-coding) !


##Start coding

Here are the instruction about how to use the SDK to control the Bebop drone.

### Discover the drones

First of all, you will need to discover the drones around you. To do that, we will use the libARDiscovery.

> Start discovery:

```c
// Not yet available in pure C
```

```objective_c
- (void)startDiscovery
{
    [[ARDiscovery sharedInstance] start];
}
```

```java
private ARDiscoveryService mArdiscoveryService;
private ServiceConnection mArdiscoveryServiceConnection;

private void initDiscoveryService()
{
   // create the service connection
   if (mArdiscoveryServiceConnection == null)
   {
       mArdiscoveryServiceConnection = new ServiceConnection()
       {
           @Override
           public void onServiceConnected(ComponentName name, IBinder service)
           {
               mArdiscoveryService = ((ARDiscoveryService.LocalBinder) service).getService();

               startDiscovery();
           }

           @Override
           public void onServiceDisconnected(ComponentName name)
           {
               mArdiscoveryService = null;
           }
       };
   }

   if (mArdiscoveryService == null)
   {
       // if the discovery service doesn't exists, bind to it
       Intent i = new Intent(getApplicationContext(), ARDiscoveryService.class);
       getApplicationContext().bindService(i, mArdiscoveryServiceConnection, Context.BIND_AUTO_CREATE);
   }
   else
   {
       // if the discovery service already exists, start discovery
       startDiscovery();
   }
}

private void startDiscovery()
{
   if (mArdiscoveryService != null)
   {
       mArdiscoveryService.start();
   }
}
```

> The libARDiscovery will let you know when BLE and Wifi devices have been found on network:

```c
// Not yet available in pure C
```

```objective_c
- (void)registerReceivers
{
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(discoveryDidUpdateServices:) name:kARDiscoveryNotificationServicesDevicesListUpdated object:nil];
}

- (void)discoveryDidUpdateServices:(NSNotification *)notification
{
    NSArray *deviceList = [[notification userInfo] objectForKey:kARDiscoveryServicesList];

    // Do what you want with the device list (deviceList is an array of ARService*)
}
```

```java
// your class should implement ARDiscoveryServicesDevicesListUpdatedReceiverDelegate
private void registerReceivers()
{
    mArdiscoveryServicesDevicesListUpdatedReceiver = new ARDiscoveryServicesDevicesListUpdatedReceiver(this);
    LocalBroadcastManager localBroadcastMgr = LocalBroadcastManager.getInstance(getApplicationContext());
   localBroadcastMgr.registerReceiver(mArdiscoveryServicesDevicesListUpdatedReceiver, new IntentFilter(ARDiscoveryService.kARDiscoveryServiceNotificationServicesDevicesListUpdated));
}

@Override
public void onServicesDevicesListUpdated()
{
    Log.d(TAG, "onServicesDevicesListUpdated ...");

    if (mArdiscoveryService != null)
    {
        List<ARDiscoveryDeviceService> deviceList = mArdiscoveryService.getDeviceServicesArray();

        // Do what you want with the device list
    }
}
```

> Once you have the ARService you want to use, transform it into an ARDiscoveryDevice (you will need it at the [next step](#create_device_controller))

```c
// No BLE support in C, so we use the device IP/Port
// product should only be a wifi product (no Rolling Spider)
ARDiscovery_Device_t* createDiscoveryDevice(eARDISCOVERY_PRODUCT product, const char *name, const char *ip, int port)
{
    eARDISCOVERY_ERROR errorDiscovery = ARDISCOVERY_OK;
    ARDiscovery_Device_t *device = NULL;

    if (ip == NULL || port == 0)
    {
        fprintf(stderr, "Bad parameters");
        return device;
    }
    if (product < ARDISCOVERY_PRODUCT_NSNETSERVICE || product >= ARDISCOVERY_PRODUCT_BLESERVICE)
    {
        fprintf(stderr, "Bad product (not a wifi product)");
        return device;
    }

    device = ARDISCOVERY_Device_New(&errorDiscovery);

    if (errorDiscovery == ARDISCOVERY_OK)
    {
        errorDiscovery = ARDISCOVERY_Device_InitWifi (device, product, name, port);
    }

    if (errorDiscovery != ARDISCOVERY_OK)
    {
        ARDISCOVERY_Device_Delete(&device);
    }

    return device;
}
```

```objective_c
// this should be called in background
- (ARDISCOVERY_Device_t *)createDiscoveryDeviceWithService:(ARService*)service
{
    ARDISCOVERY_Device_t *device = NULL;

    eARDISCOVERY_ERROR errorDiscovery = ARDISCOVERY_OK;

    device = ARDISCOVERY_Device_New (&errorDiscovery);

    if (errorDiscovery == ARDISCOVERY_OK)
    {
        // init the discovery device
        if (service.product == ARDISCOVERY_PRODUCT_ARDRONE)
        {
            // need to resolve service to get the IP
            BOOL resolveSucceeded = [self resolveService:service];

            if (resolveSucceeded)
            {
                NSString *ip = [[ARDiscovery sharedInstance] convertNSNetServiceToIp:service];
                int port = (int)[(NSNetService *)service.service port];

                if (ip)
                {
                    // create a Wifi discovery device
                    errorDiscovery = ARDISCOVERY_Device_InitWifi (device, service.product, [service.name UTF8String], [ip UTF8String], port);
                }
                else
                {
                    NSLog(@"ip is null");
                    errorDiscovery = ARDISCOVERY_ERROR;
                }
            }
            else
            {
                NSLog(@"Resolve error");
                errorDiscovery = ARDISCOVERY_ERROR;
            }
        }

        if (errorDiscovery != ARDISCOVERY_OK)
        {
            ARDISCOVERY_Device_Delete(&device);
        }
    }

    return device;
}

#pragma mark resolveService
- (BOOL)resolveService:(ARService*)service
{
    BOOL retval = NO;
    _resolveSemaphore = dispatch_semaphore_create(0);
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(discoveryDidResolve:) name:kARDiscoveryNotificationServiceResolved object:nil];
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(discoveryDidNotResolve:) name:kARDiscoveryNotificationServiceNotResolved object:nil];

    [[ARDiscovery sharedInstance] resolveService:service];

    // this semaphore will be signaled in discoveryDidResolve and discoveryDidNotResolve
    dispatch_semaphore_wait(_resolveSemaphore, dispatch_time(DISPATCH_TIME_NOW, 10000000000));

    NSString *ip = [[ARDiscovery sharedInstance] convertNSNetServiceToIp:service];
    if (ip != nil)
    {
        retval = YES;
    }

    [[NSNotificationCenter defaultCenter] removeObserver:self name:kARDiscoveryNotificationServiceResolved object:nil];
    [[NSNotificationCenter defaultCenter] removeObserver:self name:kARDiscoveryNotificationServiceNotResolved object:nil];
    _resolveSemaphore = nil;
    return retval;
}

- (void)discoveryDidResolve:(NSNotification *)notification
{
    dispatch_semaphore_signal(_resolveSemaphore);
}

- (void)discoveryDidNotResolve:(NSNotification *)notification
{
    NSLog(@"Resolve failed");
    dispatch_semaphore_signal(_resolveSemaphore);
}
```

```java
    private ARDiscoveryDevice createDiscoveryDevice(ARDiscoveryDeviceService service)
    {
        ARDiscoveryDevice device = null;
        if ((service != null) &&
                (ARDISCOVERY_PRODUCT_ENUM.ARDISCOVERY_PRODUCT_ARDRONE.equals(ARDiscoveryService.getProductFromProductID(service.getProductID()))))
        {
            try
            {
                device = new ARDiscoveryDevice();

                ARDiscoveryDeviceNetService netDeviceService = (ARDiscoveryDeviceNetService) service.getDevice();

                device.initWifi(ARDISCOVERY_PRODUCT_ENUM.ARDISCOVERY_PRODUCT_ARDRONE, netDeviceService.getName(), netDeviceService.getIp(), netDeviceService.getPort());
            }
            catch (ARDiscoveryException e)
            {
                e.printStackTrace();
                Log.e(TAG, "Error: " + e.getError());
            }
        }

        return device;
    }
```

> Clean everything:

```c
// Not needed in pure C as we currently don't use ARDiscovery
```

```objective_c
- (void)unregisterReceivers
{
    [[NSNotificationCenter defaultCenter] removeObserver:self name:kARDiscoveryNotificationServicesDevicesListUpdated object:nil];
}

- (void)stopDiscovery
{
    [[ARDiscovery sharedInstance] stop];
}
```

```java
private void unregisterReceivers()
{
    LocalBroadcastManager localBroadcastMgr = LocalBroadcastManager.getInstance(getApplicationContext());

    localBroadcastMgr.unregisterReceiver(mArdiscoveryServicesDevicesListUpdatedReceiver);
}

private void closeServices()
{
    Log.d(TAG, "closeServices ...");

    if (mArdiscoveryService != null)
    {
        new Thread(new Runnable() {
            @Override
            public void run()
            {
                mArdiscoveryService.stop();

                getApplicationContext().unbindService(mArdiscoveryServiceConnection);
                mArdiscoveryService = null;
            }
        }).start();
    }
}
```

### <a name="create_device_controller">Setup a device controller</a>

The device controller is an object that will make the interface between the drone and you.

**After having [started](#start_device_controller) the device controller, you should receive all its states and settings through the command received callback.**

> Create the device controller:

```c
eARCONTROLLER_ERROR error = ARCONTROLLER_OK;
ARCONTROLLER_Device_t *deviceController = ARCONTROLLER_Device_New (discoveryDevice, &error);
```

```objective_c
eARCONTROLLER_ERROR error = ARCONTROLLER_OK;
ARCONTROLLER_Device_t *deviceController = ARCONTROLLER_Device_New (discoveryDevice, &error);
```

```java
try
{
    deviceController = new ARDeviceController (device);
}
catch (ARControllerException e)
{
    e.printStackTrace();
}
```

> Listen to the states changes:

```c
error = ARCONTROLLER_Device_AddStateChangedCallback(deviceController, stateChanged, NULL);

// called when the state of the device controller has changed
void stateChanged (eARCONTROLLER_DEVICE_STATE newState, eARCONTROLLER_ERROR error, void *customData)
{
    switch (newState)
    {
        case ARCONTROLLER_DEVICE_STATE_RUNNING:
            break;
        case ARCONTROLLER_DEVICE_STATE_STOPPED:
            break;
        case ARCONTROLLER_DEVICE_STATE_STARTING:
            break;
        case ARCONTROLLER_DEVICE_STATE_STOPPING:
            break;
        default:
            break;
    }
}
```

```objective_c
error = ARCONTROLLER_Device_AddStateChangedCallback(deviceController, stateChanged, (__bridge void *)(self));

// called when the state of the device controller has changed
void stateChanged (eARCONTROLLER_DEVICE_STATE newState, eARCONTROLLER_ERROR error, void *customData)
{
    // SELF_TYPE is the class name of self
    SELF_TYPE *selfCpy = (__bridge SELF_TYPE *)customData;

    switch (newState)
    {
        case ARCONTROLLER_DEVICE_STATE_RUNNING:
            break;
        case ARCONTROLLER_DEVICE_STATE_STOPPED:
            break;
        case ARCONTROLLER_DEVICE_STATE_STARTING:
            break;
        case ARCONTROLLER_DEVICE_STATE_STOPPING:
            break;
        default:
            break;
    }
}
```

```java
// your class should implement ARDeviceControllerListener
deviceController.addListener (this);

@Override
// called when the state of the device controller has changed
public void onStateChanged (ARDeviceController deviceController, ARCONTROLLER_DEVICE_STATE_ENUM newState, ARCONTROLLER_ERROR_ENUM error)
{
    switch (newState)
    {
        case ARCONTROLLER_DEVICE_STATE_RUNNING:
            break;
        case ARCONTROLLER_DEVICE_STATE_STOPPED:
            break;
        case ARCONTROLLER_DEVICE_STATE_STARTING:
            break;
        case ARCONTROLLER_DEVICE_STATE_STOPPING:
            break;

        default:
            break;
    }
}
```

> <a name="add_commands_receive_cb">Listen to the commands received from the drone</a> (example of the battery level received)

```c
error = ARCONTROLLER_Device_AddCommandReceivedCallback(deviceController, onCommandReceived, NULL);

// called when a command has been received from the drone
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (elementDictionary != NULL)
    {
        // if the command received is a battery state changed
        if (commandKey == ARCONTROLLER_DICTIONARY_KEY_COMMON_COMMONSTATE_BATTERYSTATECHANGED)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;

            // get the command received in the device controller
            HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
            if (element != NULL)
            {
                // get the value
                HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_COMMON_COMMONSTATE_BATTERYSTATECHANGED_PERCENT, arg);

                if (arg != NULL)
                {
                    uint8_t batteryLevel = arg->value.U8;
                    // do what you want with the battery level
                }
            }
        }
        // else if (commandKey == THE COMMAND YOU ARE INTERESTED IN)
    }
}
```

```objective_c
error = ARCONTROLLER_Device_AddCommandReceivedCallback(deviceController, onCommandReceived, (__bridge void *)(self));

// called when a command has been received from the drone
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    SELF_TYPE *selfCpy = (__bridge SELF_TYPE *)customData;

    if (elementDictionary != NULL)
    {
        // if the command received is a battery state changed
        if (commandKey == ARCONTROLLER_DICTIONARY_KEY_COMMON_COMMONSTATE_BATTERYSTATECHANGED)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;

            // get the command received in the device controller
            HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
            if (element != NULL)
            {
                // get the value
                HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_COMMON_COMMONSTATE_BATTERYSTATECHANGED_PERCENT, arg);

                if (arg != NULL)
                {
                    uint8_t batteryLevel = arg->value.U8;
                    // do what you want with the battery level
                }
            }
        }
        // else if (commandKey == THE COMMAND YOU ARE INTERESTED IN)
    }
}
```

```java
// your class should implement ARDeviceControllerListener
deviceController.addListener (this);

@Override
// called when a command has been received from the drone
public void onCommandReceived(ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary)
{
    if (elementDictionary != null)
    {
        // if the command received is a battery state changed
        if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_COMMON_COMMONSTATE_BATTERYSTATECHANGED)
        {
            ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);

            if (args != null)
            {
                Integer batValue = (Integer) args.get(ARFeatureCommon.ARCONTROLLER_DICTIONARY_KEY_COMMON_COMMONSTATE_BATTERYSTATECHANGED_PERCENT);

                // do what you want with the battery level
            }
        }
    }
    else
    {
        Log.e(TAG, "elementDictionary is null");
    }
}
```

> <a name="bebop_add_video_receive_cb">Listen to the video stream received from the drone</a>

```c
error = ARCONTROLLER_Device_SetVideoReceiveCallback (deviceController, didReceiveFrameCallback, NULL, NULL);

void didReceiveFrameCallback (ARCONTROLLER_Frame_t *frame, void *customData)
{
    // display the frame
}
```

```objective_c
error = ARCONTROLLER_Device_SetVideoReceiveCallback (deviceController, didReceiveFrameCallback, NULL, (__bridge void *)(self));

void didReceiveFrameCallback (ARCONTROLLER_Frame_t *frame, void *customData)
{
    SELF_TYPE *selfCpy = (__bridge SELF_TYPE *)customData;
    // display the frame
}
```

```java
// your class should implement ARDeviceControllerStreamListener
deviceController.addStreamListener(this);

@Override
public void onFrameReceived(ARDeviceController deviceController, ARFrame frame)
{
    // display the frame
}

@Override
public void onFrameTimeout(ARDeviceController deviceController)
{
}
```

> <a name="start_device_controller">Finally, starts the device controller (after that call, the callback you set in ARCONTROLLER_Device_AddStateChangedCallback should be called)</a>.

```c
error = ARCONTROLLER_Device_Start (deviceController);
```

```objective_c
error = ARCONTROLLER_Device_Start (deviceController);
if (error == ARCONTROLLER_OK)
{
    _deviceController = deviceController;
}
```

```java
ARCONTROLLER_ERROR_ENUM error = deviceController.start();
```

> Cleanup when done:

```c
// This function will wait until the device controller is stopped
void deleteDeviceController(ARCONTROLLER_Device_t *deviceController)
{
    if (deviceController == NULL)
    {
        return;
    }

    eARCONTROLLER_ERROR error = ARCONTROLLER_OK;

    eARCONTROLLER_DEVICE_STATE state = ARCONTROLLER_Device_GetState(deviceController, &error);
    if ((error == ARCONTROLLER_OK) && (state != ARCONTROLLER_DEVICE_STATE_STOPPED))
    {
        // after that, stateChanged should be called soon
        error = ARCONTROLLER_Device_Stop (_deviceController);

        if (error == ARCONTROLLER_OK)
        {
            sem_wait(&someSemaphore);
        }
        else
        {
            fprintf(stderr, "- error :%s", ARCONTROLLER_Error_ToString(error));
        }
    }

    // once the device controller is stopped, we can delete it
    ARCONTROLLER_Device_Delete(&deviceController);
}

// dont forget to create the semaphore and to sem_post it in the case ARCONTROLLER_DEVICE_STATE_STOPPED of the stateChanged function
// DO NOT CALL ARCONTROLLER_Device_Delete FROM THE stateChanged FUNCTION !
```

```objective_c
- (void)deleteDeviceController
{
    // in background
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
        eARCONTROLLER_ERROR error = ARCONTROLLER_OK;

        // if the device controller is not stopped, stop it
        eARCONTROLLER_DEVICE_STATE state = ARCONTROLLER_Device_GetState(_deviceController, &error);
        if ((error == ARCONTROLLER_OK) && (state != ARCONTROLLER_DEVICE_STATE_STOPPED))
        {
            // after that, stateChanged should be called soon
            error = ARCONTROLLER_Device_Stop (_deviceController);

            if (error == ARCONTROLLER_OK)
            {
                dispatch_semaphore_wait(_stateSem, DISPATCH_TIME_FOREVER);
            }
            else
            {
                NSLog(@"- error :%s", ARCONTROLLER_Error_ToString(error));
            }
        }

        // once the device controller is stopped, we can delete it
        if (_deviceController != NULL)
        {
            ARCONTROLLER_Device_Delete(&_deviceController);
        }
    });
}

// dont forget to add dispatch_semaphore_signal(pilotingViewController.stateSem); in the case ARCONTROLLER_DEVICE_STATE_STOPPED of the stateChanged function
```

```java
ARCONTROLLER_ERROR_ENUM error = deviceController.stop();
```

### Taking off
In order to make your drone take off you will need to ensure that its flying status is landed (even if you can send take off commands anyway, it just won't take of if it not in landed state). <br/>
Then, you can send the take off command. <br/>
In response, your drone will send you a state change (if it has taken off) : State *Landed* -> State *TakingOff* -> State *Hovering* (or *Flying*).

> Take off


```c
eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE getFlyingState(ARCONTROLLER_Device_t *deviceController)
{
    eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE flyingState = ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_MAX;
    eARCONTROLLER_ERROR error;
    ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary = ARCONTROLLER_ARDrone3_GetCommandElements(deviceController->aRDrone3, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED, &error);
    if (error == ARCONTROLLER_OK && elementDictionary != NULL)
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            // Get the value
            HASH_FIND_STR(element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                // Enums are stored as I32
                flyingState = arg->value.I32;
            }
        }
    }
    return flyingState
}

void takeOff(ARCONTROLLER_Device_t *deviceController)
{
    if (deviceController == NULL)
    {
        return;
    }
    if (getFlyingState(deviceController) == ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_LANDED)
    {
        deviceController->aRDrone3->sendPilotingTakeOff(deviceController->aRDrone3);
    }
}
```

```objective_c
- (eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE)getFlyingState {

    eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE flyingState = ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_MAX;

    eARCONTROLLER_ERROR error;
    // get the current flying state description
    ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary = ARCONTROLLER_ARDrone3_GetCommandElements(_deviceController->aRDrone3, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED, &error);
    if (error == ARCONTROLLER_OK && elementDictionary != NULL)
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            // get the value
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);

            if (arg != NULL)
            {
                // Enums are I32
                flyingState = arg->value.I32;
            }
        }
    }

    return flyingState;
}

- (void)takeoff
{
    if ([self getFlyingState] == ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_LANDED)
    {
        _deviceController->aRDrone3->sendPilotingTakeOff(_deviceController->aRDrone3);
    }
}
```

```java
private ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM getPilotingState()
{
    ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM flyingState = ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM.eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_UNKNOWN_ENUM_VALUE;
    if (deviceController != null)
    {
        try
        {
            ARControllerDictionary dict = deviceController.getCommandElements(ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED);
            if (dict != null)
            {
                ARControllerArgumentDictionary<Object> args = dict.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
                if (args != null)
                {
                    Integer flyingStateInt = (Integer) args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE);
                    flyingState = ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM.getFromValue(flyingStateInt);
                }
            }
        }
        catch (ARControllerException e)
        {
            e.printStackTrace();
        }

        return flyingState;
    }
}

private void takeoff()
{
    if (ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM.ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_LANDED.equals(getPilotingState()))
    {
        ARCONTROLLER_ERROR_ENUM error = deviceController.getFeatureARDrone3().sendPilotingTakeOff();

        if (!error.equals(ARCONTROLLER_ERROR_ENUM.ARCONTROLLER_OK))
        {
            ARSALPrint.e(TAG, "Error while sending take off : " + error);
        }
    }
}
```

> The drone changes its state. Flying state should be ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_TAKINGOFF, then ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_HOVERING or ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_FLYING.


```c
// called when a command has been received from the drone
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    // if the command received is a flying state changed
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;

        // get the command received in the device controller
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            // get the value
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);

            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE flyingState = arg->value.I32;
            }
        }
    }
}
```

```objective_c
// called when a command has been received from the drone
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    // if the command received is a flying state changed
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;

        // get the command received in the device controller
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            // get the value
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);

            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE flyingState = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived(ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary)
{
    if (elementDictionary != null)
    {
        if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED)
        {
            ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
            if (args != null)
            {
                Integer flyingStateInt = (Integer) args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE);
                ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM flyingState = ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM.getFromValue(flyingStateInt);
            }
        }
    }
    else
    {
        Log.e(TAG, "elementDictionary is null");
    }
}
```

After that, you can start piloting your drone.

### Landing

When you're done flying, you will need to land. This is how you do it: simply send the landing command.

```c
void land(ARCONTROLLER_Device_t *deviceController)
{
    if (deviceController == NULL)
    {
        return;
    }
    eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE flyingState = getFlyingState(deviceController);
    if (flyingState == ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_FLYING || flyingState == ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_HOVERING)
    {
        deviceController->aRDrone3->sendPilotingLanding(deviceController->aRDrone3);
    }
}
```

```objective_c
- (void)land
{
    eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE flyingState = [self getFlyingState];
    if (flyingState == ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_FLYING || flyingState == ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_HOVERING)
    {
        _deviceController->aRDrone3->sendPilotingLanding(_deviceController->aRDrone3);
    }
}
```

```java
private void land()
{
    ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM flyingState = getPilotingState();
    if (ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM.ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_HOVERING.equals(flyingState) ||
            ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM.ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_HOVERING.equals(flyingState))
    {
        ARCONTROLLER_ERROR_ENUM error = deviceController.getFeatureARDrone3().sendPilotingLanding();

        if (!error.equals(ARCONTROLLER_ERROR_ENUM.ARCONTROLLER_OK))
        {
            ARSALPrint.e(TAG, "Error while sending take off : " + error);
        }
    }
}
```

### Piloting

The Bebop drone is piloted with angles. And the way you specifie these angles are in percentage of the max angle. <br/>
The piloting command is automatically sent by the device controller each 25ms. <br/>
If a disconnection appears, or if the commands are not received, the Bebop will set all its angle to 0 after 500ms for security reasons.

In the piloting command there are 6 params:

* Flag: 1 if the roll and pitch values should be taken in consideration. 0 otherwise
* Roll: roll angle percentage (from -100 to 100). Negative values go left, positive go right.
* Pitch: pitch angle percentage (from -100 to 100). Negative values go backward, positive go forward.
* Yaw: yaw speed percentage (calculated on the max rotation speed)(from -100 to 100). Negative values go left, positive go right.
* Gaz: gaz speed percentage (calculated on the max vertical speed)(from -100 to 100). Negative values go down, positive go up.

Here is how you set the piloting angles:

> Make the drone moves forward (50% of its max angle)

```c
deviceController->aRDrone3->setPilotingPCMDFlag(deviceController->aRDrone3, 1);
deviceController->aRDrone3->setPilotingPCMDPitch(deviceController->aRDrone3, 50);
```

```objective_c
_deviceController->aRDrone3->setPilotingPCMDFlag(_deviceController->aRDrone3, 1);
_deviceController->aRDrone3->setPilotingPCMDPitch(_deviceController->aRDrone3, 50);
```

```java
deviceController.getFeatureARDrone3().setPilotingPCMDFlag((byte) 1);
deviceController.getFeatureARDrone3().setPilotingPCMDPitch((byte) 50);
```

> Make the drone rotate to the right (50% of its max rotation speed)

```c
deviceController->aRDrone3->setPilotingPCMDYaw(deviceController->aRDrone3, 50);
```

```objective_c
_deviceController->aRDrone3->setPilotingPCMDYaw(_deviceController->aRDrone3, 50);
```

```java
deviceController.getFeatureARDrone3().setPilotingPCMDYaw((byte) 50);
```

### Start video streaming

To start the video stream, you will need to send a command to the Bebop. When the frame are received, the callback [you set at the initialisation of your device controller](#bebop_add_video_receive_cb) will be called.

> Start video stream

```c
deviceController->aRDrone3->sendMediaStreamingVideoEnable(deviceController->aRDrone3, 1);
```

```objective_c
_deviceController->aRDrone3->sendMediaStreamingVideoEnable(_deviceController- aRDrone3, 1);
```

```java
deviceController.getFeatureARDrone3().sendMediaStreamingVideoEnable((byte)1);
```

> Stop video stream

```c
deviceController->aRDrone3->sendMediaStreamingVideoEnable(deviceController->aRDrone3, 0);
```

```objective_c
_deviceController->aRDrone3->sendMediaStreamingVideoEnable(_deviceController->aRDrone3, 0);
```

```java
deviceController.getFeatureARDrone3().sendMediaStreamingVideoEnable((byte)0);
```

### Taking a picture

The drone lets you take pictures. 

> Take a picture

```c
deviceController->aRDrone3->sendMediaRecordPicture(deviceController->aRDrone3, 0);
```

```objective_c
_deviceController->aRDrone3->sendMediaRecordPicture(_deviceController->aRDrone3, 0);
```

```java
deviceController.getFeatureARDrone3().sendMediaRecordPicture((byte)0);
```

### Download pictures and videos

Once the picture or video has been taken, the Bebop stores it on its internal memory. Pictures are stored in `internal_000/Bebop_Drone/media/`. <br/>
To get the pictures, you can:

* simply do a ftp request:
    * port: 21
    * login: "anonymous"
    * no password
* use libARDataTransfer which provides an abstraction of the ftp

**Please note that libARController is not including the data transfer for the moment, it will certainly in the future so this process will be simplified**

Here is how to do it with libARDataTransfer.

libARDataTransfer lets you get a list of all stored medias quite quickly. It also provides you a way to enrich the list of medias with their thumbnails. It also gives you the ability to download the media.

<div></div>
First, you will need to create the data transfer manager

> Declare vars

```objective_c
#define DEVICE_PORT     21
#define MEDIA_FOLDER    "internal_000"

@property (nonatomic, assign) ARSAL_Thread_t threadRetreiveAllMedias;   // the thread that will do the media retrieving
@property (nonatomic, assign) ARSAL_Thread_t threadGetThumbnails;       // the thread that will download the thumbnails
@property (nonatomic, assign) ARSAL_Thread_t threadMediasDownloader;    // the thread that will download medias

@property (nonatomic, assign) ARDATATRANSFER_Manager_t *manager;        // the data transfer manager
@property (nonatomic, assign) ARUTILS_Manager_t *ftpListManager;        // an ftp that will do the list
@property (nonatomic, assign) ARUTILS_Manager_t *ftpQueueManager;       // an ftp that will do the download
```

```java
private static final int DEVICE_PORT = 21;
private static final String MEDIA_FOLDER = "internal_000";

private AsyncTask<Void, Float, ArrayList<ARMediaObject>> getMediaAsyncTask;
private AsyncTask<Void, Float, Void> getThumbnailAsyncTask;
private Handler mFileTransferThreadHandler;
private HandlerThread mFileTransferThread;
private boolean isRunning = false;
private boolean isDownloading = false;
private final Object lock = new Object();

private ARDataTransferManager dataTransferManager;
private ARUtilsManager ftpListManager;
private ARUtilsManager ftpQueueManager;
```

> Create the data transfer manager

```objective_c
- (void)createDataTransferManager
{
    NSString *productIP = @"192.168.42.1";  // TODO: get this address from libARController
    
    eARDATATRANSFER_ERROR result = ARDATATRANSFER_OK;
    _manager = ARDATATRANSFER_Manager_New(&result);
    
    if (result == ARDATATRANSFER_OK)
    {
        eARUTILS_ERROR ftpError = ARUTILS_OK;
        _ftpListManager = ARUTILS_Manager_New(&ftpError);
        if(ftpError == ARUTILS_OK)
        {
            _ftpQueueManager = ARUTILS_Manager_New(&ftpError);
        }
        
        if(ftpError == ARUTILS_OK)
        {
            ftpError = ARUTILS_Manager_InitWifiFtp(_ftpListManager, [productIP UTF8String], DEVICE_PORT, ARUTILS_FTP_ANONYMOUS, "");
        }
        
        if(ftpError == ARUTILS_OK)
        {
            ftpError = ARUTILS_Manager_InitWifiFtp(_ftpQueueManager, [productIP UTF8String], DEVICE_PORT, ARUTILS_FTP_ANONYMOUS, "");
        }
        
        if(ftpError != ARUTILS_OK)
        {
            result = ARDATATRANSFER_ERROR_FTP;
        }
    }
    // NO ELSE
    
    if (result == ARDATATRANSFER_OK)
    {
        NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
        NSString *path = [paths lastObject];
        
        result = ARDATATRANSFER_MediasDownloader_New(_manager, _ftpListManager, _ftpQueueManager, MEDIA_FOLDER, [path UTF8String]);
    }
}
```

```java
private void createDataTransferManager() {
   String productIP = "192.168.42.1";  // TODO: get this address from libARController

   ARDATATRANSFER_ERROR_ENUM result = ARDATATRANSFER_ERROR_ENUM.ARDATATRANSFER_OK;
   try
   {
       dataTransferManager = new ARDataTransferManager();
   }
   catch (ARDataTransferException e)
   {
       e.printStackTrace();
       result = ARDATATRANSFER_ERROR_ENUM.ARDATATRANSFER_ERROR;
   }

   if (result == ARDATATRANSFER_ERROR_ENUM.ARDATATRANSFER_OK)
   {
       try
       {
           ftpListManager = new ARUtilsManager();
           ftpQueueManager = new ARUtilsManager();

           ftpListManager.initWifiFtp(productIP, DEVICE_PORT, ARUtilsFtpConnection.FTP_ANONYMOUS, "");
           ftpQueueManager.initWifiFtp(productIP, DEVICE_PORT, ARUtilsFtpConnection.FTP_ANONYMOUS, "");
       }
       catch (ARUtilsException e)
       {
           e.printStackTrace();
           result = ARDATATRANSFER_ERROR_ENUM.ARDATATRANSFER_ERROR_FTP;
       }
   }
   if (result == ARDATATRANSFER_ERROR_ENUM.ARDATATRANSFER_OK)
   {
       // direct to external directory
       String externalDirectory = Environment.getExternalStorageDirectory().toString().concat("/ARSDKMedias/");
       try
       {
           dataTransferManager.getARDataTransferMediasDownloader().createMediasDownloader(ftpListManager, ftpQueueManager, MEDIA_FOLDER, externalDirectory);
       }
       catch (ARDataTransferException e)
       {
           e.printStackTrace();
           result = e.getError();
       }
   }

   if (result == ARDATATRANSFER_ERROR_ENUM.ARDATATRANSFER_OK)
   {
       // create a thread for the download to run the download runnable
       mFileTransferThread = new HandlerThread("FileTransferThread");
       mFileTransferThread.start();
       mFileTransferThreadHandler = new Handler(mFileTransferThread.getLooper());
   }

   if (result != ARDATATRANSFER_ERROR_ENUM.ARDATATRANSFER_OK)
   {
       // clean up here because an error happened
   }
}
```

<div></div>
Then, we can get the list of all medias on the Bebop (without their thumbnail). This operation is quite quick.

> Get the list of the medias 

```objective_c
- (void)startMediaListThread
{
    // first retrieve Medias without their thumbnails
    ARSAL_Thread_Create(&_threadRetreiveAllMedias, ARMediaStorage_retreiveAllMediasAsync, (__bridge void *)self);
}

static void* ARMediaStorage_retreiveAllMediasAsync(void* arg)
{
    PilotingViewController *self = (__bridge PilotingViewController *)(arg);
    [self getAllMediaAsync];
    return NULL;
}

- (void)getAllMediaAsync
{
    eARDATATRANSFER_ERROR result = ARDATATRANSFER_OK;
    int mediaListCount = 0;
    
    if (result == ARDATATRANSFER_OK)
    {
        mediaListCount = ARDATATRANSFER_MediasDownloader_GetAvailableMediasSync(_manager,0,&result);
        if (result == ARDATATRANSFER_OK)
        {
            for (int i = 0 ; i < mediaListCount && result == ARDATATRANSFER_OK; i++)
            {
                ARDATATRANSFER_Media_t * mediaObject = ARDATATRANSFER_MediasDownloader_GetAvailableMediaAtIndex(_manager, i, &result);
                NSLog(@"Media %i : %s", i, mediaObject->name);
                // Do what you want with this mediaObject
            }
        }
    }
}
```

```java
private void fetchMediasList() {
   if (getMediaAsyncTask == null)
   {
       getMediaAsyncTask = new AsyncTask<Void, Float, ArrayList<ARMediaObject>>()
       {
           @Override
           protected ArrayList<ARMediaObject> doInBackground(Void... params)
           {
               ArrayList<ARMediaObject> mediaList = null;
               synchronized (lock)
               {
                   ARDataTransferMediasDownloader mediasDownloader = null;
                   if (dataTransferManager != null)
                   {
                       mediasDownloader = dataTransferManager.getARDataTransferMediasDownloader();
                   }

                   if (mediasDownloader != null)
                   {
                       try
                       {
                           int mediaListCount = mediasDownloader.getAvailableMediasSync(false);
                           mediaList = new ArrayList<>(mediaListCount);
                           for (int i = 0; i < mediaListCount; i++)
                           {
                               ARDataTransferMedia currentMedia = mediasDownloader.getAvailableMediaAtIndex(i);
                               final ARMediaObject currentARMediaObject = new ARMediaObject();
                               currentARMediaObject.updateDataTransferMedia(getResources(), currentMedia);
                               mediaList.add(currentARMediaObject);
                           }
                       }
                       catch (ARDataTransferException e)
                       {
                           e.printStackTrace();
                           mediaList = null;
                       }
                   }
               }

               return mediaList;
           }

           @Override
           protected void onPostExecute(ArrayList<ARMediaObject> arMediaObjects)
           {
                // Do what you want with the list of media object
           }
       };
   }

   if (getMediaAsyncTask.getStatus() != AsyncTask.Status.RUNNING) {
       getMediaAsyncTask.execute();
   }
}
```

<div></div>

Once the list is received, we can start downloading the thumbnail (not needed if you don't display thumbnails).

> Download thumbnails

```objective_c
- (void)startMediaThumbnailDownloadThread
{
    // first retrieve Medias without their thumbnails
    ARSAL_Thread_Create(&_threadGetThumbnails, ARMediaStorage_retreiveMediaThumbnailsSync, (__bridge void *)self);
}

static void* ARMediaStorage_retreiveMediaThumbnailsSync(void* arg)
{
    PilotingViewController *self = (__bridge PilotingViewController *)(arg);
    [self downloadThumbnails];
    return NULL;
}

- (void)downloadThumbnails
{
    ARDATATRANSFER_MediasDownloader_GetAvailableMediasAsync(_manager, availableMediaCallback, (__bridge void *)self);
}

void availableMediaCallback (void* arg, ARDATATRANSFER_Media_t *media, int index)
{
    if (NULL != arg)
    {
        PilotingViewController *self = (__bridge PilotingViewController *)(arg);  
        // you can alternatively call updateThumbnailWithARDATATRANSFER_Media_t if you use the ARMediaObjectDelegate
        UIImage *newThumbnail = [UIImage imageWithData:[NSData dataWithBytes:media->thumbnail length:media->thumbnailSize]];
        // Do what you want with the image
    }
}
```

```java
private void fetchThumbnails() {
   if (getThumbnailAsyncTask == null)
   {
       getThumbnailAsyncTask = new AsyncTask<Void, Float, Void>()
       {
           @Override
           protected Void doInBackground(Void... params)
           {
               synchronized (lock)
               {
                   ARDataTransferMediasDownloader mediasDownloader = null;
                   if (dataTransferManager != null)
                   {
                       mediasDownloader = dataTransferManager.getARDataTransferMediasDownloader();
                   }

                   if (mediasDownloader != null)
                   {
                       try
                       {
                           // availableMediaListener is a ARDataTransferMediasDownloaderAvailableMediaListener (you can pass YourActivity.this if YourActivity implements this interface)
                           mediasDownloader.getAvailableMediasAsync(availableMediaListener, null);
                       }
                       catch (ARDataTransferException e)
                       {
                           e.printStackTrace();
                       }
                   }
               }
               return null;
           }

           @Override
           protected void onPostExecute(Void param)
           {
               adapter.notifyDataSetChanged();
           }
       };
   }

   if (getThumbnailAsyncTask.getStatus() != AsyncTask.Status.RUNNING) {
       getThumbnailAsyncTask.execute();
   }
}

@Override
public void didMediaAvailable(Object arg, final ARDataTransferMedia media, final int index)
{
   runOnUiThread(new Runnable()
   {
       @Override
       public void run()
       {
           ARMediaObject mediaObject = getMediaAtIndex(index);
           if (mediaObject != null)
           {
               mediaObject.updateThumbnailWithDataTransferMedia(getResources(), media);
               // after that, you can retrieve the thumbnail through mediaObject.getThumbnail()
           }
       }
   });
}

```

<div></div>

Next step is to download the medias.

> Download medias

```objective_c
- (void)downloadMedias
{
    eARDATATRANSFER_ERROR result = ARDATATRANSFER_OK;
    int mediasToDlCount = [self getMediaToDlCount];
    for (int i = 0 ; i < mediasToDlCount && result == ARDATATRANSFER_OK; i++)
    {
        ARDATATRANSFER_Media_t *media = [self getMediaToDownload:i];
        result = ARDATATRANSFER_MediasDownloader_AddMediaToQueue(_manager, media, medias_downloader_progress_callback, (__bridge void *)(self), medias_downloader_completion_callback,(__bridge void*)self);
    }
    
    if (result == ARDATATRANSFER_OK)
    {
        if (_threadMediasDownloader == NULL)
        {
            // if not already started, start download thread in background
            ARSAL_Thread_Create(&_threadMediasDownloader, ARDATATRANSFER_MediasDownloader_QueueThreadRun, _manager);
        }
    }
}
void medias_downloader_progress_callback(void* arg, ARDATATRANSFER_Media_t *media, float percent)
{
    // the media is downloading
}

void medias_downloader_completion_callback(void* arg, ARDATATRANSFER_Media_t *media, eARDATATRANSFER_ERROR error)
{
    // the media is downloaded
}
```

```java
/**
* Add the medias to the transfer queue and, if needed, start the queue
* @param mediaToDl list of media index to download
*/
private void downloadMedias(ArrayList<Integer> mediaToDl)
{
   ARDataTransferMediasDownloader mediasDownloader = null;
   if (dataTransferManager != null)
   {
       mediasDownloader = dataTransferManager.getARDataTransferMediasDownloader();
   }

   if (mediasDownloader != null)
   {
       for (int i = 0; i < mediaToDl.size(); i++)
       {
           int mediaIndex = mediaToDl.get(i);
           ARDataTransferMedia mediaObject = null;
           try
           {
               mediaObject = dataTransferManager.getARDataTransferMediasDownloader().getAvailableMediaAtIndex(mediaIndex);
           }
           catch (ARDataTransferException e)
           {
               e.printStackTrace();
           }

           if (mediaObject != null)
           {
               try
               {
                   mediasDownloader.addMediaToQueue(mediaObject, progressListener, null, completeListener, null);
               }
               catch (ARDataTransferException e)
               {
                   e.printStackTrace();
               }
           }
       }

       if (!isRunning)
       {
           isRunning = true;
           Runnable downloaderQueueRunnable = mediasDownloader.getDownloaderQueueRunnable();
           mFileTransferThreadHandler.post(downloaderQueueRunnable);
       }
   }
   isDownloading = true;
}

@Override
public void didMediaComplete(Object arg, ARDataTransferMedia media, ARDATATRANSFER_ERROR_ENUM error)
{
    // the media is downloaded
}

@Override
public void didMediaProgress(Object arg, ARDataTransferMedia media, float percent)
{
    // the media is downloading
}
```

> Stop downloading medias

```objective_c
- (void)cancelCurrentDownload {
    if (_threadMediasDownloader != NULL)
    {
        ARDATATRANSFER_MediasDownloader_CancelQueueThread(_manager);
        
        ARSAL_Thread_Join(_threadMediasDownloader, NULL);
        ARSAL_Thread_Destroy(&_threadMediasDownloader);
        _threadMediasDownloader = NULL;
    }
}
```

```java
private void cancelCurrentDownload()
{
   dataTransferManager.getARDataTransferMediasDownloader().cancelQueueThread();
   isDownloading = false;
   isRunning = false;
}
```

<div></div>

When you don't need the data transfer anymore, don't forget to clean everything

> Clean

```objective_c
- (void)clean
{
    if (_threadRetreiveAllMedias != NULL)
    {
        ARDATATRANSFER_MediasDownloader_CancelGetAvailableMedias(_manager);
        
        ARSAL_Thread_Join(_threadRetreiveAllMedias, NULL);
        ARSAL_Thread_Destroy(&_threadRetreiveAllMedias);
        _threadRetreiveAllMedias = NULL;
    }
    
    if (_threadGetThumbnails != NULL)
    {
        ARDATATRANSFER_MediasDownloader_CancelGetAvailableMedias(_manager);
        
        ARSAL_Thread_Join(_threadGetThumbnails, NULL);
        ARSAL_Thread_Destroy(&_threadGetThumbnails);
        _threadGetThumbnails = NULL;
    }
    
    if (_threadMediasDownloader != NULL)
    {
        ARDATATRANSFER_MediasDownloader_CancelQueueThread(_manager);
        
        ARSAL_Thread_Join(_threadMediasDownloader, NULL);
        ARSAL_Thread_Destroy(&_threadMediasDownloader);
        _threadMediasDownloader = NULL;
    }
    
    ARDATATRANSFER_MediasDownloader_Delete(_manager);
    
    ARUTILS_Manager_CloseWifiFtp(_ftpListManager);
    ARUTILS_Manager_CloseWifiFtp(_ftpQueueManager);
    
    ARUTILS_Manager_Delete(&_ftpListManager);
    ARUTILS_Manager_Delete(&_ftpQueueManager);
    ARDATATRANSFER_Manager_Delete(&_manager);
}
```

```java
private void clean()
{
   new Thread(new Runnable()
   {
       @Override
       public void run()
       {
           cancelCurrentDownload();

           if (dataTransferManager != null)
           {
               dataTransferManager.getARDataTransferMediasDownloader().cancelGetAvailableMedias();
           }
           if (getMediaAsyncTask != null && getMediaAsyncTask.getStatus() == AsyncTask.Status.RUNNING)
           {
               synchronized (lock)
               {
                   getMediaAsyncTask.cancel(true);
               }
           }
           if (getThumbnailAsyncTask != null && getThumbnailAsyncTask.getStatus() == AsyncTask.Status.RUNNING)
           {
               synchronized (lock)
               {
                   getThumbnailAsyncTask.cancel(true);
               }
           }

           if (ftpListManager != null)
           {
               ftpListManager.closeWifiFtp();

               ftpListManager.dispose();
               ftpListManager = null;
           }
           if (ftpQueueManager != null)
           {
               ftpQueueManager.closeWifiFtp();
               ftpQueueManager.dispose();
               ftpQueueManager = null;
           }
           if (dataTransferManager != null)
           {
               dataTransferManager.dispose();
               dataTransferManager = null;
           }

           if (mFileTransferThread != null)
           {
               mFileTransferThread.quit();
               mFileTransferThread = null;
           }
       }
   }).start();
}
```