import turtle
import random
import time
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

colorList = ["red", "green", "blue", "black", "magenta", "orange", "gray"]
turtle.shape('turtle')
turtle.setup(600, 600)
turtle.screensize(700, 700)
turtle.penup()

num = 1
for _ in range(36) :
    turtle.goto(0,0)
    turtle.right(10)
    turtle.forward(350)
    turtle.pencolor(random.choice(colorList))
    turtle.write(str(num), font=('Arial', 15, 'bold'))
    num += 1

turtle.goto(0,0)
time.sleep(5)
turtle.pendown()
turtle.pensize(5)

angle = random.randint(10, 360) // 10*10
turtle.right(angle)
turtle.forward(350)

number = angle // 10
if number < 10 :
    number = '0' + str(number)
else :
    number = str(number)

filename = "C:/photo/picture" + number + ".jpg"
img = Image.open(filename)
img.show()

turtle.done()