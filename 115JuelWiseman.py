#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
# Create the spiders body
spider.color("black")
spider.pensize(40)
spider.circle(20)

# Configure spiders legs 
legs = 8
length = 95
spacing = 360 / legs
spider.pensize(5)
loop = 0

# Draw spiders legs
while (loop < legs):
  spider.penup()
  spider.goto(0,20)
  spider.pendown()
  spider.setheading(spacing*loop)
  spider.forward(length)
  loop = loop + 1
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()