# NAO Humanoid Robot Project (Webots R2025a)

## Overview
This project was developed using the NAO humanoid robot in Webots R2025a.  
It demonstrates basic motion control, choreography (dance routine), and simple state-based behavior using Python controllers and prebuilt motion files.

---

## Project Type
- Humanoid Robot Dance Routine
- Motion sequencing using Webots `.motion` files

---

## Robot Used
- NAO Humanoid Robot (from Webots NAO template)

---

## Software Used
- Webots R2025a
- Python (Webots Controller API)

---

## Motion Files Used
The following prebuilt motion files were used:

- Forwards.motion
- Forwards50.motion
- Backwards.motion
- SideStepLeft.motion
- SideStepRight.motion
- TurnLeft40.motion
- TurnLeft60.motion
- TurnLeft180.motion
- TurnRight40.motion
- TurnRight60.motion
- StandUpFromFront.motion

---

## Project Description

The robot performs a structured motion routine using a state-based controller. The robot dances to the famous dance of "Macarena"

### Behavior Flow:
1. Robot starts in a stable pose
2. Executes a dance routine using side stepping motions
3. Performs a left turn using prebuilt motion files
4. Repeats the dance and turn sequence
5. Stops after completing the defined cycles

---

## Key Features
- State machine-based control (DANCE → TURN → STOP)
- Use of prebuilt NAO motion library
- Smooth motion transitions
- Basic behavior sequencing without external sensors

---

## Notes
- No external sensors (LiDAR / depth / custom vision) were used
- All movements are based on predefined Webots motion files
- Focus of the project is motion sequencing and control logic

---

## Author
Mahnoor Raja
