# Errors

<aside class="notice">This error section is stored in a separate file in `includes/_errors.md`. Slate allows you to optionally separate out your docs into many files...just save them to the `includes` folder and add them to the top of your `index.md`'s frontmatter. Files are included in the order listed.</aside>

## Configuration errors

Error Code | Name | Error message
---------- | ------- | --------
9000 	| UNKNOWN_LOCATION 	                                | The requested garden location does not exist 
9001 	| SENSOR_SERIAL_ALREADY_EXISTS 	                    | Request to create a sensor with duplicate serial number
9002 	| SENSOR_SERIAL_DOES_NOT_EXIST 	                    | Supplied sensor serial number does not exist or is not owned by me
9003 	| NOT_MY_SENSOR 	                                | Sensor assigned to a different account - cannot update
9004 	| NOT_MY_LOCATION 	                                | Location assigned to a different account
9005 	| NO_PLANT_AT_LOCATION 	                            | This feature requires a plant to be assigned to the location
9008 	| SENSOR_FIND_ERROR 	                            | The sensor does not exist or is not assigned to this location
9009 	| EVENT_ID_INVALID 	                                | One, or more, of the event ids were invalid
9010 	| LOCATION_FIND_ERROR 	                            | The location does not exist or is not assigned to this user
9011 	| UNKNOWN_DETECTOR_TYPE 	                        | The supplied detector type is invalid
9012 	| UNSUPPORTED_HISTORY_FORMAT 	                    | Invalid or unsupported history format
9014 	| UNSUPPORTED_RESOLUTION 	                        | Supplied sample resolution is not supported
9019 	| STALE_DATA_UPDATE_ERROR 	                        | Cannot update from supplied data as server data is newer
9020 	| INVALID_USER_DATA_VERSION 	                    | Cannot update as the supplied user data version EXCEEDS the server version
9021 	| LOCATION_ALREADY_EXISTS 	                        | Cannot create a location with the same location identifier
9022 	| UNKNOWN_ACTION 	                                | Sync could not work out what to do for an item
9023 	| EVENT_CREATE_ERROR 	                            | Attempt to create an event failed
9030 	| UNKNOWN_IMAGE_ACTION 	                            | Action not recognized, expected c, u or d
9031 	| MISSING_LOCATION_IDENTIFIER 	                    | Location identifier parameter missing
9032 	| GPS_DATA_MISSING 	                                | GPS data missing - cannot suggest plants
9035 	| RESET_ID_INVALID 	                                | Supplied id is invalid or not found
9036 	| RESET_ID_EXPIRED 	                                | Supplied id has expired
9037 	| RESET_ID_ALREADY_USED 	                        | Supplied id has been used
9038 	| GARDEN_LOCATION_NOT_ACTIVE 	                    | Requested suggestions for a location that does not have sensor associated
9039 	| NO_LOCATION_STATUS_PRESENT 	                    | Location for supplied location does not exist
9040 	| MISSING_PLANT_ASSIGNED_DATE 	                    | If setting a plant id you MUST supply an assigned date (or removed)
9041 	| INVALID_OR_MISSING_FROM_DATE 	                    | Expected a from date and was invalid or absent
9042 	| INVALID_OR_MISSING_TO_DATE 	                    | Expected a to date and was invalid or absent
9043 	| DEVICE_TIME_MISSING 	                            | Expected a mandatory datetime and was absent
9044 	| DEVICE_TIME_OUT_OF_RANGE 	                        | Device time out of acceptable synch with server time
9045 	| USER_SHARING_INVALID_SET_OPTION                   | The parameter can only be to_be_reminded, never_remind or shared
9046 	| USER_SHARING_INVALID_SET_OPTION_
==>     | FOR_CURRENT_STATE                                 | User sharing cannot be set to new state when in current state
9047 	| INVALID_UNKNOWN_OR_PRIVATE_LOCATION 	            | Either the identifier does not exist or is private
9048 	| REQUEST_DATE_SPAN_TOO_LARGE 	                    | The requested date span is too large
9049 	| INVALID_DATE_FORMAT 	                            | Could not parse the supplied date format use YYYY-MM-DD
9050 	| UNKNOWN_PLANT_SCIENCE_DATABASE 	                | The supplied library database identifier was not valid
9051 	| INVALID_GPS_DATA 	                                | The supplied gps data was invalid or out of range

## Common errors

Error Code | Name | Error message
---------- | ------- | --------
5000 	| UNSUPPORTED_API 	    | The requested version of this message is not supported
5001 	| NOT_YET_IMPLEMENTED 	| This feature has not yet been implemented
5003 	| NOT_ENOUGH_PARAMETERS | Invalid number of parameters
5003 	| DEPRECATED_IS_ERROR 	| This function is deprecated and cannot be called
5005 	| JSON_PARSE_ERROR 	    | Malformed JSON error
5006 	| S3_ID_MISSING 	    | S3_ID_MISSING
5007 	| S3_SECRET_MISSING 	| S3_SECRET_MISSING
5008 	| UNSUPPORTED_LANGUAGE 	| Unsupported language

## User errors

Error Code | Name | Error message
---------- | ------- | --------
8000 	| USER_ALREADY_EXISTS 	    | The user email already exists
8001 	| INVALID_EMAIL_FORMAT 	    | The supplied email is invalid
8002 	| INVALID_PASSWORD_FORMAT 	| The supplied password is invalid
8003 	| INVALID_USER 	            | The supplied user is invalid
8004 	| UNKNOWN_USER_EMAIL 	    | The supplied email is not recognised
8005 	| MISSING_USERNAME 	        | Username is missing
8006 	| USERNAME_EXISTS 	        | Username is already in system
8007 	| USERNAME_FORMAT_INVALID 	| Username is invalid
8008 	| UNKNOWN_OR_INVALID_USER 	| User is missing
