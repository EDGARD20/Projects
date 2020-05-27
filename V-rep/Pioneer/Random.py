import World
import random
robot = World.init()
print sorted(robot.keys())

while robot:
    simulationTime = World.getSimulationTime()
    if simulationTime % 1000 == 0:
        print ('Time:', simulationTime,
        "ultraSonicSensorLeft", World.getSensorReading("ultraSonicSensorLeft"),
        "ultraSonicSensorRight", World.getSensorReading("ultraSonicSensorRight"))

    motorSpeed = dict(speedLeft= random.randint(-100, 100), speedRight=random.randint(-100, 100))

    World.collectNearestBlock() # not needed for simulation, just for taking red box implemented in world in V-rep,
    World.setMotorSpeeds(motorSpeed)
    if simulationTime %10000 == 0:
        print ("Trying to collect a block...", World.collectNearestBlock())