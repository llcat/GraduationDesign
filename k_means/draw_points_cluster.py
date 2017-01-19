#使用turtle画出所有点的分布，方便查看所有点的被聚成几类

from turtle import *
'''
points = []
points_file = open("data.txt","r")
my_turtle = Turtle()
points = points_file.readlines()
my_turtle.fd(200)
my_turtle.setpos(0,0)
my_turtle.left(90)
my_turtle.fd(200)
my_turtle.getscreen().tracer(10,25)
my_turtle.penup()
for point in points:
    pos_x,pos_y = map(int,point.split(","))
    my_turtle.setpos(pos_x,pos_y)
    my_turtle.dot(5,"red")

my_turtle.getscreen().mainloop()
'''
class ResultShow(object):
    def __init__(self):
        self.my_turtle = Turtle()
        self.my_screen = self.my_turtle.getscreen()

    def draw(self,result):
        self.my_turtle.fd(200)
        self.my_turtle.setpos(0, 0)
        self.my_turtle.left(90)
        self.my_turtle.fd(200)
        self.my_screen.tracer(10, 25)
        self.my_turtle.penup()
        for res in result:
            if res[0] == "0":
                self.my_turtle.pencolor((1,0,0))
            elif res[0] == "1":
                self.my_turtle.pencolor(0,1,0)
            elif res[0] == "2":
                self.my_turtle.pencolor(0,0,1)
            elif res[0] == "3":
                self.my_turtle.pencolor(1,1,0)
            else:
                pass

            for re in res[1]:
                self.my_turtle.setpos(re['x']*200, re['y']*200)
                self.my_turtle.dot(5)
        self.my_screen.mainloop()

