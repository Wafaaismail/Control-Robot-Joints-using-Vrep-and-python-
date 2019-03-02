

try:
    import vrep
except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')
#connect with vrep
print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
    vrep.simxAddStatusbarMessage(clientID,'Hello V-REP!',vrep.simx_opmode_oneshot)

    res,objs=vrep.simxGetObjects(clientID,vrep.sim_handle_all,vrep.simx_opmode_blocking)
    if res==vrep.simx_return_ok:
        print ('Number of objects in the scene: ',len(objs))
        res1,joint1_handel=vrep.simxGetObjectHandle(clientID,"P_Arm_joint1",vrep.simx_opmode_blocking)
        res2,joint2_handel=vrep.simxGetObjectHandle(clientID,"P_Arm_joint2",vrep.simx_opmode_blocking)
        res3,joint3_handel=vrep.simxGetObjectHandle(clientID,"P_Arm_joint3",vrep.simx_opmode_blocking)
        res4,joint4_handel=vrep.simxGetObjectHandle(clientID,"P_Arm_joint4",vrep.simx_opmode_blocking)
        res5,joint5_handel=vrep.simxGetObjectHandle(clientID,"P_Arm_joint5",vrep.simx_opmode_blocking)
        res6,joint6_handel=vrep.simxGetObjectHandle(clientID,"P_Arm_joint6",vrep.simx_opmode_blocking)

    import numpy as np

    def last_pos(join_num):
        theta =0
        if(join_num==1):
            result, theta = vrep.simxGetJointPosition(clientID, joint1_handel, vrep.simx_opmode_blocking)
        elif(join_num==2):
            result, theta = vrep.simxGetJointPosition(clientID, joint2_handel, vrep.simx_opmode_blocking)
        elif(join_num ==3):
            result, theta = vrep.simxGetJointPosition(clientID, joint3_handel, vrep.simx_opmode_blocking)
        elif(join_num ==4):
            result, theta = vrep.simxGetJointPosition(clientID, joint4_handel, vrep.simx_opmode_blocking)
        elif(join_num ==5):
            result, theta = vrep.simxGetJointPosition(clientID, joint5_handel, vrep.simx_opmode_blocking)
        elif(join_num ==6):
            result, theta = vrep.simxGetJointPosition(clientID, joint6_handel, vrep.simx_opmode_blocking)
        return theta

    def movementAngle(step):
        movementAngle = 10
        if (step == 1):
            movementAngle =((step*movementAngle)*3.14)/180
        elif (step == 2):
            movementAngle =((step*movementAngle)*3.14)/180
        elif (step == 3):
            movementAngle =((step*movementAngle)*3.14)/180
        elif (step == 4):
            movementAngle =((step*movementAngle)*3.14)/180
        elif (step == 5):
            movementAngle =((step*movementAngle)*3.14)/180
        elif (step == 6):
            movementAngle =((step*movementAngle)*3.14)/180
        return movementAngle


    #set position
    import time
    def inc_joint_pos(joint_num,step):
        if (joint_num ==1):
            pos1=vrep.simxSetJointTargetPosition(clientID,joint1_handel,(last_pos(joint_num) + movementAngle(step)),vrep.simx_opmode_blocking)
            time.sleep(1)
        elif(joint_num ==2):
            pos2 =vrep.simxSetJointTargetPosition(clientID,joint2_handel,(last_pos(joint_num) +  movementAngle(step)),vrep.simx_opmode_blocking)
            time.sleep(1)
        elif(joint_num ==3):
            pos3 =vrep.simxSetJointTargetPosition(clientID,joint3_handel,(last_pos(joint_num) +  movementAngle(step)),vrep.simx_opmode_blocking)
            time.sleep(1)
        elif(joint_num ==4):
            pos4 =vrep.simxSetJointTargetPosition(clientID,joint4_handel,(last_pos(joint_num) +  movementAngle(step)),vrep.simx_opmode_blocking)
            time.sleep(1)
        elif(joint_num ==5):
            pos5 =vrep.simxSetJointTargetPosition(clientID,joint5_handel,(last_pos(joint_num) +  movementAngle(step)),vrep.simx_opmode_blocking)
            time.sleep(1)
        elif(joint_num ==6):
            pos6 =vrep.simxSetJointTargetPosition(clientID,joint6_handel,(last_pos(joint_num) + movementAngle(step)),vrep.simx_opmode_blocking)
            time.sleep(1)

    def dec_joint_pos(joint_num,step):
        pos1=vrep.simxSetJointTargetPosition(clientID,joint1_handel,(last_pos(joint_num) - movementAngle(step)),vrep.simx_opmode_blocking)
        time.sleep(1)

        pos2 =vrep.simxSetJointTargetPosition(clientID,joint2_handel,(last_pos(joint_num) -  movementAngle(step)),vrep.simx_opmode_blocking)
        time.sleep(1)

        pos3 =vrep.simxSetJointTargetPosition(clientID,joint3_handel,(last_pos(join_num) -  movementAngle(step)),vrep.simx_opmode_blocking)
        time.sleep(1)

        pos4 =vrep.simxSetJointTargetPosition(clientID,joint4_handel,(last_pos(join_num) -  movementAngle(step)),vrep.simx_opmode_blocking)
        time.sleep(1)

        pos5 =vrep.simxSetJointTargetPosition(clientID,joint5_handel,(last_pos(join_num) -  movementAngle(step)),vrep.simx_opmode_blocking)
        time.sleep(1)

        pos6 =vrep.simxSetJointTargetPosition(clientID,joint6_handel,(last_pos(join_num) - movementAngle6),vrep.simx_opmode_blocking)
        time.sleep(1)


else:
    print ('Failed connecting to remote API server')
    print ('Program ended')

#****************************************GUI******************************************************
from tkinter import *
class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 1
        self.joint_num=0
        self.create_widget()


    def create_widgetinc(self):
            self.bttn = Button(self)
            self.bttn['command'] = (self.callbackinc)
        self.bttn.grid()


    def callbackinc(self):
        self.bttn['text'] = "increase: " + str(self.bttn_clicks)
        if (self.bttn_clicks == 1):
            inc_joint_pos(joint_num,1)
            self.bttn_clicks+=1
        elif (self.bttn_clicks == 2):
            inc_joint_pos(joint_num,2)
            self.bttn_clicks+=1
        elif (self.bttn_clicks == 3):
            inc_joint_pos(joint_num,3)
            self.bttn_clicks+=1
        elif (self.bttn_clicks == 4):
            inc_joint_pos(joint_num,4)
            self.bttn_clicks+=1
        elif (self.bttn_clicks == 5):
            inc_joint_pos(joint_num,5)
            self.bttn_clicks+=1
        elif (self.bttn_clicks == 6):
            inc_joint_pos(joint_num,6)
            self.bttn_clicks =1


        def callbackdec(self):
            self.bttn['text'] = "decrease: " + str(self.bttn_clicks)
            if (self.bttn_clicks == 1):
                dec_joint_pos(joint_num,1)
                self.bttn_clicks+=1
            elif (self.bttn_clicks == 2):
                dec_joint_pos(joint_num,2)
                self.bttn_clicks+=1
            elif (self.bttn_clicks == 3):
                dec_joint_pos(joint_num,3)
                self.bttn_clicks+=1
            elif (self.bttn_clicks == 4):
                dec_joint_pos(joint_num,4)
                self.bttn_clicks+=1
            elif (self.bttn_clicks == 5):
                dec_joint_pos(joint_num,5)
                self.bttn_clicks+=1
            elif (self.bttn_clicks == 6):
                dec_joint_pos(joint_num,6)
                self.bttn_clicks =1



root = Tk()
root.title("Click Counter")
root.geometry('200x50')

app = Application(root)

root.mainloop()
