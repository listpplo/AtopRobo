import time
from socket import socket, AF_INET, SOCK_STREAM
import pymelsec as plc
from pymelsec.constants import DT


def send_dl2_data():
    print("Google")
    dl2 = socket(AF_INET, SOCK_STREAM)
    dl2.settimeout(0.5)
    # try:
    #     dl2.connect(("192.168.250.100", 5002))
    #     connectToDL2 = True
    # except Exception as e:
    #     print("Unable to Connect to DL2 -- ", e)
    #     connectToDL2 = False

    connectToDL2 = False

    plc_device = plc.Type3E(host="192.168.3.250", port=1202)
    try:
        plc_device.connect("192.168.3.250", port=1202)
        plc_is_connected = True
    except Exception as e:
        print(e)
        plc_is_connected = False

    while True:
        print(connectToDL2)
        if connectToDL2:
            try:
                dl2.sendall(b"M0\r\n")
                data = dl2.recv(1024).decode()
                print(data)
                height_1 = int(data[3:13])/10000
                height_2 = int(data[14:])/10000
                plc_device.batch_write("D6000", [height_1, height_2], DT.FLOAT)
                print("Sending")
                connectToDL2 = True
            except Exception as e:
                print(e)

        if not connectToDL2:
            try:
                print("Trying to Reconnect")
                dl2.connect(("192.168.3.100", 1210))
                connectToDL2 = True
            except Exception as e:
                print("This is the error ", e)
                connectToDL2 = False
        time.sleep(0.5)

        if not plc_is_connected:
            try:
                plc_device.connect("192.168.3.250", port=1202)
            except Exception as e:
                print(e)
    


if __name__ == "__main__":
    send_dl2_data()