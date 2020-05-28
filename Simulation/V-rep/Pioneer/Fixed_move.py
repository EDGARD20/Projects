import World

robot = World.init()
print sorted(robot.keys())

while robot:
    simulationTime = World.getSimulationTime()
    if simulationTime % 1000 == 0:
        print ('Time:', simulationTime,
        "ultraSonicSensorLeft", World.getSensorReading("ultraSonicSensorLeft"),
        "ultraSonicSensorRight", World.getSensorReading("ultraSonicSensorRight"))

    def running(nBlock, direction, simTime):
        speed = 3
        if direction == 'r':

            for i in range(0, nBlock):
                World.collectNearestBlock()
                World.execute(dict(speedLeft=0, speedRight=speed), simTime, 0)
                World.collectNearestBlock()
        if direction == 'l':
            for i in range(0, nBlock):
                World.collectNearestBlock()
                World.execute(dict(speedLeft=speed, speedRight=0), simTime, 0)
                World.collectNearestBlock()
        if direction == 'f':
            for i in range(0, nBlock):
                World.collectNearestBlock()
                World.execute(dict(speedLeft=speed, speedRight=speed), simTime, 0)
                World.collectNearestBlock()
        if direction == 'b':
            for i in range(0, nBlock):
                World.collectNearestBlock()
                World.execute(dict(speedLeft=speed, speedRight=-speed), simTime, 0)
                World.collectNearestBlock()
    # you need to run many times to get the correct values.
    # The goal is to collect red box on the area as many as possible
    # Better method is to modify simulation time
    # instead of time to reaped we can set how many block we want the robot moves.
    # running(nBlock, Direction, simulationTime)
    running(2, 'f', 1600)  # every 1600ms = 1 block then here syntax means 2 block forward.
    running(1, 'r', 1770)
    running(3, 'f', 1600)
    running(1, 'b', 1880)
    running(3, 'f', 1600)
    running(1, 'r', 1770)
    running(3, 'f', 1600)
    running(1, 'r', 1770)
    running(3, 'f', 1600)
    running(1, 'l', 1770)
    running(2, 'f', 1600)
    running(1, 'r', 1770)
    running(2, 'f', 1600)
    running(1, 'r', 1775)
    running(2, 'f', 1600)
    running(1, 'b', 1880)
    running(3, 'f', 1600)
    # and so on,, Have fun

    World.STOP()
    if simulationTime %10000 == 0:
        print ("Trying to collect a block...", World.collectNearestBlock())
    robot = 0