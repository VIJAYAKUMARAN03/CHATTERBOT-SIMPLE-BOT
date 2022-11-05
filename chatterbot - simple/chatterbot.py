# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:34:59 2022

@author: Student
"""

from greets import *
from PyDictionary import PyDictionary

s="""! I am a simple chatter bot,
You can use me to search meaning('word' - meaning),antonyms(word - antonyms) for a word.
Also you can use me to perform some binary mathematical operations (No. operator No.) (e.g. 5 + 3)"""

print(get_greet(),s)

d= PyDictionary()

while(1):
    msg=input()
    msgs=msg.split()
    if "quit" in msg:
        print("Its hard to leave ... Anyway Bye.. Have a Nice Day :)!")
        break
    elif msgs[1] =="+" or  msgs[1]=="-" or msgs[1] == "*" or msgs[1]=="/" :
        a=float(msgs[0])
        b=float(msgs[2])
        if(msgs[1]=="+"):
            print(a+b)
        elif(msgs[1]=="-"):
            print(a-b)
        elif(msgs[1]=="*"):
            print(a*b)
        else:
            print(a/b)
    elif "- message" in msg:
        print("meaning of",msg[0],"is",d.meaning(msg[0]))
    elif "- synonym" in msg:
        print("synonym of",msg[0],"is",d.synonym(msg[0]))          
    elif "- antonym" in msg:
      print("antonym of",msg[0],"is",d.antonym(msg[0]))        