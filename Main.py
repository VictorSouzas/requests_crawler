# -*- coding: utf-8 -*-

import sys
import Robot.DigitalOceanRobot as dgo
import Robot.VultrRobot as vtr
import Robot.PacketRobot as pkg
import Controller.RobotController as RobotController


def help():
    return """
            -d or --donwload\t to donwload the data\n
            -v or --view\t to view the data\n
            -r or --remove\t to delete the data\n
            -h or --help\t to view this message\n
    """


args = sys.argv[1:]
if len(args) == 0:
    print(help())
if args[0] == '--help' or args[0] == '-h':
    print(help())
elif args[0] == '--download' or args[0] == '-d':
    print("Downloading data")
    digital_ocean = dgo.DigitalOceanRobot()
    digital_ocean_data = digital_ocean.parse()
    vultr = vtr.VultrRobot()
    vultr_data = vultr.parse()
    packet = pkg.PacketRobot()
    packet_data = packet.parse()
    RobotController.save(digital_ocean_data)
    RobotController.save(vultr_data)
    RobotController.save(packet_data)
    print("Done.")
elif args[0] == '--view' or args[0] == '-v':
    data = RobotController.read()
    if len(data) == 0:
        print("There is nothing th show")
    else:
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
elif args[0] == '--remove' or args[0] == '-r':
    print("Removing data")
    RobotController.remove()
    print("Data removed")
else:
    print(help())
