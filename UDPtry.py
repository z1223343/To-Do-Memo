import socket
import time

k = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    acc = car_state.kinematics_true.linear_acceleration
    print("%f,%f,%f,%f,%f,%f" % (roll, pitch, yaw,acc.x_val,acc.y_val,acc.z_val))

    k.sendto("%f,%f,%f,%f,%f,%f" % (roll, pitch, yaw,acc.x_val,acc.y_val,acc.z_val),('127.0.0.1',8888))
    time.sleep(0.05)
