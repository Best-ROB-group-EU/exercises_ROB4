#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:50:22 2020

@author: root
"""

#cv2.IMREAD_COLOR = flag 1
#cv2.IMREAD_GRAYSCALE = flag 2
#cv2. IMREAD_UNCHANGED = flag 3


import cv2
import numpy as np

def rgb_hsv():
     green = np.uint8([[[0,255,0 ]]])
     blue = np.uint8([[[0,0,255 ]]])
     red = np.uint8([[[255,0,0 ]]])
     hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
     hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
     hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
     print('green in hsv', hsv_green)
     print('blue in hsv', hsv_blue)
     print('red in hsv', hsv_red)

def picture(k):
    img = cv2.imread('/home/valdas/Desktop/RoboticP/figs/messi.jpg', k) #path, flag
    cv2.imshow('image',img) #string, arent
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def thresholdmessi():
     messi = cv2.imread('/home/valdas/Desktop/RoboticP/figs/messi.jpg',1)
     messi_hsv = cv2.cvtColor(messi, cv2.COLOR_BGR2HSV)
     
     lower_blue = np.array([110, 50,50]) #hsv pallette 
     upper_blue = np.array([140,255,255])
     
     mask = cv2.inRange(messi_hsv, lower_blue, upper_blue)
     target = cv2.bitwise_and(messi,messi, mask=mask) #mask combined with collored picture
     cv2.imshow('imi', messi)
     cv2.imshow('mask', mask)
     cv2.imshow('pipi', target)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

def thresholdtherma():
    therma1 = cv2.imread('/home/valdas/Desktop/RoboticP/figs/thermal1.png',1)
    therma1_hsv = cv2.cvtColor(therma1,cv2.COLOR_BGR2HSV)
    
    lower = np.array([0, 0, 62])
    higher = np.array([0, 0, 100])
    
    mask = cv2.inRange(therma1_hsv, lower, higher)
    target = cv2.bitwise_and(therma1, therma1, mask=mask)
    cv2.imshow('ini', therma1)
    cv2.imshow('therma1_hsv', therma1_hsv)
    cv2.imshow('target', target)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0)

def bitwise():
    therma1 = cv2.imread('/home/valdas/Desktop/RoboticP/figs/thermal1.png',1)
    therma2 = cv2.imread('/home/valdas/Desktop/RoboticP/figs/thermal2.png',1)
    
    bit_and = cv2.bitwise_and(therma1, therma2)
    bit_or = cv2.bitwise_or(therma1, therma2)
    
    cv2.imshow('therma1', therma1)
    cv2.imshow('therma2', therma2)
    cv2.imshow('bit_and', bit_and)
    cv2.imshow('bit_or', bit_or)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0)

def contrast():
    
#-----Reading the image-----------------------------------------------------
    img = cv2.imread('/home/valdas/Desktop/RoboticP/figs/Einstein.tif', 1)
    cv2.imshow("img",img) 
#Converting
    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    #cv2.imshow("lab",lab)

#-----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)
    #cv2.imshow('l_channel', l)
    #cv2.imshow('a_channel', a)
    #cv2.imshow('b_channel', b)

#-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=6.0, tileGridSize=(8,8)) #contrast increasement cliplimit
    cl = clahe.apply(l)
    #cv2.imshow('CLAHE output', cl)

#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl,a,b))
    cv2.imshow('limg', limg)

#-----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    cv2.imshow('final', final)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0)
#bitwise()
contrast()
    
    
    
    
    
    
    
    