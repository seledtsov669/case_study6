"""Case-study Тесселяция
Разработчики:
Marinkin O. (40%)
Seledtsov A. (60%)
Evdishenko M. (35%)
"""
import math
import turtle

def get_color1():
    """Функция, получающая нужные цвета заливки"""
    print("choose form colors: black, red, green, blue, purple, yellow")
    # Вывести допустимые цвета
    color1 = input('Write down first color ').strip()
    color1 = color1.lower()
    while color1 != 'black' and color1 != 'red' and  color1 != 'blue' and color1 != 'yellow' and color1 != 'green' and color1 != 'purple':
        color1 = input("wrong color, choose another ").strip()
        color1 = color1.lower()
    return color1
def get_colour2():
    color2 = input('Write down first color ').strip()
    color2 = color2.lower()
    while color2 != 'black' and color2 != 'red' and  color2 != 'blue' and color2 != 'yellow' and color2 != 'green' and color2 != 'purple':
        color2 = input("wrong color, choose another ").strip()
        color2 = color2.lower()
    return color2

def get_num_hexagons():
    """Funktion getting number of hexagons in a raw"""
    num_hexagons = float(input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '))
    while not (4 <= num_hexagons <= 20):
        num_hexagons = float(input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: '))
    return num_hexagons

def draw_hexagon(x, y, side, color):
    '''
    Funktion drawing hexagon
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: side length of a hexagon
    :return: None
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.left(90)
    turtle.color('black', color)

    turtle.down()
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(side)
        turtle.right(60)
    turtle.end_fill()
    turtle.up()

def draw_raw_hexagons(x, y, n, color1, color2):
    """Funktion drawing a raw of hexagons"""
    w = x
    e = y
    side_hexagon = math.floor(500 / (2 * n))
    for i in range(math.ceil(n / 2)):
        draw_hexagon(x, y, side_hexagon, color1)
        #Получить координаты для следуующего шестиугольника
        x = turtle.xcor() + 2 * (side_hexagon * math.sqrt(3))
        y = turtle.ycor()


    turtle.up()
    turtle.goto(w - side_hexagon * math.sqrt(3), e)

    for q in range(math.floor(n / 2)):
        x = turtle.xcor() + 2 * (side_hexagon * math.sqrt(3))
        y = turtle.ycor()
        draw_hexagon(x, y, side_hexagon, color2)

def draw_raw_hexagons1(x, y, n, color1, color2):
    """Funktion drawing a raw of hexagons"""
    w = x
    e = y
    side_hexagon = math.floor(500 / (2 * n))
    for i in range(math.ceil(n / 2)):
        draw_hexagon(x, y, side_hexagon, color2)
        #Получить координаты для следуующего шестиугольника
        x = turtle.xcor() + 2 * (side_hexagon * math.sqrt(3))
        y = turtle.ycor()

    turtle.up()
    turtle.goto(w - side_hexagon * math.sqrt(3), e)

    for q in range(math.floor(n / 2)):
        x = turtle.xcor() + 2 * (side_hexagon * math.sqrt(3))
        y = turtle.ycor()
        draw_hexagon(x, y, side_hexagon, color1)

def main(x, y, color1, color2):
    """Funktion making tessellation"""
    q = x
    m = y
    n = get_num_hexagons()
    side_hexagon = math.ceil(500 / (2 * n))
    d = side_hexagon * math.sqrt(3)
    h = side_hexagon / 2
    if n % 2 == 0:
        for i in range(math.ceil(n / 4)):
            draw_raw_hexagons(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)

        turtle.up()
        turtle.goto(q + d / 2, m + side_hexagon + h)
        x = turtle.xcor()
        y = turtle.ycor()
        for u in range(math.ceil(n / 4)):
            draw_raw_hexagons(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)

        turtle.up()
        turtle.goto(q, m + 2 * (side_hexagon + h))
        x = turtle.xcor()
        y = turtle.ycor()
        for o in range(math.floor(n / 4)):
            draw_raw_hexagons1(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)

        turtle.up()
        turtle.goto(q + d / 2, m + 3 * (side_hexagon + h))
        x = turtle.xcor()
        y = turtle.ycor()
        for v in range(math.floor(n / 4)):
            draw_raw_hexagons1(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)
    elif n == 5 or n == 9 or n == 13 or n == 17:
        for i in range(math.ceil(n / 4)):
            draw_raw_hexagons(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)

        turtle.up()
        turtle.goto(q + d / 2, m + side_hexagon + h)
        x = turtle.xcor()
        y = turtle.ycor()
        for u in range(math.floor(n / 4)):
            draw_raw_hexagons(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)

        turtle.up()
        turtle.goto(q, m + 2 * (side_hexagon + h))
        x = turtle.xcor()
        y = turtle.ycor()
        for o in range(math.floor(n / 4)):
            draw_raw_hexagons1(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)

        turtle.up()
        turtle.goto(q + d / 2, m + 3 * (side_hexagon + h))
        x = turtle.xcor()
        y = turtle.ycor()
        for v in range(math.floor(n / 4)):
            draw_raw_hexagons1(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)
    elif n == 7 or n == 11 or n == 15 or n == 19:
        for i in range(math.ceil(n / 4)):
            draw_raw_hexagons(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)

        turtle.up()
        turtle.goto(q + d / 2, m + side_hexagon + h)
        x = turtle.xcor()
        y = turtle.ycor()
        for u in range(math.ceil(n / 4)):
            draw_raw_hexagons(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)

        turtle.up()
        turtle.goto(q, m + 2 * (side_hexagon + h))
        x = turtle.xcor()
        y = turtle.ycor()
        for o in range(math.ceil(n / 4)):
            draw_raw_hexagons1(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)

        turtle.up()
        turtle.goto(q + d / 2, m + 3 * (side_hexagon + h))
        x = turtle.xcor()
        y = turtle.ycor()
        for v in range(math.floor(n / 4)):
            draw_raw_hexagons1(x, y, n, color1, color2)
            y += 4 * (side_hexagon + h)


turtle.speed(970)
main(-250, -250, get_color1(), get_colour2())
turtle.mainloop()