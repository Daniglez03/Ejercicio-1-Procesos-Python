import os
import platform
from time import sleep

if (platform.system() == 'Linux'):
    def padre():
        cantidad = int(input("Cuántos procesos hijos quieres ?"))
        for i in range(cantidad):
            newPid = os.fork()
            if(newPid == 0):
                hijo()
    def hijo():
        print("Soy un hijo con PID :", os.getpid())
        sleep(5)
        print("Estoy acabando mi ejecución...")
        os._exit(0)

if __name__ == "__main__":
    padre()