#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(giancarlo, sides):
    for s in range(sides):
        giancarlo.forward(50)
        giancarlo.right(360/sides)
        
def fillCorner(judd, corner):
    drawSquare(judd, 100)
    if corner == 1:
        judd.begin_fill()
        drawSquare(judd, 50)
        judd.end_fill()
    elif corner == 2:
        judd.forward(50)
        judd.begin_fill()
        drawSquare(judd, 50)
        judd.end_fill()
    elif corner == 3:
        judd.right(90)
        judd.forward(50)
        judd.left(90)
        judd.begin_fill()
        drawSquare(judd, 50)
        judd.end_fill()
    elif corner == 4:
        judd.up()
        judd.right(90)
        judd.forward(50)
        judd.left(90)
        judd.forward(50)
        judd.down()
        judd.begin_fill()
        drawSquare(judd, 50)
        judd.end_fill()
    
        
def squaresInSquares(pat, num):
    length = 300
    pat.up()
    pat.goto(-150,150)
    pat.down()
    for n in range(num):
        num = int(num)
        drawSquare(pat, length)
        length = length-50
        pat.up()
        pat.forward(25)
        pat.right(90)
        pat.forward(25)
        pat.left(90)
        pat.down()
        
        

def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 3) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
