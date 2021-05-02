import cv2
import numpy as np
#scanning image
img=cv2.imread("exp.png")


#edge detection
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  
                                         cv2.THRESH_BINARY, 9, 9) 

#cartoon
color=cv2.bilateralFilter(img, 9 , 250, 250)
cartoon=cv2.bitwise_and(color,color,mask=edges)

scale_percent=1
width=int(cartoon.shape[1]*scale_percent)
height=int(cartoon.shape[0]*scale_percent)
dimension=(width,height)
resized=cv2.resize(cartoon,dimension,interpolation=cv2.INTER_AREA)
#display
#cv2.imshow("Image", img) 
#cv2.imshow("edges", edges) 
#cv2.imshow("Cartoon", cartoon) 
cv2.imshow("output",resized)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

   
