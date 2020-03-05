#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:11:14 2020

@author: root
"""
import cv2

img = cv2.imread('/home/valdas/Desktop/RoboticP/figs/tools-black.jpg',1)
edge = cv2.Canny(img,830,250)
contours, hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

print("Number of Contours found = " + str(len(contours))) 

def scissors(value1,value2,value3):
    if value1<0:
         cv2.drawContours(img, contours, 7, (0,0,255), -1)
    else:
         cv2.drawContours(img, contours, 7, (0,0,255), value1)
         
    if value2<0:
         cv2.drawContours(img, contours, 8, (0,0,255), -1)
    else:
         cv2.drawContours(img, contours, 8, (0,0,255), value2)
    if value3<0:
         cv2.drawContours(img, contours, 9, (0,0,255), -1)
    else:
         cv2.drawContours(img, contours, 9, (0,0,255), value3)     
    cv2.imshow('picture',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0)
def pen():
    cv2.drawContours(img, contours, 5, (255,0,0), 5)
    cv2.drawContours(img, contours, 0, (255,0,0), 5)  
    cv2.imshow('picture',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0)
def crocodile():
    cv2.drawContours(img, contours, 2, (0,255,0), 5)
    cv2.drawContours(img, contours, 6, (0,255,0), 5)
    cv2.drawContours(img, contours, 4, (0,255,0), 5)
    cv2.imshow('picture',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0)
def circle(value):
    if value<0:
        cv2.drawContours(img, contours, 1, (50,50,0), -1) #full image
    else:
        cv2.drawContours(img, contours, 1, (255,255,0), 5) #only the edges
    cv2.imshow('picture',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0)
def alltogether():
    cv2.drawContours(img, contours, 7, (0,0,255), 5)
    cv2.drawContours(img, contours, 8, (0,0,255), 5)
    cv2.drawContours(img, contours, 9, (0,0,255), 5)
    cv2.drawContours(img, contours, 5, (255,0,0), 5)
    cv2.drawContours(img, contours, 0, (255,0,0), 5)
    cv2.drawContours(img, contours, 2, (0,255,0), 5)
    cv2.drawContours(img, contours, 6, (0,255,0), 5)
    cv2.drawContours(img, contours, 4, (0,255,0), 5)
    cv2.drawContours(img, contours, 1, (255,255,0), 5)
    cv2.imshow('picture',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0)
