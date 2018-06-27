# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
import time
import numpy as np
import pygame
from pygame.locals import *
import serial
import csv
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import threading
import datetime
import json
import boto3
import commands
import os
print os.getcwd()
print os.chdir(sys.path[0])
print os.getcwd()
import urllib2
from bs4 import BeautifulSoup
import time
#bucket_name = "soildb"
#s3 = boto3.resource('s3')
#print os.path.realpath(os.path.dirname(sys.argv[0]))

d = datetime.datetime.today()
filename =  d.strftime("%Y-%m-%d_%H:%M")+".csv"
#with open(filename,"w"):pass
#os.chmod(filename,0777)
#filename2 = d.strftime("%Y-%m-%d_%H:%M")+".csv"
#filename = "A.csv"
#print filename
cnt  = 0
#ser=serial.Serial("/dev/ttyUSB0",9600)
#f = open('20180310.csv','w')
#writer = csv.writer(f)
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QComboboxSample')

        self.combo = QComboBox(self)
        self.combo.addItem("A")
        self.combo.addItem("B")
        self.combo.addItem("C")

        self.show()


#f.close()
def display():

    f = open(filename,'w')
    writer = csv.writer(f)
    global cnt

    i = 0
    B = []
    Heat_d_A = []
    Heat_d_B = []
    Heat_d_C = []
    data2 = []
    data3 = []
    cnt = 0
    while(1):
        try:
            #print("start")

            url = "http://192.168.100.125/"

            # URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
            instance = urllib2.urlopen(url)

            # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
            soup = BeautifulSoup(instance, "html.parser")

            data = soup.find_all("h1")
            data2=[]
            #print data
            #print('size'),
            #print len(data)

            Data = []
            #data2=[]
            d2_ = datetime.datetime.today()
            print d2_.strftime("%Y-%m-%d_%H:%M:%S"),
            print": ",
            data2.append(d2_)
            for i in data:
               #print "i: ",
               #print i
               #print(str(i).replace('<h1>','').replace('</h1>','').replace('</h>','').replace('<h>','')),
               d=str(i).replace('<h1>','').replace('</h1>','').replace('</h>','').replace('<h>','')
               #print(type(d))
               d=int(d)

               print(d),
               #print(type(d))
               data2.append(d)
               if cnt != 6:
                   print(","),
               #cnt = cnt+1
            #data2.append(Data)
            # 248 168 133    97  65  52
            #149 65 28   58  25  4
            #58 25 11
            writer.writerow(data2)
            for iii in range(1,len(data2)):
                heat_d_A = 0.30
                heat_d_B = 0.12
                heat_d_C = 0.07
                if data2[iii] > 900:
                    heat_d_A = 0.10
                    heat_d_B = 0.04
                    heat_d_C = 0
                elif data2[iii] > 800:
                    heat_d_A = heat_d_A+0.053*1
                    heat_d_B = heat_d_B+0.051*1
                    heat_d_C = heat_d_C+0.041*1
                elif data2[iii] > 700:
                    heat_d_A = heat_d_A+0.054*3
                    heat_d_B = heat_d_B+0.051*3
                    heat_d_C = heat_d_C+0.041*3
                elif data2[iii] > 600:
                    heat_d_A = heat_d_A+0.055*4
                    heat_d_B = heat_d_B+0.051*4
                    heat_d_C = heat_d_C+0.041*4
                elif data2[iii] > 500:
                    heat_d_A = heat_d_A+0.056*5
                    heat_d_B = heat_d_B+0.051*5
                    heat_d_C = heat_d_C+0.041*5
                elif data2[iii] > 400:
                    heat_d_A = heat_d_A+0.057*6
                    heat_d_B = heat_d_B+0.051*6
                    heat_d_C = heat_d_C+0.041*6
                elif data2[iii] > 300:
                    heat_d_A = heat_d_A+0.058*7
                    heat_d_B = heat_d_B+0.051*7
                    heat_d_C = heat_d_C+0.041*7
                elif data2[iii] > 200:
                    heat_d_A = heat_d_A+0.059*8
                    heat_d_B = heat_d_B+0.051*8
                    heat_d_C = heat_d_C+0.041*8
                elif data2[iii] > 100:
                    heat_d_A = heat_d_A+0.06*9
                    heat_d_B = heat_d_B+0.051*9
                    heat_d_C = heat_d_C+0.041*9
                else:
                    heat_d_A = heat_d_A+0.061*10
                    heat_d_B = heat_d_B+0.051*10
                    heat_d_C = heat_d_C+0.041*10
                #print heat_d_A,
                #print heat_d_B,
                #print heat_d_C
                Heat_d_A.append(heat_d_A)
                Heat_d_B.append(heat_d_B)
                Heat_d_C.append(heat_d_C)
            #print(Heat_d_A)
            glClear(GL_COLOR_BUFFER_BIT)

            glEnableClientState(GL_VERTEX_ARRAY)

            base1 = 0.5

            for i in range(1,8):
                c=7-i
                base2 = base1 -0.01
                base1 = base1-0.20

                glColor3f(Heat_d_A[c], Heat_d_B[c], Heat_d_C[c])
                glVertexPointerf(np.array([
                    [-0.8,  base1, 0.0],
                    [-0.8, base2, 0.0],
                    [ 0.8,  base1, 0.0],
                    [ 0.8, base2, 0.0],
                    ], dtype=np.float))
                glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

            SCREEN_SIZE = (405, 850)

            pygame.init()

            screen_rect = Rect(245, 0, 480, 900)
            #screen = pygame.display.set_mode(screen_rect.size)
            screen = pygame.display.set_mode(SCREEN_SIZE)

            pygame.display.set_caption("Hello, world!")
            cnt2 = str(cnt)
            sysfont = pygame.font.SysFont(None, 40)
            hello00 = sysfont.render(filename, True, (0,0,0))
            sysfont = pygame.font.SysFont(None, 80)
            hello0 = sysfont.render(cnt2, True, (0,0,0))
            hello2 = sysfont.render(str(data2[7]), True, (0,0,0))
            hello3 = sysfont.render(str(data2[6]), True, (0,0,0))
            hello4 = sysfont.render(str(data2[5]), True, (0,0,0))
            hello5 = sysfont.render(str(data2[4]), True, (0,0,0))
            hello6 = sysfont.render(str(data2[3]), True, (0,0,0))
            hello7 = sysfont.render(str(data2[2]), True, (0,0,0))
            hello8 = sysfont.render(str(data2[1]), True, (0,0,0))


            screen.fill((255,255,255))
            screen.blit(hello00, (50,0))
            screen.blit(hello0, (50,100))
            screen.blit(hello2, (50,250))
            screen.blit(hello3, (50,315))
            screen.blit(hello4, (50,380))
            screen.blit(hello5, (50,445))
            screen.blit(hello6, (50,510))
            screen.blit(hello7, (50,575))
            screen.blit(hello8, (50,640))
            data2 = []
            data3 = []

            pygame.display.update()
            glFlush()
            cnt = cnt +1
            print cnt
            Heat_d_A = []
            Heat_d_B = []
            Heat_d_C = []

        except:
            pass
        time.sleep(0.1)
def init():
    # 画面の色
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)

def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(300, 700)
    glutInitWindowPosition(210, 0)
    glutCreateWindow(b"sample2")
    glutDisplayFunc(display)
    #glClearColor(0.58, 0.25, 0.11, 0.0)
    glClearColor(0.97, 0.67, 0.52, 0.0)

    app = QApplication(sys.argv)
    #ui = UI()
    #app.exec_()
    #pyqtapp = threading.Thread(target=UI)
    #pyqtapp.start()

    glutMainLoop()
    app.exec_()

if __name__ == "__main__":
    main()
