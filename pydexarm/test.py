#!/usr/bin/env python3
import serial, time

s = serial.Serial("/dev/ttyACM0",115200)

def w(gcode):
    s.write(gcode.encode('utf-8')+b'\r\n')
    while (not s.read()): pass

#main function
def main():
    # アームを初期位置に
    w("M1111")
    time.sleep(1)
    # 動作速度の設定(8000が最大？？)
    w("G0 F8000")
    # アームを指定した座標まで動かす
    w("G0 X150Y0Z100")
    w('G0 X0Y300Z0')
    w('G0 X0Y-300Z0')
    w('G0 X150Y150Z0')
    w('G0 X150Y-150Z0')
    w('G0 X300Y0Z0')
    w('G0 X200Y0Z50')

if __name__ == '__main__':
    main()