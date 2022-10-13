#!/usr/bin/env python
# ip cam example
import cv2
import urllib 
import numpy as np
stream=urllib.urlopen('http://root:robot3233@god.csie.ntu.edu.tw/axis-cgi/mjpg/video.cgi?resolution=704x480')
# stream=urllib.urlopen('http://192.168.1.161:81/videostream.cgi?user=wuhsch&pwd=6423122')
# stream=urllib.urlopen('http://god.csie.ntu.edu.tw/videostream.cgi?user=root&pwd=robot3233')

bytes=''
while True:
	bytes+=stream.read(1024)
	a = bytes.find('\xff\xd8')
	b = bytes.find('\xff\xd9')
	if a!=-1 and b!=-1:
		jpg = bytes[a:b+2]
		bytes= bytes[b+2:]

		i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),1)
		#i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
		cv2.imshow('i',i)
		if cv2.waitKey(1) ==27:
    			exit(0)
#write your programs here
test ='123'
test1 ='123456'
