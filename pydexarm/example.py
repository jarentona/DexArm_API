from pydexarm import Dexarm

'''windows'''
#dexarm = Dexarm(port="COM67")
'''mac & linux'''
# device = Dexarm(port="/dev/tty.usbmodem3086337A34381")
dexarm = Dexarm(port="/dev/ttyACM0")


dexarm.go_home()
dexarm.fast_move_to(0, 250, 160)
dexarm.fast_move_to(50, 300, 0)
dexarm.fast_move_to(50, 300, -50)
#dexarm.soft_gripper_pick()
dexarm.fast_move_to(50, 300, 0)
dexarm.fast_move_to(-50, 300, 0)
dexarm.fast_move_to(-50, 300, -50)
dexarm.fast_move_to(-49, 301, -51)
dexarm.fast_move_to(-48, 302, -52)
dexarm.fast_move_to(-47, 303, -53)

#dexarm.soft_gripper_place()
#dexarm.soft_gripper_nature()
#dexarm.move_to(0, 400, 0)
#print("3", dexarm.get_current_position())
#dexarm.move_to(0, 400, -50)
#dexarm.delay_ms(1000)
#print("4", dexarm.get_current_position())
#dexarm.delay_ms(3000)
#print("#5",dexarm.get_current_position())
dexarm.go_home()
print("#6",dexarm.get_current_position())

#dexarm.air_picker_stop()
dexarm.close()
