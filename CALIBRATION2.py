import cv2
import cv2,math,subprocess
from skimage.metrics import structural_similarity
import numpy as np
import time
start_time = time.time()
def structural_sim(img1, img2):
    sim, diff = structural_similarity(img1, img2, full=True)
    return sim

cancel3=0
order3=0
play3=0
preview3=0
select3=0
def PROPERWRITE(q1,file):
    for q2 in range(3):
        file.write(str(q1[q2]) + "\n")
def CALIBRATION():
    select = cv2.imread("C:/project/KAL_ANAL/GRAYBUTTON/select.png", 0)
    cancel = cv2.imread("C:/project/KAL_ANAL/GRAYBUTTON/cancel.png", 0)
    order = cv2.imread("C:/project/KAL_ANAL/GRAYBUTTON/order.png", 0)
    play = cv2.imread("C:/project/KAL_ANAL/GRAYBUTTON/play.png", 0)
    preview = cv2.imread("C:/project/KAL_ANAL/GRAYBUTTON/preview.png", 0)
    cap = cv2.VideoCapture("C:/project/gwent.mp4")
    frameAmount=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    selectSSIM=0
    cancelSSIM=0
    orderSSIM=0
    playSSIM=0
    previewSSIM=0
    succ, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    select3 = frame[1033:1050, 1787:1809]
    cancel3 = frame[1033:1050, 1787:1809]
    order3 = frame[1033:1050, 1787:1809]
    play3 = frame[1033:1050, 1787:1809]
    preview3 = frame[1033:1050, 1787:1809]
    KUROK=0
    for x in range(frameAmount-40000-10):
        if KUROK == 0 and cancelSSIM > 0.3:
            cap.set(cv2.CAP_PROP_POS_FRAMES, (cap.get(cv2.CAP_PROP_POS_FRAMES)-2))
            succ, frame = cap.read()
            LEFT_TOP_CORNER = frame[60, 50]
            LEFT_BOT_CORNER = frame[1027, 60]

            LEFT_TOP_CARD = frame[134, 1540]
            LEFT_BOT_CARD = frame[395, 1540]
            RIGHT_TOP_CARD = frame[134, 1710]
            RIGHT_BOT_CARD = frame[395, 1712]
            KUROK = 1
        succ,frame = cap.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        select2=frame[1033:1050,1787:1809]
        cancel2=frame[1033:1050,1787:1809]
        order2=frame[1033:1050,1787:1809]
        play2=frame[1033:1050,1787:1809]
        preview2=frame[1033:1050,1787:1809]
        selectSSIM2=structural_sim(select, select2)
        if selectSSIM2 > selectSSIM:
            select3=select2
            selectSSIM=selectSSIM2
        cancelSSIM2=structural_sim(cancel, cancel2)
        if cancelSSIM2 > cancelSSIM:
            cancel3=cancel2
            cancelSSIM=cancelSSIM2
        orderSSIM2=structural_sim(order,order2)
        if orderSSIM2> orderSSIM:
            order3=order2
            orderSSIM=orderSSIM2
        playSSIM2=structural_sim(play, play2)
        if playSSIM2 > playSSIM:
            play3=play2
            playSSIM=playSSIM2
        previewSSIM2=structural_sim(preview, preview2)
        if previewSSIM2 > previewSSIM:
            preview3=preview2
            previewSSIM=previewSSIM2
        print(x)
        print(selectSSIM," ",cancelSSIM," ",orderSSIM," ",playSSIM," ",previewSSIM)
    cv2.imwrite("C:/FINAL/CALIBRATION/cancel.png", cancel3)
    cv2.imwrite("C:/FINAL/CALIBRATION/order.png", order3)
    cv2.imwrite("C:/FINAL/CALIBRATION/play.png", play3)
    cv2.imwrite("C:/FINAL/CALIBRATION/preview.png", preview3)
    cv2.imwrite("C:/FINAL/CALIBRATION/select.png", select3)
    file = open("CALIBRATION.txt","w")
    PROPERWRITE(LEFT_TOP_CORNER,file)
    PROPERWRITE(LEFT_BOT_CORNER,file)

    PROPERWRITE(LEFT_TOP_CARD,file)
    PROPERWRITE(LEFT_BOT_CARD,file)
    PROPERWRITE(RIGHT_TOP_CARD,file)
    PROPERWRITE(RIGHT_BOT_CARD,file)
    file.close()
  #  return LEFT_TOP_CORNER, LEFT_BOT_CORNER, RIGHT_TOP_CORNER, RIGHT_BOT_CORNER,LEFT_TOP_CARD,LEFT_BOT_CARD,RIGHT_TOP_CARD,RIGHT_BOT_CARD
CALIBRATION()
# print(LEFT_TOP_CORNER)
