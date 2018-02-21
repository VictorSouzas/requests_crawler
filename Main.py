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
print(args)
