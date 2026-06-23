from controller import Robot

TIME_STEP = 32
robot = Robot()

def m(name):
    d = robot.getDevice(name)
    d.setVelocity(0.5)
    return d

RSP = m("RShoulderPitch")
LSP = m("LShoulderPitch")
RSR = m("RShoulderRoll")
LSR = m("LShoulderRoll")
RER = m("RElbowRoll")
LER = m("LElbowRoll")
REY = m("RElbowYaw")
LEY = m("LElbowYaw")
RHR = m("RHipRoll")
LHR = m("LHipRoll")

def wait(ms):
    for _ in range(max(1, ms // TIME_STEP)):
        robot.step(TIME_STEP)

def pose(joints, ms=1000):
    for joint, val in joints.items():
        joint.setPosition(val)
    wait(ms)

pose({RSP:1.4, LSP:1.4, RSR:-0.3, LSR:0.3,
      RER:0.5, LER:-0.5, REY:1.2, LEY:-1.2,
      RHR:0.0, LHR:0.0})

# Step 1: Right arm raises forward (horizontal)
pose({RSP:0.0, RSR:0.0, RER:0.0, REY:0.0})

# Step 2: Left arm raises forward to match
pose({LSP:0.0, LSR:0.0, LER:0.0, LEY:0.0})

# Step 3: Rotate right wrist
pose({REY:1.5})

# Step 4: Rotate left wrist
pose({LEY:-1.5})

# Step 5: Right arm crosses to left shoulder
pose({RSP:0.4, RSR:0.31, RER:1.5, REY:1.0})

# Step 6: Left arm crosses to right shoulder
pose({LSP:0.4, LSR:-0.31, LER:-1.5, LEY:-1.0})

# Step 7: LEFT hand touches head
pose({
    LSP: -1.5,
    LSR:  0.0,
    LER: -1.5,
    LEY:  0.0
})

# Step 8: RIGHT hand touches head
pose({
    RSP: -1.5,
    RSR:  0.0,
    RER:  1.5,
    REY:  0.0
})

# Step 9: Both arms drop to hips
pose({RSP:1.7, LSP:1.7, RSR:-0.1, LSR:0.1,
      RER:0.1, LER:-0.1, REY:0.5, LEY:-0.5})

# Step 10: Hip sway
pose({RHR:-0.3, LHR:-0.3}, 400)
pose({RHR: 0.3, LHR: 0.3}, 400)
pose({RHR:-0.3, LHR:-0.3}, 400)
pose({RHR: 0.3, LHR: 0.3}, 400)
pose({RHR: 0.0, LHR: 0.0}, 400)

print("Done! Hey Macarena!")
wait(500)