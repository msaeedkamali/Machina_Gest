import websockets
import asyncio
import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
from machinaRobot import *
import json



Message_Recieved='''
{"event":"action-issued","last":"Move(0,0,3);","id":106,"pos":[-487.1,-109.7,485.9],"ori":[1,0,0,0,-1,0],"quat":[0.0001,-1,0,0.0001],"axes":null,"extax":null,"conf":null}
'''

data=json.loads(Message_Recieved)
#print(b)


dt=data['last']
print(dt)
#machinaRobot.sendToBridge(evback)
