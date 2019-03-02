

import vrep
import numpy as np
print("start vrep successfully ")
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,500,5)
if clientID!=-1:
    res,objs=vrep.simxGetObjects(clientID,vrep.sim_handle_all,vrep.simx_opmode_buffer)
    if res==vrep.simx_return_ok:
        print ('Number of objects in the scene: ',len(objs))
        ret1, LBR4p_joint1 = vrep.simxGetObjectHandle(clientID, 'LBR4p_joint1#',vrep.simx_opmode_buffer)
        ret2 = vrep.simxSetJointPosition(clientID,LBR4p_joint1,.25,vrep.simx_opmode_buffer)
    else:
        print ('Remote API function call returned with error code: ',res)
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')
