import cv2
import numpy as np

Vid = cv2.VideoCapture("vid.avi")
fps = Vid.get(cv2.CAP_PROP_FPS)
size = (int (Vid.get(cv2.CAP_PROP_FRAME_WIDTH)),int(Vid.get(cv2.CAP_PROP_FRAME_WIDTH)))

vidWrite = cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)


sucess , frame = Vid.read()

while sucess:
    vidWrite.write(frame)
    sucess, frame = Vid.read()