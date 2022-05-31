import cv2,math,subprocess
from skimage.metrics import structural_similarity
import numpy as np
import time
import sys
start_time = time.time()

def structural_sim(img1, img2):
    sim, diff = structural_similarity(img1, img2, full=True)
    return sim

S1=cv2.imread("C:\project\KAL_ANAL\S1.png")
S2=cv2.imread("C:\project\KAL_ANAL\S2.png")
R1=cv2.imread("C:\project\KAL_ANAL\R1.png")
RRR3=cv2.imread("C:\project\KAL_ANAL\RRR3.png")
Crown=cv2.imread("C:\project\KAL_ANAL\Crown.png")
MP=cv2.imread("C:\project\KAL_ANAL\MP.png")
EP=cv2.imread("C:\project\KAL_ANAL\EP.png")

RRR2=cv2.imread("C:\project\KAL_ANAL\RRR2.png")
RRR1=cv2.imread("C:\project\KAL_ANAL\RRR1.png")
RRR0=cv2.imread("C:\project\KAL_ANAL\RRR0.png")
NR1=cv2.imread("C:\project\KAL_ANAL/NR1.png")
NR2=cv2.imread("C:\project\KAL_ANAL/NR2.png")
R2=cv2.imread("C:\project\KAL_ANAL\R2.png")
NR3=cv2.imread("C:\project\KAL_ANAL/NR3.png")
FR=cv2.imread("C:\project\KAL_ANAL\FR.png")
sword=cv2.imread("C:\project\KAL_ANAL\sword.png")


S1 = cv2.cvtColor(S1, cv2.COLOR_BGR2GRAY)
S2 = cv2.cvtColor(S2, cv2.COLOR_BGR2GRAY)
R1 = cv2.cvtColor(R1, cv2.COLOR_BGR2GRAY)

Crown = cv2.cvtColor(Crown, cv2.COLOR_BGR2GRAY)
MP = cv2.cvtColor(MP, cv2.COLOR_BGR2GRAY)
EP = cv2.cvtColor(EP, cv2.COLOR_BGR2GRAY)
NR1 = cv2.cvtColor(NR1, cv2.COLOR_BGR2GRAY)
NR2 = cv2.cvtColor(NR2, cv2.COLOR_BGR2GRAY)
R2 = cv2.cvtColor(R2, cv2.COLOR_BGR2GRAY)
NR3=cv2.cvtColor(NR3, cv2.COLOR_BGR2GRAY)
FR=cv2.cvtColor(FR, cv2.COLOR_BGR2GRAY)
sword=cv2.cvtColor(sword, cv2.COLOR_BGR2GRAY)

#Базовая инициация
cap = cv2.VideoCapture("gwent.mp4")
frameRate = cap.get(cv2.CAP_PROP_FPS)

font=cv2.FONT_HERSHEY_COMPLEX

frameNumber=0
frameCounter=0
KUROK=0

#Нахождение "Ход оппонента/Ваш ход" Как работает
while (True):
    succ,frame=cap.read()

    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ssimS1=structural_sim(S1, frame[527:556, 857:1059])
    ssimS2=structural_sim(S2, frame[527:556, 857:1059])
    frameNumber += 1
    if (ssimS1 > 0.5) or (ssimS2 > 0.5):
        frameCounter+=1
        KUROK=1
    if (KUROK==1) and ((ssimS1 < 0.50) and (ssimS2 < 0.50)):
            command = "cd/d C:\project"
            subprocess.call(command, shell=True)
            command = "ffmpeg -y -ss " + str(round(((frameNumber-frameCounter)/frameRate), 1)) + " -i gwent.mp4 -c copy -t " + str(round((frameCounter)/frameRate, 1)) + " ANAL_G_R0_0" + ".mp4"
            subprocess.call(command, shell=True)
            break

    print("frameNumber", frameNumber)
    cv2.putText(frame,str(ssimS1),(400,400),font,1,(255,255,255),1)
    cv2.imshow("HUI",frame)
    if (cv2.waitKey(22) & 0xFF == ord('q')):
        break
# Фаза мулигана R1   #Инициация перед циклом - сбросить счетчики - инициировать RRR3_New чтоб не был пустой
KUROK = 0
frameCounter = 0
list=[]
RRR3_New=frame[508:568, 446:484]
while True:
    succ, frame = cap.read()
    frameNumber += 1
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    R1sei4as = frame[50:126, 804:1114]
    RRR3 = frame[508:568, 446:484]
    Crown2 = frame[36:82, 36:82]
    ssimCrown = structural_sim(Crown, Crown2)
    ssimR1 = structural_sim(R1,R1sei4as)
    ssimRRR3 = structural_sim(RRR3, RRR3_New)
    RRR3_New = RRR3

    if (ssimR1 > 0.40) and (ssimRRR3 < 0.75) :
        list.append(frameNumber)


    print("frameNumber",frameNumber)

    if (ssimR1 >= 0.40):
        frameCounter += 1
        if KUROK == 0:
            KUROK=1
    if ssimCrown >0.7:
        StartSec=(frameNumber - frameCounter + 20) / frameRate
        Duration = (80) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R1_0_0_Crown_Start" + ".mp4"
        subprocess.call(command, shell=True)
        for x in range(len(list)):
            StartSec = (list[x]-2) / frameRate
            Duration = (80) / frameRate
            command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R1_0_1_Crown_"+str(x)+ ".mp4"
            subprocess.call(command, shell=True)
        StartSec = (frameNumber - 800) / frameRate
        Duration = (880) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R1_0_2_Crown_END.mp4"
        subprocess.call(command, shell=True)
        break
    if (KUROK==1) and (ssimR1 < 0.4) and (ssimCrown < 0.6):
        StartSec=(frameNumber - frameCounter + 20) / frameRate
        Duration = (80) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R1_0_0_Crown_Start" + ".mp4"
        subprocess.call(command, shell=True)
        for x in range(len(list)):
            StartSec = (list[x]-2) / frameRate
            Duration = (80) / frameRate
            command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R1_0_1_Crown_"+str(x)+ ".mp4"
            subprocess.call(command, shell=True)
        StartSec = (frameNumber - 60) / frameRate
        Duration = (300) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R1_0_2_Crown_END_"+str(x+1) + ".mp4"
        subprocess.call(command, shell=True)
        break
# Actual Round 1
# #Инициация перед циклом - сбросить счетчики - инициировать ELA,MLA,ECC,MCC,EBS,MBS чтоб не был пустой
ELA2 = frame[232:256, 53:67]
MLA2 = frame[888:913, 53:67]
ECC2 = frame[29:52, 1822:1834]
MCC2 = frame[1031:1053, 1822:1834]
EBS2 = frame[353:396, 1824:1872]
MBS2 = frame[684:725, 1824:1872]
EC2 = frame[136:146, 1700:1710]
list=[]
list2=[]
coordinates = []
KUROK=0
frameCounter=0
while True:
    succ, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameNumber += 1
    frameCounter += 1
    ELA = frame[232:256, 53:67]
    MLA = frame[888:913, 53:67]
    ECC=frame[29:52,1822:1834]
    MCC=frame[1031:1053,1822:1834]
    EBS=frame[353:396,1824:1872]
    MBS=frame[684:725,1824:1872]
    Crown2=frame[36:82,36:82]
    MP2=frame[977:1017,883:1035]
    EP2=frame[53:92,883:1035]
    EC=frame[136:146,1700:1710]


    ssimELA = structural_sim(ELA,ELA2)
    ssimMLA = structural_sim(MLA,MLA2)
    ssimECC = structural_sim(ECC,ECC2)
    ssimMCC = structural_sim(MCC,MCC2)
    ssimEBS = structural_sim(EBS,EBS2)
    ssimMBS = structural_sim(MBS,MBS2)
    ssimCrown = structural_sim(Crown,Crown2)
    ssimMP=structural_sim(MP,MP2)
    ssimEP=structural_sim(EP,EP2)
    ssimEC=structural_sim(EC,EC2)

    ELA2 = ELA
    MLA2 = MLA
    ECC2 = ECC
    MCC2 = MCC
    EBS2 = EBS
    MBS2 = MBS
    EC2 = EC

    print("frameNumber", frameNumber)

    if ssimCrown<0.9:
        list.append(1)
    elif (ssimCrown>0.9) and (ssimECC<0.7):
        list.append(1)
    elif (ssimCrown>0.9) and (ssimMCC < 0.7):
        list.append(1)
    elif (ssimCrown>0.9) and (ssimEBS < 0.7):
        list.append(1)
    elif (ssimCrown>0.9) and (ssimMBS < 0.7):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimMLA < 0.7):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimELA < 0.7):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimEC < 0.5):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimMP > 0.4):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimEP > 0.4):
        list.append(1)
    else: list.append(0)

    if (ssimMP >0.4) and (ssimEP>0.4):
        list2=list.copy()
        for x in range(len(list)-1):
            if list[x] == 1:
                for x2 in range(min(330,(((len(list)-1)-x)))):
                    list2[x+x2]=1
        for x in range(len(list)):
            if (KUROK==0) and (list2[x]==1):
                coordinates.append(x)
                KUROK=1
            elif (KUROK==1) and (list2[x]==0):
                coordinates.append(x)
                KUROK=0
            elif (KUROK==1) and (x==(len(list)-1)):
                coordinates.append(x)
        for x in range(0, len(coordinates), 2):
            StartSec = (frameNumber + coordinates[x] - len(list) - 94) / frameRate
            Duration = (coordinates[x + 1] - coordinates[x] + 94) / frameRate
            command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R1_0_3" + str(x) + ".mp4"
            subprocess.call(command, shell=True)
        StartSec = (frameNumber - 300) / frameRate
        Duration = (600) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R1_0_3" + str(x+1) + ".mp4"
        subprocess.call(command, shell=True)

        break
# Поиск надписи "NEXT ROUND - ROUND 2"
while True:
    succ, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameNumber += 1
    NR1_2=frame[376:436,738:1136]
    NR2_2=frame[500:598,908:970]

    ssimNR = structural_sim(NR1,NR1_2)
    ssimNR2 = structural_sim(NR2,NR2_2)

    if (ssimNR > 0.4) and (ssimNR2 > 0.4):
        StartSec = (frameNumber - 20) / frameRate
        Duration = (70) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2" + ".mp4"
        subprocess.call(command, shell=True)
        break
#РАУНД 2 МУЛИГАН
KUROK = 0
frameCounter = 0
list=[]
RRR3_New=frame[508:568, 446:484]
while True:
    succ, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameNumber += 1
    R2_2 = frame[50:126, 804:1114]
    RRR3 = frame[508:568, 446:484]


    ssimR2 = structural_sim(R2,R2_2)
    ssimRRR3 = structural_sim(RRR3, RRR3_New)
    Crown2 = frame[36:82, 36:82]
    ssimCrown = structural_sim(Crown, Crown2)
    RRR3_New = RRR3

    if  (ssimR2 > 0.40) and (ssimRRR3 < 0.4) :
        list.append(frameNumber)


    print("frameNumber",frameNumber)

    # if (ssimR2 >= 0.60):
    #     frameCounter += 1
    #     if KUROK == 0:
    #         KUROK=1
    if ssimCrown >0.4:
        StartSec = (frameNumber - frameCounter + 20) / frameRate
        Duration = (80) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_0_Crown" + ".mp4"
        subprocess.call(command, shell=True)
        for x in range(len(list)):
            StartSec = (list[x]-2) / frameRate
            Duration = (80) / frameRate
            command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_1_Crown_"+str(x)+ ".mp4"
            subprocess.call(command, shell=True)
        StartSec = (frameNumber - 800) / frameRate
        Duration = (880) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_2_Crown.mp4"
        subprocess.call(command, shell=True)
        break
    # if (KUROK==1) and (ssimR2 < 0.6) and (ssimCrown < 0.1):
    #     StartSec=(frameNumber - frameCounter + 20) / frameRate
    #     Duration = (80) / frameRate
    #     command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_0" + ".mp4"
    #     subprocess.call(command, shell=True)
    #     for x in range(len(list)):
    #         StartSec = (list[x]-2) / frameRate
    #         Duration = (80) / frameRate
    #         command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_1_"+str(x)+ ".mp4"
    #         subprocess.call(command, shell=True)
    #     StartSec = (frameNumber - 60) / frameRate
    #     Duration = (300) / frameRate
    #     command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_2_"+str(x+1) + ".mp4"
    #     subprocess.call(command, shell=True)
    #     break
#ACTUAL ROUND 2
ELA2 = frame[232:256, 53:67]
MLA2 = frame[888:913, 53:67]
ECC2 = frame[29:52, 1822:1834]
MCC2 = frame[1031:1053, 1822:1834]
EBS2 = frame[353:396, 1824:1872]
MBS2 = frame[684:725, 1824:1872]
EC2 = frame[136:146, 1700:1710]
list=[]
list2=[]
coordinates = []
KUROK=0
frameCounter=0
while True:
    succ, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameNumber += 1
    frameCounter += 1
    ELA = frame[232:256, 53:67]
    MLA = frame[888:913, 53:67]
    ECC=frame[29:52,1822:1834]
    MCC=frame[1031:1053,1822:1834]
    EBS=frame[353:396,1824:1872]
    MBS=frame[684:725,1824:1872]
    Crown2=frame[36:82,36:82]
    MP2=frame[977:1017,883:1035]
    EP2=frame[53:92,883:1035]
    EC=frame[136:146,1700:1710]
    sword2 = frame[404:423, 735:756]
    ssimSword = structural_sim(sword,sword2)

    ssimELA = structural_sim(ELA,ELA2)
    ssimMLA = structural_sim(MLA,MLA2)
    ssimECC = structural_sim(ECC,ECC2)
    ssimMCC = structural_sim(MCC,MCC2)
    ssimEBS = structural_sim(EBS,EBS2)
    ssimMBS = structural_sim(MBS,MBS2)
    ssimCrown = structural_sim(Crown,Crown2)
    ssimMP=structural_sim(MP,MP2)
    ssimEP=structural_sim(EP,EP2)
    ssimEC=structural_sim(EC,EC2)

    ELA2 = ELA
    MLA2 = MLA
    ECC2 = ECC
    MCC2 = MCC
    EBS2 = EBS
    MBS2 = MBS
    EC2 = EC
    print("frameNumber", frameNumber)
    if ssimCrown<0.9:
        list.append(1)
    elif (ssimCrown>0.9) and (ssimECC<0.7):
        list.append(1)
    elif (ssimCrown>0.9) and (ssimMCC < 0.7):
        list.append(1)
    elif (ssimCrown>0.9) and (ssimEBS < 0.7):
        list.append(1)
    elif (ssimCrown>0.9) and (ssimMBS < 0.7):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimMLA < 0.7):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimELA < 0.7):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimEC < 0.5):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimMP > 0.4):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimEP > 0.4):
        list.append(1)
    else: list.append(0)

    if (ssimMP >0.4) and (ssimEP>0.4):
        list2=list.copy()
        for x in range(len(list)-1):
            if list[x] == 1:
                for x2 in range(min(330,(((len(list)-1)-x)))):
                    list2[x+x2]=1
        for x in range(len(list)):
            if (KUROK==0) and (list2[x]==1):
                coordinates.append(x)
                KUROK=1
            elif (KUROK==1) and (list2[x]==0):
                coordinates.append(x)
                KUROK=0
            elif (KUROK==1) and (x==(len(list)-1)):
                coordinates.append(x)
        if (len(coordinates) % 2) == 1:
            del coordinates[-1]
        for x in range(0, len(coordinates), 2):
            print(x)
            print(coordinates)
            StartSec = (frameNumber + coordinates[x] - len(list) - 94) / frameRate
            Duration = (coordinates[x + 1] - coordinates[x] + 94) / frameRate
            command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_3_" + str(x) + ".mp4"
            subprocess.call(command, shell=True)
        StartSec = (frameNumber - 300) / frameRate
        Duration = (600) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_3_" + str(x+1) + ".mp4"
        subprocess.call(command, shell=True)
        break
    if (ssimSword > 0.4):
        list2=list.copy()
        for x in range(len(list)-1):
            if list[x] == 1:
                for x2 in range(min(330,(((len(list)-1)-x)))):
                    list2[x+x2]=1
        for x in range(len(list)):
            if (KUROK==0) and (list2[x]==1):
                coordinates.append(x)
                KUROK=1
            elif (KUROK==1) and (list2[x]==0):
                coordinates.append(x)
                KUROK=0
            elif (KUROK==1) and (x==(len(list)-1)):
                coordinates.append(x)
        if (len(coordinates) % 2) == 1:
            del coordinates[-1]
        for x in range(0, len(coordinates), 2):
            StartSec = (frameNumber + coordinates[x] - len(list) - 94) / frameRate
            Duration = (coordinates[x + 1] - coordinates[x] + 94) / frameRate
            command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_3_Sword_" + str(x) + ".mp4"
            subprocess.call(command, shell=True)
        StartSec = (frameNumber - 600) / frameRate
        Duration = min((2600),int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-frameNumber) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R2_0_3_Sword_" + str(x+1) + ".mp4"
        subprocess.call(command, shell=True)
        sys.exit()

#НАДПИСЬ Р3
frameCounter=0
while True:
    frameNumber += 1
    succ, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    NR1_2=frame[376:436,738:1136]
    NR3_2=frame[500:598,908:970]

    redraws2 = frame[506:526, 263:283]


    ssimNR = structural_sim(NR1,NR1_2)
    ssimNR3 = structural_sim(NR3,NR3_2)

    if (ssimNR > 0.4) and (ssimNR3 > 0.4):
        StartSec = (frameNumber - 20) / frameRate
        Duration = (70) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3" + ".mp4"
        subprocess.call(command, shell=True)
        break

#РАУНД 3 МУЛИГАН
KUROK = 0
frameCounter = 0
list=[]
RRR3_New=frame[508:568, 446:484]
while True:
    succ, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameNumber += 1
    FR_2 = frame[58:128, 728:1194]
    RRR3 = frame[508:568, 446:484]
    Crown2 = frame[36:82, 36:82]
    ssimCrown = structural_sim(Crown, Crown2)
    ssimFR = structural_sim(FR,FR_2)
    ssimRRR3 = structural_sim(RRR3, RRR3_New)
    RRR3_New = RRR3

    if  (ssimFR > 0.40) and (ssimRRR3 < 0.75) :
        list.append(frameNumber)


    print("frameNumber",frameNumber)

    # if (ssimR2 >= 0.60):
    #     frameCounter += 1
    #     if KUROK == 0:
    #         KUROK=1
    if ssimCrown >0.8:
        StartSec=(frameNumber - frameCounter + 20) / frameRate
        Duration = (80) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_0_Crown" + ".mp4"
        subprocess.call(command, shell=True)
        for x in range(len(list)):
            StartSec = (list[x]-2) / frameRate
            Duration = (80) / frameRate
            command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_1_Crown"+str(x)+ ".mp4"
            subprocess.call(command, shell=True)
        StartSec = (frameNumber - 800) / frameRate
        Duration = (880) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_2_Crown.mp4"
        subprocess.call(command, shell=True)
        break
    # if KUROK==1 and (ssimR2 < 0.6) and (ssimCrown < 0.1):
    #     StartSec=(frameNumber - frameCounter + 20) / frameRate
    #     Duration = (80) / frameRate
    #     command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_0" + ".mp4"
    #     subprocess.call(command, shell=True)
    #     for x in range(len(list)):
    #         StartSec = (list[x]-2) / frameRate
    #         Duration = (80) / frameRate
    #         command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_1_"+str(x)+ ".mp4"
    #         subprocess.call(command, shell=True)
    #     StartSec = (frameNumber - 60) / frameRate
    #     Duration = (300) / frameRate
    #     command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_2_"+str(x+1) + ".mp4"
    #     subprocess.call(command, shell=True)
    #     break

#ACTUAL ROUND 3
ELA2 = frame[232:256, 53:67]
MLA2 = frame[888:913, 53:67]
ECC2 = frame[29:52, 1822:1834]
MCC2 = frame[1031:1053, 1822:1834]
EBS2 = frame[353:396, 1824:1872]
MBS2 = frame[684:725, 1824:1872]
EC2 = frame[136:146, 1700:1710]
list=[]
list2=[]
coordinates = []
KUROK=0
frameCounter=0
while True:
    succ, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameNumber += 1
    frameCounter += 1
    ELA = frame[232:256, 53:67]
    MLA = frame[888:913, 53:67]
    ECC=frame[29:52,1822:1834]
    MCC=frame[1031:1053,1822:1834]
    EBS=frame[353:396,1824:1872]
    MBS=frame[684:725,1824:1872]
    Crown2=frame[36:82,36:82]
    MP2=frame[977:1017,883:1035]
    EP2=frame[53:92,883:1035]
    EC=frame[136:146,1700:1710]
    sword2 = frame[404:423, 735:756]

    ssimELA = structural_sim(ELA,ELA2)
    ssimMLA = structural_sim(MLA,MLA2)
    ssimECC = structural_sim(ECC,ECC2)
    ssimMCC = structural_sim(MCC,MCC2)
    ssimEBS = structural_sim(EBS,EBS2)
    ssimMBS = structural_sim(MBS,MBS2)
    ssimCrown = structural_sim(Crown,Crown2)
    ssimMP=structural_sim(MP,MP2)
    ssimEP=structural_sim(EP,EP2)
    ssimEC=structural_sim(EC,EC2)
    ssimSword = structural_sim(sword,sword2)

    ELA2 = ELA
    MLA2 = MLA
    ECC2 = ECC
    MCC2 = MCC
    EBS2 = EBS
    MBS2 = MBS
    EC2 = EC
    print("frameNumber", frameNumber)
    if ssimCrown<0.9:
        list.append(1)
    elif (ssimCrown>0.9) and (ssimECC<0.7):
        list.append(1)
    elif (ssimCrown>0.9) and (ssimMCC < 0.7):
        list.append(1)
    elif (ssimCrown>0.9) and (ssimEBS < 0.7):
        list.append(1)
    elif (ssimCrown>0.9) and (ssimMBS < 0.7):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimMLA < 0.7):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimELA < 0.7):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimEC < 0.5):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimMP > 0.4):
        list.append(1)
    elif (ssimCrown > 0.9) and (ssimEP > 0.4):
        list.append(1)
    else: list.append(0)

    if (ssimMP >0.4) and (ssimEP>0.4):
        list2=list.copy()
        for x in range(len(list)-1):
            if list[x] == 1:
                for x2 in range(min(330,(((len(list)-1)-x)))):
                    list2[x+x2]=1
        for x in range(len(list)):
            if (KUROK==0) and (list2[x]==1):
                coordinates.append(x)
                KUROK=1
            elif (KUROK==1) and (list2[x]==0):
                coordinates.append(x)
                KUROK=0
            elif (KUROK==1) and (x==(len(list)-1)):
                coordinates.append(x)
        for x in range(0, len(coordinates), 2):
            StartSec = (frameNumber + coordinates[x] - len(list) - 94) / frameRate
            Duration = (coordinates[x + 1] - coordinates[x] + 94) / frameRate
            command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_3_" + str(x) + ".mp4"
            subprocess.call(command, shell=True)
        StartSec = (frameNumber - 300) / frameRate
        Duration = min((2600),int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-frameNumber) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_3_" + str(x+1) + ".mp4"
        subprocess.call(command, shell=True)

        break
    if ssimSword > 0.4:
        list2=list.copy()
        for x in range(len(list)-1):
            if list[x] == 1:
                for x2 in range(min(330,(((len(list)-1)-x)))):
                    list2[x+x2]=1
        for x in range(len(list)):
            if (KUROK==0) and (list2[x]==1):
                coordinates.append(x)
                KUROK=1
            elif (KUROK==1) and (list2[x]==0):
                coordinates.append(x)
                KUROK=0
            elif (KUROK==1) and (x==(len(list)-1)):
                coordinates.append(x)
        for x in range(0, len(coordinates), 2):
            StartSec = (frameNumber + coordinates[x] - len(list) - 94) / frameRate
            Duration = (coordinates[x + 1] - coordinates[x] + 94) / frameRate
            command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_3_Sword_" + str(x) + ".mp4"
            subprocess.call(command, shell=True)
        StartSec = (frameNumber - 600) / frameRate
        Duration = min((2600),int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-frameNumber) / frameRate
        command = "ffmpeg -y -ss " + str(round(StartSec, 1)) + " -i gwent.mp4 -c copy -t " + str(round(Duration, 1)) + " ANAL_G_R3_0_3_Sword_" + str(x+1) + ".mp4"
        subprocess.call(command, shell=True)




print("--- %s seconds ---" % (time.time() - start_time))