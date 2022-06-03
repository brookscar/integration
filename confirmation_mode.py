from marvelmind import MarvelmindHedge
from time import sleep
import sys
import time

#Open motor
baudRate = 115200
port = "/dev/ttyACM0"
import sys
sys.path.append("../src/open_motor/")
from open_motor_serial import open_motor
comms = open_motor()
comms.init_serial_port(port,baudRate,0.5)

hedge = MarvelmindHedge(tty = "/dev/ttyACM1", adr=19, debug=False) # create MarvelmindHedge thread

def firstCheckpoint():
    hedge.dataEvent.clear()

    if(hedge.positionUpdated):
        X = hedge.position()[1]
        Y = hedge.position()[2]
        
        hedge.print_position()
        time.sleep(1)
    
        if(2.2 <= X <= 2.5 or X > 2.6):
            print("i am stopping")
            comms.send_pwm_goal(0,0,0,0)
            time.sleep(3)
            comms.send_pwm_goal(0,80,-80,0)
            time.sleep(2)
            comms.send_pwm_goal(0,253,300,0)
            time.sleep(2)
            comms.send_pwm_goal(0,-150,150,0)
            time.sleep(1)
            comms.send_pwm_goal(0,253,300,0)
            time.sleep(1)
            comms.send_pwm_goal(0,80,-80,0)
            time.sleep(0.5)
            comms.send_pwm_goal(0,253,300,0)
            
            
            
        else:
            print("i am running")
            comms.send_pwm_goal(0,253,290,0)
                
def main():

    hedge.start() # start thread
    while True:
        try:
            hedge.dataEvent.clear()

            if(hedge.positionUpdated):
                X = hedge.position()[1]
                Y = hedge.position()[2]
                
                hedge.print_position()
                time.sleep(1)
                if(-2 <= X <= 22):
                
                    if(-2 <= X <= 2.8):
                        firstCheckpoint()
                     
                    else:
                        comms.send_pwm_goal(0,0,0,0)
                        
            else:
                comms.send_pwm_goal(0,0,0,0)
                   
        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()
main()