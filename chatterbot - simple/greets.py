# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:34:11 2022

@author: Student
"""
from random import *

def get_greet():
    greetings=["Hello","Hi","Hey","Good Day","Hey there"]
    return(greetings[randint(0,len(greetings)-1)])



