# Object Modeling Example Code

from __future__ import division
import traceback

time = 0   # time is used to move objects from one frame to another

def setup():
    size (800, 800, P3D)
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    try:
        global time
        time += 0.005

        camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position of the virtual camera

        background (255, 217, 249)  # clear screen and set background to light blue
        
        # set up the lights
        ambientLight(200, 200, 200);
        lightSpecular(255, 255, 255)
        directionalLight (50, 50, 50, -0.5, 0.5, -1)
        
        # set some of the surface properties
        noStroke()
        specular (25, 25, 25)
        shininess (15.0)
    
        #scale (1, 1.10, 1)
        car()
        
    except Exception: 
        traceback.print_exc()

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 50):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # round main body
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2

def car():
    # windshield
    fill (245, 245, 245)
    pushMatrix()
    rotateY(-time)
    translate (5.5, 0.5, 0)
    scale (10, 9, 9)
    cylinder()
    popMatrix()
    
    pushMatrix()
    rotateY(-time)
    translate (-5.5, 0.5, 0)
    scale (10, 9, 9)
    cylinder()
    popMatrix()
    
    # bumper
    fill (250, 220, 0)
    pushMatrix()
    rotateY(-time)
    translate (27.5, 8, 0)
    box (3, 3, 18)
    popMatrix()
    
    # top half
    fill (201, 224, 191)
    pushMatrix()
    rotateY(-time)
    scale (15, 10, 10)
    cylinder()
    popMatrix()
    
    # bottom cube
    pushMatrix()
    translate (0, 5, 0)
    rotateY(-time)
    box(50, 10, 20)
    popMatrix()
    
    # Curve front
    pushMatrix()
    rotateY(-time)
    translate (25, 5, 0)
    scale (5, 5, 10)
    cylinder()
    popMatrix()
    
    # curve back
    pushMatrix()
    rotateY(-time)
    translate (-25, 5, 0)
    scale (5, 5, 10)
    cylinder()
    popMatrix()
    
    # wheel front right
    fill(50, 50, 50)
    pushMatrix()
    rotateY(-time)
    translate (20, 7, 10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()
    
    # wheel front left
    fill(50, 50, 50)
    pushMatrix()
    rotateY(-time)
    translate (20, 7, -10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()

    # wheel back right
    fill(50, 50, 50)
    pushMatrix()
    rotateY(-time)
    translate (-20, 7, 10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()
    
    # wheel back left
    fill(50, 50, 50)
    pushMatrix()
    rotateY(-time)
    translate (-20, 7, -10)
    scale (5, 5, 1.5 )
    cylinder()
    popMatrix()
    
    # door knobs right
    fill (235, 235, 235)
    pushMatrix()
    rotateY(-time)
    translate (3, 2, 10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    pushMatrix()
    rotateY(-time)
    translate (-10, 2, 10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    # door knobs left
    pushMatrix()
    rotateY(-time)
    translate (3, 2, -10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    pushMatrix()
    rotateY(-time)
    translate (-10, 2, -10)
    scale (1.5, 0.5, 0.5)
    sphere(1)
    popMatrix()
    
    # antenna
    fill (250, 220, 0)
    pushMatrix()
    rotateY(-time)
    translate (-25, -3, 7)
    scale (0.1, 5, 0.1)
    rotateX(1.5708)
    cylinder()
    popMatrix()
    
    # headlights back right
    fill (255, 100, 0)
    pushMatrix()
    rotateY(-time)
    translate (-25, 5, 5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # headlights back left
    pushMatrix()
    rotateY(-time)
    translate (-25, 5, -5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # headlights front right
    fill (150, 150, 150)
    pushMatrix()
    rotateY(-time)
    translate (25, 5, 5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    fill (235, 235, 235)
    pushMatrix()
    rotateY(-time)
    translate (26.5, 5, 5)
    scale (4.5, 1.5, 1.5)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    # headlights front left
    fill (150, 150, 150)
    pushMatrix()
    rotateY(-time)
    translate (25, 5, -5)
    scale (5.5, 2, 2)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    fill (235, 235, 235)
    pushMatrix()
    rotateY(-time)
    translate (26.5, 5, -5)
    scale (4.5, 1.5, 1.5)
    rotateY (1.5708)
    cylinder()
    popMatrix()
    
    
"""
    # a red box
    fill (255, 0, 0)
    pushMatrix()
    translate (-30, 0, 0)
    rotateX (time)
    box(20)
    popMatrix()

    # a green sphere
    fill (0, 250, 0)
    pushMatrix()
    translate (0, 8 * sin(4 * time), 0)  # move up and down
    sphereDetail(60)  # this controls how many polygons make up each sphere
    sphere(10)
    popMatrix()

    # a blue cylinder
    fill (0, 0, 255)
    pushMatrix()
    translate (30, 0, 0)
    rotateX (-time)
    scale (10, 10, 10)
    cylinder()
    popMatrix()    
"""
