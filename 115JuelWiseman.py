#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
# Create the spiders body
spider.color("black")
spider.pensize(40)
spider.circle(20)

spider.speed(0)

# Configure spiders legs 
legs = 8
length = 95
spacing = 10000/ legs
spider.pensize(5)
loop = 0

# Draw spiders legs
while (loop < legs):
  spider.penup()
  spider.goto(0,20)
  spider.pendown()
  if loop < 4:
    spider.setheading(spacing*loop)
    spider.forward(length)
  else:
    spider.setheading(spacing*loop)
    spider.forward(length)
  loop = loop + 1
spider.hideturtle()

# Draw spiders eyes
spider.penup()
spider.goto(10,10)
spider.pendown()
spider.color("red")
spider.pensize(4)
spider.circle(2)

spider.penup()
spider.goto(-12,10)
spider.pendown()
spider.color("red")
spider.pensize(4)
spider.circle(2)
# Draw spiders pupils
spider.penup()
spider.goto(10,10)
spider.pendown()
spider.color("black")
spider.pensize(2)
spider.circle(1)

spider.penup()
spider.goto(-12,10)
spider.pendown()
spider.color("black")
spider.pensize(2)
spider.circle(1)
wn = trtl.Screen()
wn.mainloop()