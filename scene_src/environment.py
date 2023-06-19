from cylinder import *
import random

def tree():
    pushMatrix()
    translate (0, -30, 0)
    scale (0.9)
    
    # main
    fill (110, 200, 50)
    pushMatrix()
    translate(0, -2, 0)
    box (17, 20, 17)
    popMatrix()
    
    # shrubs
    fill (150, 200, 50)
    pushMatrix()
    translate (5, -2, 5)
    box(10, 10, 10)
    popMatrix()
    
    pushMatrix()
    translate (-5, -7, -7)
    box(10, 15, 7)
    popMatrix()
    
    # trunk
    fill (185, 100, 55)
    pushMatrix()
    translate(0, 20, 0)
    box (3.5, 25, 3.5)
    popMatrix()
    
    fill (165, 95, 55)
    pushMatrix()
    translate (2, 20, -2)
    box (2, 7, 2)
    popMatrix()
    
    popMatrix()
    
def water():
    pushMatrix()
    translate (0, -55, 0)
    scale (1.5)
    
    #main
    fill (115, 160, 200)
    pushMatrix()
    translate (0, -5, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=12, r2=12, h=20)
    popMatrix()
    
    #accent
    fill (95, 140, 180)
    pushMatrix()
    translate (0, -17, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=5, r2=12, h=5)
    popMatrix()
    
    # legs
    fill (120, 100, 55)
    pushMatrix()
    translate (9, 20, 5)
    box (1, 35, 1)
    popMatrix()
    
    pushMatrix()
    translate (-9, 20, 5)
    box (1, 35, 1)
    popMatrix()
    
    pushMatrix()
    translate (9, 20, -5)
    box (1, 35, 1)
    popMatrix()
    
    pushMatrix()
    translate (-9, 20, -5)
    box (1, 35, 1)
    popMatrix()
    
    popMatrix()
    
def light():
    pushMatrix()
    translate (0, -20, 0)
    scale (0.8)
    
    # main
    fill (155, 165, 180)
    pushMatrix()
    box (1.5, 30, 1.5)
    popMatrix()
    
    # base
    fill (125, 115, 140)
    pushMatrix()
    translate (0, 20, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=2, r2=2.5, h=10)
    popMatrix()
    
    # cap
    pushMatrix()
    translate (0, -19, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=2.5, r2=4, h=3)
    popMatrix()

    pushMatrix()
    translate (0, -20, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=2.5, r2=3, h=3)
    popMatrix()
        
    # bulb
    fill (255, 230, 35)
    pushMatrix()
    translate (0, -15, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=4, r2=3, h=7)
    popMatrix()
    
    popMatrix()
    
def plant1():
    pushMatrix()
    translate (0, -5, 0)
    scale (0.8)
    
    # main
    fill (125, 120, 110)
    pushMatrix()
    rotateX(-1.5708)
    cylinder (sides=8, r1=10, r2=8, h=15)
    popMatrix()
    
    # dirt
    fill (255, 200, 165)
    pushMatrix()
    translate (0, -0.5, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=8, r2=6, h=15)
    popMatrix()
    
    # plant
    fill (150, 200, 100)
    pushMatrix()
    translate (0, -10, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=7, r2=3, h=10)
    popMatrix()
    
    popMatrix()
    
def plant2():
    pushMatrix()
    translate (0, -5, 0)
    scale (0.8)
    
    # main
    fill (125, 120, 110)
    pushMatrix()
    rotateX(-1.5708)
    cylinder (sides=8, r1=10, r2=8, h=15)
    popMatrix()
    
    # dirt
    fill (255, 200, 165)
    pushMatrix()
    translate (0, -0.5, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=8, r2=6, h=15)
    popMatrix()
    
    # plant
    fill (150, 200, 100)
    pushMatrix()
    translate (0, -20, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=7, r2=7, h=15)
    cylinder (sides=8, r1=5, r2=5, h=20)
    popMatrix()
    
    # trunk
    fill (185, 100, 55)
    pushMatrix()
    translate(0, -10, 0)
    box (2, 20, 2)
    popMatrix()
    
    popMatrix()
    
def power():
    pushMatrix()
    translate (0, -30, 0)
    scale (1.15)
    
    # main
    fill (190, 170, 150)
    pushMatrix()
    box (2, 55, 2)
    popMatrix()

    # bars
    fill (170, 150, 120)
    pushMatrix()
    translate (0, -25, 1.5)
    rotateZ(1.5708)
    box (2, 15, 1)
    popMatrix()
    
    pushMatrix()
    translate (0, -21, 1.5)
    rotateZ(1.5708)
    box (2, 15, 1)
    popMatrix()
    
    # lines
    fill (200)
    
    # capacitor
    fill (165, 165, 180)
    pushMatrix()
    translate (2, -10, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=2, r2=2, h=10)
    popMatrix()
    
    pushMatrix()
    translate (-2, -15, 0)
    rotateX(-1.5708)
    cylinder (sides=8, r1=2, r2=2, h=7)
    popMatrix()
    
    popMatrix()
 
def billboard():
    pushMatrix()
    scale (1, 1, 1)
    
    pushMatrix()
    translate (0, -25, 0)
    
    # main
    fill (190, 170, 150)
    pushMatrix()
    box (70, 30, 2)
    popMatrix()
    
    # legs
    fill (170, 150, 120)
    pushMatrix()
    translate (30, 15, 0)
    box (5, 15, 5)
    popMatrix()
    
    pushMatrix()
    translate (-30, 15, 0)
    box (5, 15, 5)
    popMatrix()
    
    # image
    fill (245, 245, 245)
    pushMatrix()
    translate (0, 0, 1)
    box (50, 17, 2)
    popMatrix()
    
    # lights
    fill (245, 200, 0)
    pushMatrix()
    translate (0, -12, 1)
    box(20, 3, 3)
    popMatrix()
    
    popMatrix()
    
    popMatrix()

def turbine(t, speed=2):
    pushMatrix()
    translate (0, -27, 0)
    
    # main
    fill (245)
    pushMatrix()
    rotateX(-1.5708)
    cylinder (sides=9, r1=3, r2=6, h=50)
    popMatrix()
    
    # head
    fill (245)
    pushMatrix()
    translate (0, -25, -1)
    rotateY(3.14159)
    cylinder (sides=6, r1=3, r2=4, h=12)
    popMatrix()
    
    fill (220, 205, 228)
    pushMatrix()
    translate (0, -25, 5)
    rotateY(3.14159)
    cylinder (sides=6, r1=3, r2=3, h=5)
    popMatrix()
    
    # fan
    pushMatrix()
    translate (0, -25, 7)
    rotateZ(-t*speed)
    fan()
    popMatrix()
    
    # base
    fill (165, 155, 180)
    pushMatrix()
    translate (0, 20, 0)
    rotateX(-1.5708)
    cylinder (sides=9, r1=8, r2=9, h=10)
    popMatrix()
    
    popMatrix()
    
def fan():
    # blades
    fill (245)
    pushMatrix()
    translate (12, 0, 0)
    box (25, 5, 1)
    popMatrix()
    
    pushMatrix()
    translate (-12, 0, 0)
    box (25, 5, 1)
    popMatrix()
    
    pushMatrix()
    translate (0, 12, 0)
    rotateZ(1.5708)
    box (25, 5, 1)
    popMatrix()
    
    pushMatrix()
    translate (0, -12, 0)
    rotateZ(1.5708)
    box (25, 5, 1)
    popMatrix()
    
    # tip
    fill (220, 205, 228)
    pushMatrix()
    translate (0, 0, 1.5)
    rotateY(3.14159)
    cylinder (sides=6, r1=1, r2=3, h=7)
    popMatrix()
     
def road():
    # tar
    fill (80, 90, 110)
    pushMatrix()
    box (100, 1, 80)
    popMatrix()
    
    # line
    fill (220)
    pushMatrix()
    translate (0, -0.5, 0)
    box (70, 1, 2)
    popMatrix()
    
def sidewalk():
    fill (255)
    pushMatrix()
    box (100, 1, 10)
    popMatrix()
    
def grass(detailed=False):
    fill (150, 200, 100)
    pushMatrix()
    box (100, 1, 100)
    popMatrix()
    
    fill (120, 170, 70)
    if detailed:
        for i in range (random.randint (0, 10)):
            pushMatrix()
            translate (random.randint (-45, 45), -0.5, random.randint (-45, 45))
            box (1, random.randint(1, 3), 1)
            popMatrix()
    
