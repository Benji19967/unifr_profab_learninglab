# Shadow play

## Outline

### Hardware

- Stepper motor (connected to battery pack)
    - 3V powerful enough?
- Light (with builtin Arduino)
- External battery pack (can power 2 devices)
- USB Camera (initial mount with elastics)
- Pin or magnets (to attach paper to rotating 3D printed piece)
- Arduino ESP32 (coonected to battery pack)
    - Connect motor via breadboard

- 3D printed:
    - Base (flat) (maybe has holes to attach camera)
        - Rods to attach to current top layer of robot
    - Light and motor casing
    - Rotating piece (attached to motor)
    - Optional: parts to reduce angle of emittance of light

### Software

- ROS package for camera
    - Stream images to Node-RED for debugging
    - Send images from Raspberry Pi to laptop for processing
- ROS for localization/mapping and path planning (camera and/or lidar)
- UI
    - Control light
        - Arduino to ROS or MQTT
    - Control motor
        - Arduino to ROS or MQTT
    - Optional: display camera output

### Functionality

- Light
    - Turn ON / OFF
    - Adjust light sensitivity
- Motor
    - Adjust rotation speed
- Robot
    - Locate actress
    - Turn towards actress and approach until X meters away
    - Move in front of actress
- Optional: coordinate the above intelligently
