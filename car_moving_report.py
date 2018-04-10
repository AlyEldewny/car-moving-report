
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1, 1, 1, 1)   # clear background
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10, 10, 10 ,0, 0, 0, 0, 1, 0)

x=0
angle=0
y=0

#white-route###
def signs(z):
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(z-y , 0, 1)
    glScale(1.5, 0.1, 0.5)
    glutSolidCube(2)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global y
    ###route###
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-y, 1.25, 2)
    glScale(30, 0.5, 2.75)
    glutSolidCube(3)


    for z in range (-50,20,8):
        signs(z)

    ### car###
    glLoadIdentity()
    glColor3f(0.65, 1, 0)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glTranslate(x,.25*5,0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

### torus###
    global angle
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*.25,2.5*0.5)
    glRotatef(angle,0,0,1)
    glutWireTorus(0.125,.5,12,8)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x+2.5, -2.5 * .25, -2.5 * 0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, .5, 12, 8)


    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * .25, 2.5 * 0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, .5, 12, 8)

###car move###
    if x <= 15:
       x+=0.005
       angle-=0.25
    else:
        x=-20


    if y<=7:
       y+=0.005
    else:
       y=0


    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Moving_Car_report")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()
