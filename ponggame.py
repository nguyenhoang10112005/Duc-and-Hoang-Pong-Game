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





"sdjfsj;dfl;sdkfl;ksl;dfk;lskdfl;ksdl;f"
## main function
def main():
    while True:
        sc.update()
