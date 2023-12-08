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

## Keep track of the score
leftPlayer = 0
rightPlayer = 0
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0", align="center", font=("Courier", 24, "normal"))



#Left Paddle 
left_paddle = turtle.Turtle()

left_paddle.speed(0)

left_paddle.shape("rectangle")

left_paddle.shapesize(stretch_wid=6,stretch_len=2)

left_paddle.color("red")

left_paddle.penup()

left_paddle.goto(-400,0)


#Right Paddle
right_paddle = turtle.Turtle()

right_paddle.speed(0)

right_paddle.shape("rectangle")

right_paddle.shapesize(stretch_wid=6,stretch_len=2)

## main function
def main():
    while True:
        sc.update()
        hitBall.setx(hitBall.xcor() + hitBall.dx)
        hitBall.sety(hitBall.ycor() + hitBall.dy)
