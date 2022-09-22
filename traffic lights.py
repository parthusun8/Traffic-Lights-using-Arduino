import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

while True:
    for i in range(0, 60):
        board.digital[13].write(1)
        board.digital[12].write(0)
        board.digital[11].write(0)
        time.sleep(1)
    for i in range(0, 15):
        board.digital[13].write(0)
        board.digital[12].write(1)
        board.digital[11].write(0)
        time.sleep(1)
    for i in range(0, 40):
        board.digital[13].write(0)
        board.digital[12].write(0)
        board.digital[11].write(1)
        time.sleep(1)
    time.sleep(0.1)