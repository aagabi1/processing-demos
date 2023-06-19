def cylinder(sides=20, r1=1, r2=1, h=2):
    angle = 360 / float(sides)
    halfHeight = h / 2
    # top
    beginShape();
    for i in range(sides):
        x = cos( radians( i * angle ) ) * r1
        y = sin( radians( i * angle ) ) * r1
        vertex( x, y, -halfHeight)
    endShape(CLOSE);
    
    # bottom
    beginShape();
    for i in range(sides):
        x = cos( radians( i * angle ) ) * r2
        y = sin( radians( i * angle ) ) * r2
        vertex( x, y, halfHeight)
    endShape(CLOSE);
    
    # body
    beginShape(TRIANGLE_STRIP);
    for i in range(sides + 1):
        x1 = cos( radians( i * angle ) ) * r1
        y1 = sin( radians( i * angle ) ) * r1
        x2 = cos( radians( i * angle ) ) * r2
        y2 = sin( radians( i * angle ) ) * r2
        vertex( x1, y1, -halfHeight)
        vertex( x2, y2, halfHeight)
    endShape(CLOSE)
