# /env/bin/python3
# -*- coding: utf-8 -*-

import sys
import Robot.DigitalOceanRobot as dgo
import Robot.VultrRobot as vtr
import Robot.PacketRobot as pkg
import Controller.RobotController as RobotController


def help():
    pass


args = sys.argv[1:]
if len(args) == 0:
    print(help())
if args[0] == '--help' or args[0] == '-h':
    print(help())
elif args[0] == '--download' or args[0] == '-d':
    digital_ocean = dgo.DigitalOceanRobot()
    digital_ocean_data = digital_ocean.parse()
    vultr = vtr.VultrRobot()
    vultr_data = vultr.parse()
    packet = pkg.PacketRobot()
    packet_data = packet.parse()
    RobotController.save(digital_ocean_data)
    RobotController.save(vultr_data)
    RobotController.save(packet_data)
elif args[0] == '--view' or args[0] == '-v':
    data = RobotController.read()
    for x in data:
        print("\n\nUrl: %s" % (x[0]))
        print("Service: %s" % (x[1]))
        for y in x[2:]:
            print("\nMachine: %s" % (y[0]))
            print("Plans: ")
            for z in y[1:]:
                for a in z:
                    a = a[2:-1]
                    print(a)
print(args)
