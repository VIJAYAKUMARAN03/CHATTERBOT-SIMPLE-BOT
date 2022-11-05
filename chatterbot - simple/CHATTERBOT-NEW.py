# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:34:59 2022

@author: Student
"""

from greets import *
from nltk.corpus import wordnet
s="""! I am a simple chatter bot,
You can use me to search : 
    1. meaning for a word.(meaning of 'word')
    2. synonym for a word.(synonym of 'word')
    3. antonym for a word.(antonym of 'word')
    4. Also you can use me to perform some binary mathematical operations 
        (No. operator No.) (e.g. 5 + 3)
        Addtion(+),Substraction(-),Multiplication(*),Division(/),power(^).
    5. If your input is not related in anyone of the above then I'll act as a Echoo Bot:).
    6. To stop/quit Type 'quit'! \n"""

print(get_greet(),s)



while(1):
    msg=input()
    msgs=msg.split()
    msglow=msg.lower()
    if "quit" in msglow:
        print("Its hard to leave ... Anyway Bye.. Have a Nice Day :)!")
        break
    elif len(msgs)==3:
        if(msgs[1] =="+" or  msgs[1]=="-" or msgs[1] == "*" or msgs[1]=="/"or msgs[1]=="^" ):
            a=float(msgs[0])
            b=float(msgs[2])
            if(msgs[1]=="+"):
                print(a+b)
            elif(msgs[1]=="-"):
                print(a-b)
            elif(msgs[1]=="*"):
                print(a*b)
            elif(msgs[1]=="/"):
                print(a/b)
            elif(msgs[1]=="^"):
                print(a**b)
        elif "meaning of" in msglow:
            d=wordnet.synsets(msgs[2])
            print("Meaning of",msgs[2],"is",d[0].definition())
        elif "synonym of" in msglow:
            d=wordnet.synsets(msgs[2])
            print("Synonym of",msgs[2],"is",d[0].lemmas()[0].name())          
        elif "antonym of" in msglow:
            d=wordnet.synsets(msgs[2])
            try: 
                print("Antonym of",msgs[2],"is",d[0].lemmas.antonyms()[0].name())  
            except:
                print("Sorry, Antonym of",msgs[2],"is None :(")
        else:
            print(msg)
    else:
        print(msg)