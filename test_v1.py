
import os


def DIO(result):

    if result == True:
        try:
            os.system('sudo echo 393 > /sys/class/gpio/export')
            os.system('sudo echo out > /sys/class/gpio/gpio393/direction')
            os.system('sudo echo 1 > /sys/class/gpio/gpio393/value')
        except Exception as e:
            print(e)
            return 

    else:
        try:
            os.system('sudo echo 393 > /sys/class/gpio/export')
            os.system('sudo echo out > /sys/class/gpio/gpio393/direction')
            os.system('sudo echo 0 > /sys/class/gpio/gpio393/value')
        except Exception as e:
            print(e)
            return 


if __name__ == '__main__':
    result = True
    DIO(result)