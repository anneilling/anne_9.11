from random import *
from keyboard import *
from module911 import*
game=start()
b=["Kivi", "käärid", "paber"]
g=["Kivi", "käärid", "paber"]
if game==1:
    sober(b)

elif game==2:
    robot(g)

elif game==3:
    bot_vs_bot(b,g)
              
           