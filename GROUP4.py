import cv2
import numpy as np
import cv2,math,subprocess
from skimage.metrics import structural_similarity

def structural_sim(img1, img2):
    sim, diff = structural_similarity(img1, img2, full=True)
    return sim
font=cv2.FONT_HERSHEY_COMPLEX
cap=cv2.VideoCapture("C:\project\gwent.mp4")
template = cv2.imread("C:\FINAL/POISK3.png", 0)
h, w = template.shape
succ, frame = cap.read()
frameRate = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
VideoSave = cv2.VideoWriter("filename.mp4",
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         frameRate, size)

frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
EBS2=frame2[352:396,1822:1875]
MBS2=frame2[683:726,1822:1875]

def EBSfun(EBS2):
    EBS = frame2[352:396, 1822:1875]
    ssimEBS = structural_sim(EBS, EBS2)


    result = cv2.matchTemplate(frame2[339:409, 1809:1888], template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
    if max_val > 0.97:
        bottom_right = (1809 + max_loc[0] + w, 339 + max_loc[1] + h)
        cv2.rectangle(frame, (1809 + max_loc[0], 339 + max_loc[1]), bottom_right, (255, 255, 255), 1)
        ssimEBS = 1
        EBS=EBS2

    cv2.putText(frame, str(ssimEBS), (1700, 350), font, 1, (255, 255, 255), 1)

    EBS2 = EBS
    return EBS2,ssimEBS
def MBSfun(MBS2):
    MBS = frame2[683:726, 1822:1875]
    ssimMBS = structural_sim(MBS, MBS2)
    result = cv2.matchTemplate(frame2[669:739, 1809:1888], template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
    if max_val > 0.97:
        bottom_right = (1809 + max_loc[0] + w, 669 + max_loc[1] + h)
        cv2.rectangle(frame, (1809 + max_loc[0], 669 + max_loc[1]), bottom_right, (255, 255, 255), 1)
        ssimMBS = 1
        MBS=MBS2

    cv2.putText(frame, str(ssimMBS), (1700, 600), font, 1, (255, 255, 255), 1)

    MBS2 = MBS
    return MBS2,ssimMBS
file = open("CALIBRATION.txt")
LEFT_TOP_CORNER = [0,0,0]
LEFT_BOT_CORNER = [0,0,0]


LEFT_TOP_CARD = [0,0,0]
LEFT_BOT_CARD = [0,0,0]
RIGHT_TOP_CARD = [0,0,0]
RIGHT_BOT_CARD = [0,0,0]


def PROPERREAD(q1,file):
    for q2 in range(3):
        q1[q2]=int(file.readline())
    return q1

LEFT_TOP_CORNER3 = [0,0,0]
LEFT_BOT_CORNER3 = [0,0,0]

LEFT_TOP_CARD3 = [0,0,0]
LEFT_BOT_CARD3 = [0,0,0]
RIGHT_TOP_CARD3 = [0,0,0]
RIGHT_BOT_CARD3 = [0,0,0]

LEFT_TOP_CORNER = PROPERREAD(LEFT_TOP_CORNER,file)
LEFT_BOT_CORNER = PROPERREAD(LEFT_BOT_CORNER,file)

LEFT_TOP_CARD = PROPERREAD(LEFT_TOP_CARD,file)
LEFT_BOT_CARD = PROPERREAD(LEFT_BOT_CARD,file)
RIGHT_TOP_CARD = PROPERREAD(RIGHT_TOP_CARD,file)
RIGHT_BOT_CARD = PROPERREAD(RIGHT_BOT_CARD,file)
file.close()
def VIZU_STOL():
    LEFT_TOP_CORNER2 = frame[60,50]
    LEFT_BOT_CORNER2 = frame[1027, 60]

    for x in range(3):
        LEFT_TOP_CORNER3[x] = abs(max(LEFT_TOP_CORNER2[x],LEFT_TOP_CORNER[x]) - min(LEFT_TOP_CORNER2[x],LEFT_TOP_CORNER[x]))
        LEFT_BOT_CORNER3[x] = abs(max(LEFT_BOT_CORNER2[x],LEFT_BOT_CORNER[x]) - min(LEFT_BOT_CORNER2[x],LEFT_BOT_CORNER[x]))
    cv2.putText(frame, "LEFT TOP "+str(LEFT_TOP_CORNER3)+"  "+str(LEFT_BOT_CORNER2)+"  "+str(LEFT_TOP_CORNER), (500, 200), font, 1, (255, 255, 255), 1)
    cv2.putText(frame, "LEFT BOT "+str(LEFT_BOT_CORNER3)+"  "+str(LEFT_BOT_CORNER2)+"  "+str(LEFT_BOT_CORNER), (500, 300), font, 1, (255, 255, 255), 1)


    WIJU1 = 0
    if max(LEFT_TOP_CORNER3) < 10:
        WIJU1 += 1
    if max(LEFT_BOT_CORNER3) < 10:
        WIJU1 += 1
    if WIJU1 > 0:
        cv2.putText(frame, "ВИЖУ", (1440, 100), font, 1, (255, 255, 255), 1)
        return True
    else:
        cv2.putText(frame, "НЕВИЖУ", (1440, 100), font, 1, (255, 255, 255), 1)
        return False
while True:

    succ, frame = cap.read()
    frame2=frame
    frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if VIZU_STOL():
        EBS2,ssimEBS= EBSfun(EBS2)
        MBS2,ssimMBS= MBSfun(MBS2)
    VideoSave.write(frame)
    cv2.imshow("nazvanie okoska",frame)
    if (cv2.waitKey(22) & 0xFF == ord('q')):
        break