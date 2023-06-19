# Object Modeling Example Code

from __future__ import division
import traceback
import random

from cars import *
from houses import *
from environment import *

time = 0   # time is used to move objects from one frame to another
seed = 66


def setup():
    size (1000, 1000, P3D)
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    global seed
    random.seed(seed)
    try:
        global time
        time += 0.005

        camera (0 , -50, 300, # translate
                0 , 0, 0, # rotate
                0,  1, 0)  # up/down

        background (250, 200, 100)  # clear screen and set background to light blue
        
        # set up the lights
        ambientLight(200, 200, 200);
        lightSpecular(255, 255, 255)
        directionalLight (50, 50, 50, -0.5, 0.5, -1)
        
        # set some of the surface properties
        noStroke()
        specular (25, 25, 25)
        shininess (15.0)
    
        # draw scenes
        
        if time <= 2.335:
            drawScene1()
        
        elif time > 2.335 and time <= 5.1:
            drawScene2(2.335)
            
        elif time > 5.1 and time <= 12.7:
            drawScene3(5.1)
        
        elif time > 12.7:
            time = 0
        
        '''
        if time >= 2:
            seed = 20
            camera (0 , -100, 200, # translate
                200 , 100, 0, # rotate
                0,  1, 0)  # up/down
            drawScene2()
        else:
            drawScene2()
        '''

    except Exception: 
        traceback.print_exc()


def drawScene1(offset=0):
    global seed
    seed = 15
    
    # movement values
    xtranslate = 50
    ytranslate = 30
    ztranslate = 0
    
    xrotate = 0
    yrotate = 0
    zrotate = 0
    
    # camera
    camera (400 + (xtranslate * time), -200 + (ytranslate * time), 100, # translate
            00 , 450, 95, # rotate
            0,  1, 0)  # up/down
    
    # road
    for i in range(7):
        spawn (9, i * 100, 100)
        
        # sidewalk
        spawn (16, i * 100, 55)
        spawn (16, i * 100, 145)
        
    # foliage
    for i in range (7):
        spawn (random.randint(13, 15), (i * 100) - 50, 0, -1.5708)
        if i < 3: spawn (random.randint(13, 15), (i * 100) - 50, 200, -1.5708)
    
    # grass
    for i in range (7):
        spawn (8, i * 100, 0)
        spawn (8, i * 100, 200)

    # turbine
    spawn (18, 300, 200, 3.14159)
    
    # citizen
    carspeed = 200
    pushMatrix()
    translate (50 + (carspeed * time), 0, 120)
    citizen()
    popMatrix()
    
def drawScene2(offset=0):
    global seed
    seed = 15
    localtime = time - offset
    
    # movement values
    xtranslate = 20
    ytranslate = 0
    ztranslate = 0
    
    xrotate = 20
    yrotate = 0
    zrotate = 0
    
    # camera
    camera (350 + (xtranslate * localtime), -30, -50, # translate
            250 + (xrotate * localtime), 0, 100, # rotate
            0,  1, 0)  # up/down
    
    # road
    for i in range(5):
        spawn (9, i * 100, 100)
        
        # sidewalk
        spawn (16, i * 100, 55)
        spawn (16, i * 100, 145)
        
    # foliage
    for i in range (5):
        spawn (random.randint(13, 15), (i * 100) + 150, 200, -1.5708)
    
    # grass
    for i in range (5):
        spawn (8, i * 100, 0)
        spawn (8, i * 100, 200)
        
    # billboard
    spawn (17, 300, 0, 1.5708)
    
    # turbine
    spawn (18, 300, 200, 3.14159)
    
    # cop
    spawn (118, 380, -10, -1.5708)

    
    # citizen
    if time <= 5:
        carspeed = 300
        pushMatrix()
        translate (50 + (carspeed * localtime), 0, 120) # should be z=120
        citizen()
        popMatrix()

    
def drawScene3(offset=0):
    global seed
    seed = 52
    localtime = time - offset
    
    # movement values
    xtranslate = 75
    ytranslate = 5
    ztranslate = 0
    
    xrotate = 20
    yrotate = 0
    zrotate = 0
    
    camera (500 + (xtranslate * localtime), -50 + (ytranslate * localtime), 200, # translate
                100 + (xrotate * localtime), 150, 0, # rotate
                0,  1, 0)  # up/down
    
    # houses
    for i in range (6):
        spawn (random.randint(1, 6), i * 100, 0)
        
    for i in range (3):
        spawn (random.randint(1, 6), (i * 100) + 700, 0)
        
    # foliage
    for i in range (6):
        spawn (random.randint(11, 13), (i * 100) - 50, 0)
        spawn (random.randint(14, 15), (i * 100) - 50, 200 + random.randint(-10, 15), -1.5708)
    
    # grass
    for i in range (6):
        spawn (8, i * 100, 0)
        spawn (8, i * 100, -100)
        
        spawn (8, i * 100, 200)
    
    # grass contd.
    for i in range (5):
        spawn (8, (i * 100) + 700, 0)
        spawn (8, (i * 100) + 700, -100)
        
        spawn (8, (i * 100) + 700, 200)
        
    # road
    for i in range (6):
        spawn (9, (i * 100) + 10, 100)
        
        # sidewalk
        spawn (16, i * 100, 55)
        spawn (16, i * 100, 145)
    
    # cross road
    for i in range (7):
        spawn (9, 600, (i * 100) - 200, 1.5708)
    
    for i in range (3):
        # sidewalk
        spawn (16, 555, (i * 100)+ 190, 1.5708)
        spawn (16, 555, (i * 100)- 190, 1.5708)
        
        spawn (16, 645, (i * 100)+ 190, 1.5708)
        spawn (16, 645, (i * 100)- 190, 1.5708)
        
    # road contd.
    for i in range(5):
        spawn (9, (i * 100) + 690, 100)
        
        #sidewalk
        spawn (16, (i * 100) + 690, 55)
        spawn (16, (i * 100) + 690, 145)
    
    # water
    spawn (10, 800, 200)
    
    # car
    carspeed = 150
    pushMatrix()
    translate (300 + (carspeed * localtime), 0, 130)
    citizen()
    popMatrix()
    
    # police
    carspeed = 180
    pushMatrix()
    if (localtime <= 2.25):
        translate (100 + (carspeed * localtime), 0, 130)
    else:
        translate (505, 0, 130)
    police()
    popMatrix()
    
    # bus
    busspeed = 100
    pushMatrix()
    delay = 1.45
    if (localtime <= delay):
        translate (580, 0, 0)
    else:
        translate (580, 0, 0  + (busspeed * (localtime - delay)))
        print (localtime)
    rotateY (-1.5708)
    bus()
    popMatrix()
    
    pushMatrix()
    if (localtime <= delay):
        translate (580, 0, 0)
    else:
        translate (580, 0, -100  + (busspeed * (localtime - delay)))
    rotateY (-1.5708)
    bus()
    popMatrix()
    
    pushMatrix()
    if (localtime <= delay):
        translate (580, 0, 0)
    else:
        translate (580, 0, -200  + (busspeed * (localtime - delay)))
    rotateY (-1.5708)
    bus()
    popMatrix()
    
    pushMatrix()
    if (localtime <= delay):
        translate (580, 0, 0)
    else:
        translate (580, 0, -300  + (busspeed * (localtime - delay)))
    rotateY (-1.5708)
    bus()
    popMatrix()
    
    pushMatrix()
    if (localtime <= delay):
        translate (580, 0, 0)
    else:
        translate (580, 0, -400  + (busspeed * (localtime - delay)))
    rotateY (-1.5708)
    bus()
    popMatrix()

'''
HOUSES:
    1 = house1
    2 = house2
    3 = house3
    4 = house4
    5 = house5
    6 = house6
    7 = garage

ENVIRONMENT:
    8 = grass
    9 = road
    10 = water
    11 = plant1
    12 = plant2
    13 = tree
    14 = light
    15 = power
    16 = sidewalk
    17 = billboard
    18 = turbine

CAR:
    117 = citizen
    118 = police, 12 is alr taken :)
    119 = bus
'''
def spawn(item, x, z, ry = 0):
    if item == 8:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        grass(True)
        popMatrix()
        
    if item == 1:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        house1()
        popMatrix()
        
    if item == 2:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        house2()
        popMatrix()
    
    if item == 3:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        house3()
        popMatrix()
        
    if item == 4:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        house4()
        popMatrix()
        
    if item == 5:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        house5()
        popMatrix()
    
    if item == 6:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        house6()
        popMatrix()
        
    if item == 7:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        garage()
        popMatrix()
        
    if item == 9:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        road()
        popMatrix()
        
    if item == 10:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        water()
        popMatrix()
        
    if item == 11:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        plant1()
        popMatrix()
        
    if item == 12:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        plant2()
        popMatrix()
        
    if item == 13:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        tree()
        popMatrix()
    
    if item == 14:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        light()
        popMatrix()
        
    if item == 15:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        power()
        popMatrix()
        
    if item == 16:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        sidewalk()
        popMatrix()
        
    if item == 17:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        billboard()
        popMatrix()
        
    if item == 18:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        turbine(time)
        popMatrix()
        
    if item == 117:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        citizen()
        popMatrix()
        
    if item == 118:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        police()
        popMatrix()
        
    if item == 119:
        pushMatrix()
        translate (x, 0, z)
        rotateY(ry)
        bus()
        popMatrix()
