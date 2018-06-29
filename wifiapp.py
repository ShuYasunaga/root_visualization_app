# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys


DATA = []

ii = 0
def draw():
    global ii
    # アクセスするURL
    url = "http://192.168.100.125/"

    # URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
    instance = urllib2.urlopen(url)

    # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
    soup = BeautifulSoup(instance, "html.parser")

    data = soup.find_all("h1")
    cnt = 0
    Data = []
    for i in data:
       Data.append(str(i).replace('analog input ','').replace(str(cnt),'').replace(' is ','').replace('<h1>','').replace('</h1>','').replace('</h>','').replace('<h>',''))
       print(str(i).replace('analog input ','').replace(str(cnt),'').replace(' is ','').replace('<h1>','').replace('</h1>','').replace('</h>','').replace('<h>','')),
       if cnt != 6:
           print(","),
       cnt = cnt+1
    DATA.append(Data)
    #print("")
    print "data0 : ",
    try:

        c = (1000.0 - float(DATA[ii][0]))/1000
        cc = float(DATA[ii][0])/1000
        print 'c: ',
        print c,
        print ",",
        print cc
        # 座標(0.25,0.25)から幅0.5,高さ0.5の四角形を描く
        x,y,w,h = 0.25,0.25,0.5,0.5
        glClear(GL_COLOR_BUFFER_BIT)
        # 四角形の色(緑)
        glColor3f(c/2, c, c)
        glBegin(GL_POLYGON)
        # 四角形の頂点座標
        glVertex3f(x,   y,   0.0)
        glVertex3f(x+w, y,   0.0)
        glVertex3f(x+w, y+h, 0.0)
        glVertex3f(x,   y+h, 0.0)
        glEnd()
        glFlush()
        glutPostRedisplay();
    except:
        pass

    time.sleep(5)
    ii = ii+1

# 初期化
def init():
    # 画面の色
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)

def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) # 表示設定
    glutInitWindowSize(400, 400)        # 画面サイズ
    glutInitWindowPosition(100, 100)    # 画面の表示位置
    glutCreateWindow("TEST")            # ウィンドウの名前
    init()                              # 初期化
    glutDisplayFunc(draw)               # 描画
    glutMainLoop()

if __name__ == "__main__":

    main()
