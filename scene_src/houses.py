from cylinder import *
houseScale = 1.5

def house1():
    pushMatrix()
    scale (houseScale)
    translate (0, -19, 0)
    
    # main
    fill (220, 205, 228)
    pushMatrix()
    translate(0, 2, 0)
    box (30, 32.5, 30)
    popMatrix()
    
    # shade
    fill (200, 185, 205)
    pushMatrix()
    translate(0, -5, 12)
    rotateX(-90)
    box (20, 20, 1)
    popMatrix()
    
    # door
    fill (255, 245, 225)
    pushMatrix()
    translate (-5, 10, 15)
    box (10, 17, 2)
    popMatrix()
    
    # window
    pushMatrix()
    translate (7, 10, 15)
    box (10, 10, 2)
    popMatrix()

    # roof accent
    fill (255, 245, 225)
    pushMatrix()
    translate (0, -15, 0)
    box (30, 2, 30)
    popMatrix()
    
    # sign
    pushMatrix()
    translate (0, -10, 15)
    box (20, 5, 2)
    popMatrix()
    
    popMatrix()
    
def house2():
    pushMatrix()
    scale (houseScale)
    translate (0, -12, 0)
    
    #main
    fill (255, 200, 190)
    pushMatrix()
    box (25, 25, 25)
    popMatrix()
    
    #door
    fill (235, 180, 170)
    pushMatrix()
    translate (-5, 7, 10.5)
    box (7, 10, 5)
    popMatrix()
    
    # mid section
    fill (255, 155, 100)
    pushMatrix()
    translate (0, -5, 0)
    box (27, 5, 27)
    popMatrix()
    
    # barrel
    pushMatrix()
    translate(0, -13, -5)
    rotateY(1.5708)
    cylinder(sides=20, r1=4, r2=4, h=10)
    
    translate (0, 0, -5)
    sphere(4)
    translate (0, 0, 10)
    sphere(4)
    popMatrix()
    
    # sign pole
    pushMatrix()
    translate (-20, -5, 10)
    rotateX(-1.5708)
    cylinder (sides=20, r1=2, r2=3, h=35)
    popMatrix()
    
    pushMatrix()
    translate (-20, -20, 10)
    rotateX(-1.5708)
    cylinder (sides=20, r1=4, r2=4, h=10)
    popMatrix()
    
    # sign
    fill (255, 155, 100)
    pushMatrix()
    translate (-5, -20, 10)
    box (30, 7, 1)
    popMatrix()
    popMatrix()
    
def house3():
    pushMatrix()
    scale (houseScale)
    translate (0, -12, 0)
    
    #main
    fill (255, 200, 150)
    pushMatrix()
    box (45, 25, 25)
    
    # window
    fill (225, 170, 120)
    pushMatrix()
    translate (10, 0, 3)
    box (15, 10, 20)
    popMatrix()
    
    # door
    pushMatrix()
    translate (-10, 5, 3)
    box (10, 15, 20)
    popMatrix()
    
    fill (205, 150, 100)
    pushMatrix()
    translate (-10, 11, 3)
    box (10, 3, 21)
    popMatrix()    

    # accent
    fill (250, 235, 230)
    translate (0, -13.5, 0)
    box (45, 2, 25)
    popMatrix()
    
    popMatrix()

def house4():
    pushMatrix()
    scale (houseScale)
    translate (0, -15, 0)
    
    # main
    fill (185, 200, 225)
    pushMatrix()
    box(45, 30, 25)
    popMatrix()
    
    # atrium
    fill (230, 230, 230)
    pushMatrix()
    translate (0, -2, 12)
    rotateX(-1.5708)
    cylinder (sides=7, r1=5, r2=7, h=35)
    popMatrix()
    
    pushMatrix()
    translate (15, -2.5, 12)
    rotateX(-0.5)
    box (10, 1, 10)
    popMatrix()
    
    # door
    fill (155, 170, 195)
    pushMatrix()
    translate (15, 10, 10)
    box (5, 10, 6)
    popMatrix()
    
    # windows
    pushMatrix()
    translate (-15, 0, 10)
    box (10, 20, 6)
    popMatrix()
        
    # roof
    fill (165, 165, 180)
    pushMatrix()
    translate (0, -15.5, 0)
    box (45, 1.5, 25)
    popMatrix()

    # AC
    fill (235, 200, 130)
    pushMatrix()
    translate (15, -17, 5)
    box (7, 10, 7)
    popMatrix()
    
    pushMatrix()
    translate (15, -17, -5)
    box (7, 10, 7)
    popMatrix()
    
    popMatrix()

def house5():
    pushMatrix()
    scale (houseScale)
    translate(0, -15, 0)
    
    # main
    fill (250, 155, 140)
    pushMatrix()
    box (30, 30, 25)
    popMatrix()
    
    # roof
    fill (250, 190, 155)
    pushMatrix()
    translate (0, -16, 0)
    box (30, 2, 25)
    popMatrix()
    
    # doors
    fill (230, 125, 110)
    pushMatrix()
    translate (-7, 7, 12)
    box (7, 15, 2)
    popMatrix()
    
    # sign)
    pushMatrix()
    translate (10, -7, 13)
    box (20, 10, 1)
    popMatrix()
    
    # AC cylinders
    fill (210, 150, 115)
    pushMatrix()
    translate (-5, -10, 0)
    rotateX(-1.5708)
    cylinder (r1=5, r2=5, h=20)
    popMatrix()
    
    pushMatrix()
    translate (-5, -20, 0)
    sphere (5)
    popMatrix()
    
    pushMatrix()
    translate (7, -15, 4)
    box (10, 10, 5)
    popMatrix()
    
    pushMatrix()
    translate (7, -15, -3)
    box (10, 10, 5)
    popMatrix()
    
    popMatrix()
  
def house6():
    pushMatrix()
    scale (houseScale)
    translate (0, -17, 0)
    
    # main
    fill (160, 170, 155)
    pushMatrix()
    box (35, 35, 25)
    popMatrix()
    
    # shade
    fill (225)
    pushMatrix()
    translate (0, 0, 10)
    box (30, 1, 30)
    popMatrix()
    
    # pillars
    pushMatrix()
    translate (-12, 10, 22)
    rotateX(-1.5708)
    cylinder (sides=8, r1=1.5, r2=1, h=20)
    popMatrix()
    
    pushMatrix()
    translate (12, 10, 22)
    rotateX(-1.5708)
    cylinder (sides=8, r1=1.5, r2=1, h=20)
    popMatrix()
    
    # doors
    fill (140, 150, 125)
    pushMatrix()
    translate (0, 10, 10)
    box (10, 15, 7)
    popMatrix()
    
    # sign
    pushMatrix()
    translate (0, -9, 10)
    box (20, 10, 7)
    popMatrix()
    
    # roof
    fill (190, 200, 175)
    pushMatrix()
    translate (0, -18.5, 0)
    box (35, 2, 25)
    popMatrix()
    
    # AC barrels
    fill (210, 220, 195)
    pushMatrix()
    translate (-2, -20, -4)
    rotateY(1.5708)
    cylinder (sides=9, r1=3, r2=3, h=20)
    popMatrix()

    pushMatrix()
    translate (-2, -20, 4)
    rotateY(1.5708)
    cylinder (sides=9, r1=3, r2=3, h=20)
    popMatrix()
    
    pushMatrix()
    translate (12, -20, 0)
    box(5, 10, 15)
    popMatrix()
    
    popMatrix()
        
def garage():
    pushMatrix()
    translate (12, -15, 0)
    
    # main (walls)
    fill (220, 220, 235)

    # left
    pushMatrix()
    translate(-17, 0, -5)
    box (2, 30, 40)
    popMatrix()
    
    #right
    pushMatrix()
    translate(17, 0, -5)
    box (2, 30, 40)
    popMatrix()
    
    # top
    pushMatrix()
    translate(0, -20, -5)
    box (36, 10, 40)
    popMatrix()
    
    # back
    pushMatrix()
    translate(0, 0, -24)
    box (35, 30, 2)
    popMatrix()
    
    # garage door
    fill (200, 200, 215)
    pushMatrix()
    translate (0, 0, 14)
    box (35, 30, 1)
    popMatrix()
    
    # side house
    fill (200, 215, 185)
    pushMatrix()
    translate (-30, 2, 3)
    box (25, 25, 20)
    popMatrix()
    
    # side roof
    fill (220, 235, 205)
    pushMatrix()
    translate (-30, -11.5, 3)
    box (25, 2, 20)
    popMatrix()
        
    # side AC
    fill (200, 225, 190)
    pushMatrix()
    translate (-32, -13, -3)
    rotateY(1.5708)
    cylinder (sides=9, r1=3, r2=3, h=15)
    popMatrix()
    
    pushMatrix()
    translate (-32, -13, 7)
    rotateY(1.5708)
    cylinder (sides=9, r1=3, r2=3, h=15)
    popMatrix()
    
    # side door
    fill (170, 185, 155)
    pushMatrix()
    translate (-32, 7, 8)
    box (8, 15, 12)
    popMatrix()
    
    # side bulb
    fill (245, 200, 0)
    pushMatrix()
    translate (-10, -20, 15)
    box (2.5)
    popMatrix()
    
    pushMatrix()
    translate (0, -20, 15)
    box (2.5)
    popMatrix()
    
    pushMatrix()
    translate (10, -20, 15)
    box (2.5)
    popMatrix()
    
    popMatrix()    
    

    
