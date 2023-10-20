#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import time 

import cv2
import mss
import numpy
        

def screen_record_efficiency():
    mon = {"top": 0, "left": 0, "width": 1280, "height": 720}
    
    title = "[MSS] FPS benchmark" 
    new_frame_time, prev_frame_time, fps = 0, 0, 0
    sct = mss.mss()                         # инициализировать mss
    last_time = time.time()    

    font = cv2.FONT_HERSHEY_SIMPLEX
    last_time = time.time()                 
    
    while True:
        img = numpy.asarray(sct.grab(mon))  # получаем картинку
        
        new_frame_time = time.time()
        fps = 1/(new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
    
        cv2.putText(img, str(fps), (7, 40), font, 1, (100, 255, 0), 3, cv2.LINE_AA)  # показывем фпс
        
        imS = cv2.resize(img, (854, 480))        
        cv2.imshow(title, imS)
        if cv2.waitKey(25) & 0xFF == ord("q"):  # ord("q") - вернуть позициб символа в юникоде
            cv2.destroyAllWindows()
            break
    
    return fps


screen_record_efficiency()
