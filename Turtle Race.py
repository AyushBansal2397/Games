from turtle import *
import time
import numpy as np

def race_course(speed_of_turtles=8,breadth=220,length=280):
    speed(speed_of_turtles)
    number_of_steps=int((length/20)+1)
    for step in range(number_of_steps):
        write(step,align='center')
        penup()
        right(90)
        forward(10)
        pendown()
        forward(breadth)
        penup()
        backward(breadth+10)
        left(90)
        forward(20)

def turtles(breadth=220,number_of_turtles=6,speed_of_turtles=6):
    turtle_mat=np.empty(number_of_turtles,object)
    turtle_pos=np.empty(number_of_turtles,object)
    for i in range(number_of_turtles):
        turtle_mat[i]=Turtle()
        turtle_mat[i].speed(speed_of_turtles)
        turtle_mat[i].color([float(x) for x in np.random.rand(3)]) #color(.4,.3,.5)
        turtle_mat[i].shape('turtle')
        turtle_mat[i].penup()
        turtle_mat[i].goto(0,-20-(breadth-20)/(number_of_turtles-1)*i)
        turtle_pos[i]=turtle_mat[i].position()
        turtle_mat[i].pendown()
    return turtle_mat,turtle_pos

def race(turtle_mat,turtle_pos,length=280,max_step=8):
    progress=np.zeros(len(turtle_mat))    
    while True:
        for i in range(len(turtle_mat)):
            val=np.random.randint(1,max_step)
            turtle_mat[i].forward(val)
            progress[i]+=val
            if turtle_mat[i].position()<=turtle_pos[i]:
                time.sleep(3)
                exit()
            elif progress[i]>=length:
                progress[i]=-max_step
                turtle_mat[i].right(180)
def main():
    print('\n\t\t\t\tTURTLE RACE\n\nEnter Details:-\t\t\t\t\t(Press only ENTER to pass default values)')
    while True:
        try:
            l=int(input(' Enter Length of Race Course: ') or '200')
            b=int(input(' Enter Breadth of Race Course: ') or '220')
            s=int(input(' Enter Speed of Turtles: ') or '8')
            n=int(input(' Enter Number of Turtles: ') or '6')
            ms=int(input(' Enter Max Step Size of Turtles: ') or '8')
            break
        except:
            print('\nEnter Details correctly in INTEGERS.\n')
            # race_course()
            # race(*turtles())   
    race_course(s,b,l)
    turt,pos=turtles(b,n,s)
    race(turt,pos,l,ms)

if __name__ == '__main__':
    main()
