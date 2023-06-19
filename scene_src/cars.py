from cylinder import *

def citizen():
    pushMatrix()
    translate (0, -13, 0)
    scale (0.8)
    # windshield
    fill (245, 245, 245)
    pushMatrix()
    
    translate (6, 0.5, 0)
    scale (10, 9, 9)
    cylinder()
    popMatrix()
    
    pushMatrix()
    
    translate (-6, 0.5, 0)
    scale (10, 9, 9)
    cylinder()
    popMatrix()
    
    # bumper
    fill (250, 220, 0)
    pushMatrix()
    
    translate (27.5, 8, 0)
    box (3, 3, 18)
    popMatrix()
    
    # top half
    fill (201, 224, 191)
    pushMatrix()
    
    scale (15, 10, 10)
    cylinder()
    popMatrix()
    
    # bottom cube
    pushMatrix()
    translate (0, 5, 0)
    
    box(50, 10, 20)
    popMatrix()
    
    # Curve front
    pushMatrix()
    
    translate (25, 5, 0)
    scale (5, 5, 10)
    cylinder()
    popMatrix()
    
    # curve back
    pushMatrix()
    
    translate (-25, 5, 0)
    scale (5, 5, 10)
    cylinder()
    popMatrix()
    
    # wheel front right
    fill(50, 50, 50)
    pushMatrix()
    
    translate (20, 7, 10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()
    
    # wheel front left
    fill(50, 50, 50)
    pushMatrix()
    
    translate (20, 7, -10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()

    # wheel back right
    fill(50, 50, 50)
    pushMatrix()
    
    translate (-20, 7, 10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()
    
    # wheel back left
    fill(50, 50, 50)
    pushMatrix()
    
    translate (-20, 7, -10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()
    
    # door knobs right
    fill (235, 235, 235)
    pushMatrix()
    
    translate (3, 2, 10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    pushMatrix()
    
    translate (-10, 2, 10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    # door knobs left
    pushMatrix()
    
    translate (3, 2, -10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    pushMatrix()
    
    translate (-10, 2, -10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    # antenna
    fill (250, 220, 0)
    pushMatrix()
    
    translate (-25, -3, 7)
    scale (0.5, 5, 0.5)
    rotateX(1.5708)
    cylinder()
    popMatrix()
    
    # headlights back right
    fill (255, 100, 0)
    pushMatrix()
    
    translate (-25, 5, 5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # headlights back left
    pushMatrix()
    
    translate (-25, 5, -5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # headlights front right
    fill (150, 150, 150)
    pushMatrix()
    
    translate (25, 5, 5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    fill (235, 235, 235)
    pushMatrix()
    
    translate (26.5, 5, 5)
    scale (4.5, 1.5, 1.5)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # headlights front left
    fill (150, 150, 150)
    pushMatrix()
    
    translate (25, 5, -5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    fill (235, 235, 235)
    pushMatrix()
    
    translate (26.5, 5, -5)
    scale (4.5, 1.5, 1.5)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    popMatrix()
    
def police():
    pushMatrix()
    scale (0.8)
    translate (0, -13, 0)
    
    # top half
    fill (235, 235, 235)
    pushMatrix()
    
    translate(0, 1.5, 0)
    box(20, 17, 19.5)
    popMatrix()
    
    # front windshield
    pushMatrix()
    
    translate(9.5, 0, 0)
    rotateZ(15)
    box(10, 10, 19.5)
    popMatrix()

    # back windshield
    pushMatrix()
    
    translate(-9.5, 0, 0)
    rotateZ(-15)
    box(10, 10, 19.5)
    popMatrix()
    
    # bottom cube
    fill (85, 85, 85)
    pushMatrix()
    translate (0, 5, 0)
    
    box(50, 10, 20)
    popMatrix()
    
    # Curve front
    pushMatrix()
    
    translate (25, 5, 0)
    scale (5, 5, 10)
    cylinder()
    popMatrix()
    
    # curve back
    pushMatrix()
    
    translate (-25, 5, 0)
    scale (5, 5, 10)
    cylinder()
    popMatrix()
    
    # bumper
    fill (245, 245, 245)
    pushMatrix()
    
    translate (27.5, 8, 0)
    box (3, 3, 18)
    popMatrix()
    
    # wheel front right
    fill(50, 50, 50)
    pushMatrix()
    
    translate (20, 7, 10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()
    
    # wheel front left
    fill(50, 50, 50)
    pushMatrix()
    
    translate (20, 7, -10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()

    # wheel back right
    fill(50, 50, 50)
    pushMatrix()
    
    translate (-20, 7, 10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()
    
    # wheel back left
    fill(50, 50, 50)
    pushMatrix()
    
    translate (-20, 7, -10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()
    
    # door knobs right
    fill (235)
    pushMatrix()
    
    translate (3, 2, 10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    pushMatrix()
    
    translate (-10, 2, 10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    # door knobs left
    pushMatrix()
    
    translate (3, 2, -10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    pushMatrix()
    
    translate (-10, 2, -10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    # headlights back right
    fill (255, 100, 0)
    pushMatrix()
    
    translate (-25, 5, 5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # headlights back left
    pushMatrix()
    
    translate (-25, 5, -5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # headlights front right
    fill (150, 150, 150)
    pushMatrix()
    
    translate (25, 5, 5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    fill (235, 235, 235)
    pushMatrix()
    
    translate (26.5, 5, 5)
    scale (4.5, 1.5, 1.5)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # headlights front left
    fill (150, 150, 150)
    pushMatrix()
    
    translate (25, 5, -5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    fill (235, 235, 235)
    pushMatrix()
    
    translate (26.5, 5, -5)
    scale (4.5, 1.5, 1.5)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # siren
    fill (235, 235, 235) # middle
    pushMatrix()
    
    translate(0, -8, 0)
    box(7, 3, 5)
    popMatrix()
    
    fill (100, 0, 255) # blue
    pushMatrix()
    
    translate(0, -8, -5)
    box(7, 3, 5)
    popMatrix()
    
    fill (255, 100, 0) # red
    pushMatrix()
    
    translate(0, -8, 5)
    box(7, 3, 5)
    popMatrix()
    
    popMatrix()
    
def bus():
    pushMatrix()
    scale (0.8)
    translate (0, -14, 0)
    
    # main
    fill (250, 190, 75)
    pushMatrix()
    box (60, 25, 25)
    popMatrix()
    
    # slant
    pushMatrix()
    translate (28.75, 0, 0)
    rotateZ(-0.3)
    box (10, 23, 25)
    popMatrix()
    
    # fill out bottom
    pushMatrix()
    translate (32, 10, 0)
    box (5, 5, 25)
    popMatrix()
    
    # bumper
    fill (85, 85, 100)
    pushMatrix()
    translate (35, 10, 0)
    box (5, 5, 25.5)
    popMatrix()
    
    pushMatrix()
    translate (-30, 10, 0)
    box (1, 5, 25.5)
    popMatrix()
    
    # windshield
    fill (235, 235, 235)
    pushMatrix()
    translate (33, -2, 0)
    rotateZ(-0.3)
    box (3, 15, 22)
    popMatrix()
    
    # windshiled back
    pushMatrix()
    translate (-30, -2, 0)
    box (5, 10, 20)
    popMatrix()
    
    # doors
    fill (220, 160, 40)
    pushMatrix()
    translate (15, 2, 1)
    box (7, 17, 25)
    popMatrix()
    
    # windows
    pushMatrix()
    box (15, 10, 27)
    popMatrix()
    
    pushMatrix()
    translate (-17, 0, 0)
    box (15, 7, 27)
    popMatrix()
    
    pushMatrix()
    translate (17, 0, -1)
    box (15, 7, 25)
    popMatrix()
    
    
    # wheels
    fill (85, 85, 100)
    
    # wheel front right
    pushMatrix()
    translate (25, 10, 12)
    scale (4, 4, 1.5 )
    cylinder(sides=16)
    popMatrix()
    
    # wheel front left
    pushMatrix()
    translate (25, 10, -12)
    scale (4, 4, 1.5 )
    cylinder(sides=16)
    popMatrix()

    # wheel back right
    pushMatrix()
    translate (-20, 10, 12)
    scale (4, 4, 1.5 )
    cylinder(sides=16)
    popMatrix()
    
    # wheel back left
    pushMatrix()
    translate (-20, 10, -12)
    scale (4, 4, 1.5 )
    cylinder(sides=16)
    popMatrix()
    
    # top accents
    fill (230, 110, 60)
    pushMatrix()
    translate (10, -11, 5)
    box (10, 5, 10)
    popMatrix()
    
    pushMatrix()
    translate (10, -12, -5)
    box (10, 5, 4)
    popMatrix()
    
    pushMatrix()
    translate (-7, -12, 0)
    box (15, 5, 15)
    popMatrix()
    
    pushMatrix()
    translate (20, -11, 0)
    box (5, 5, 15)
    popMatrix()
    
    popMatrix()
