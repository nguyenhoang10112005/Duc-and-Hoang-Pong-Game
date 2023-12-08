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

## Score player



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



"sdjfsj;dfl;sdkfl;ksl;dfk;lskdfl;ksdl;f"
## main function
def main():
    while True:
        sc.update()
