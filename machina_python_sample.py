from machinaRobot import *
import json


bot = MachinaRobot()
bot.SpeedTo(100)

if len(bot.data) != 0 :
    print(bot.data)