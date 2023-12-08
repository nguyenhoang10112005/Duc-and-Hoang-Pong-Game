import turtle

## screen
sc = turtle.Screen()
sc.title("Pong Game")
sc.setup(800,800)
sc.bgcolor("black")

## set up key press
sc.listen()
sc.onkeypress(paddleaup,"w")
sc.onkeypress(paddleadown,"s")
sc.onkeypress(paddlebup,"Up")
sc.onkeypress(paddlebdown,"Down")

## create ball
hitBall = turtle.Turtle()
hitBall.speed(80)
hitBall.shape("circle")
hitBall.color("white")
hitBall.penup()
hitBall.goto(0,0)
hitBall.dx = 5
hitBall.dy = -5



## main function
def main():
    while True:
        sc.update()