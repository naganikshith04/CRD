import threading
from threading import*

import time

dictionary={}

def create(key,value,timeout=0):
    if key in dictionary:
        print("Key already exists in database") 
    else:
        if(key.isalpha()):
            if len(dictionary)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    dictionary[key]=l
            else:
                print(" 1GB memory exceeded!")
        else:
            print("Invalind key , key can be only string")
def read(key):
    if key not in dictionary:
        print("Given key does not exist in database") 
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
        else:
            stri=str(key)+":"+str(b[0])
            return stri

def delete(key):
    if key not in dictionary:
        print("Given key does not exist in database")
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del dictionary[key]
                print("key is successfully deleted") 
        else:
            del dictionary[key]
            print("key is successfully deleted")


def modify(key,value):
    b=dictionary[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dictionary:
                print("Given key does not exist in database") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dictionary[key]=l
        else:
            print("time-to-live of",key,"has expired")
    else:
        if key not in dictionary:
            print("Given key does not exist in database") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dictionary[key]=l
