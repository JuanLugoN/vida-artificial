import turtle
import os
from PIL import Image

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir('../img')
PATH_IMG = os.getcwd()+'/'
os.chdir('../docs')
PATH_DOCS = os.getcwd()+'/'

def grammar_binary_tree(literal):
    """
    Grammar for binary tree
    """
    if literal == '0':
        new_string = '1[0]0'
    elif literal == '1':
        new_string = '11'
    else:
        new_string = literal
    return new_string

def grammar_koch_curve(literal):
    """
    Grammar for Koch curve
    """
    if literal == 'F':
        new_string = 'F+F-F-F+F'
    else:
        new_string = literal
    return new_string

def grammar_sierpinski_triangle(literal):
    """
    Grammar for sierpinski triangle
    """
    if literal == 'F':
        new_string = 'F-G+F+G-F'
    elif literal == 'G':
        new_string = 'GG'
    else:
        new_string = literal
    return new_string

def grammar_dragon_curve(literal):
    """
    Grammar for dragon curve
    """
    if literal == 'F':
        new_string = 'F+G'
    elif literal == 'G':
        new_string = 'F-G'
    else:
        new_string = literal
    return new_string

def grammar_fractal_plant(literal):
    """
    Grammar for dragon curve
    """
    if literal == 'X':
        new_string = 'F+[[X]-X]-F[-FX]+X'
    elif literal == 'F':
        new_string = 'FF'
    else:
        new_string = literal
    return new_string

def apply_grammar(original_string, grammar):
    """
    Apply the rules of grammar.
    :param original_string: string a to apply the grammar to.
    :param grammar: grammar to be applied.
    :return: string with grammar applied once.
    """
    tranformed_string = ""
    for literal in original_string:
        tranformed_string = tranformed_string + grammar(literal)
    return tranformed_string

def create_l_system(l_system, axiom, number_of_iterations):
    """
    Generates a chain given an l-system and an axiom, the length of the chain depends on the number of iterations.
    :param l_system: Lindenmayer system or grammar.
    :param axiom: literal with which to start producing the string.
    :param number_of_iterations: number of iterations.
    :return: String generated given an l-system.
    """
    start_string = axiom
    for counter in range(number_of_iterations):
        end_string = apply_grammar(start_string, l_system)
        start_string = end_string
    return end_string

def draw_binary_tree(instructions, angle, distance):
    """
    Draw with turtle, interpreting each literal in the instructions passed in.
    :param instructions: instructions that the turtle follows to painturt.
    :param angle: angle at which the turtle will turns.
    :param distance: distance the turtle will travel.
    """
    window = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    turt = turtle.Turtle()
    turt.left(90)
    turt.speed(0)
    turt.color('blue')
    turt.shape("turtle")
    turt.up()
    turt.back(300)
    turt.down()
    stack = []
    for task in instructions:
        if task == '0':
            turt.forward(distance)
            turt.circle(5)
        elif task == '1':
            turt.forward(distance)
        elif task == '[':
            stack.append((turt.heading(), [turt.xcor(), turt.ycor()]))
            turt.left(angle)
        elif task == "]":
            angl, pos = stack.pop()
            turt.setheading(angl)
            turt.up()
            turt.goto(pos[0], pos[1])
            turt.down()
            turt.right(angle)
    cv = turt.getscreen()
    cv.getcanvas().postscript(file=PATH_IMG+".binary_tree.eps")
    window.exitonclick()
    image = Image.open(PATH_IMG+".binary_tree.eps")
    image.save(PATH_IMG+"binary_tree.png")  
    os.remove(PATH_IMG+".binary_tree.eps")

def draw_koch_curve(instructions, angle, distance):
    """
    Draw with turtle, interpreting each literal in the instructions passed in.
    :param instructions: instructions that the turtle follows to paint.
    :param angle: angle at which the turtle will turns.
    :param distance: distance the turtle will travel.
    """
    window = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    turt = turtle.Turtle()
    turt.speed(0)
    turt.color('blue')
    turt.shape("turtle")
    turt.up()
    turt.left(90)
    turt.back(100)
    turt.right(90)
    turt.back(326)
    turt.down()
    for task in instructions:
        if task == 'F':
            turt.forward(distance)
        elif task == '+':
            turt.left(angle)
        elif task == '-':
            turt.right(angle)
    cv = turt.getscreen()
    cv.getcanvas().postscript(file=PATH_IMG+".koch_curve.eps")
    window.exitonclick()
    image = Image.open(PATH_IMG+".koch_curve.eps")
    image.save(PATH_IMG+"koch_curve.png") 
    os.remove(PATH_IMG+".koch_curve.eps")

def draw_sierpinski_triangle(instructions, angle, distance):
    """
    Draw with turtle, interpreting each literal in the instructions passed in.
    :param instructions: instructions that the turtle follows to paint.
    :param angle: angle at which the turtle will turns.
    :param distance: distance the turtle will travel.
    """
    window = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    turt = turtle.Turtle()
    turt.speed(0)
    turt.color('blue')
    turt.shape("turtle")
    turt.up()
    turt.back(150)
    turt.right(90)
    turt.forward(250)
    turt.left(180)
    turt.down()
    for task in instructions:
        if task == 'F':
            turt.forward(distance)
        elif task == 'G':
            turt.forward(distance)
        elif task == '+':
            turt.left(angle)
        elif task == '-':
            turt.right(angle)
    cv = turt.getscreen()
    cv.getcanvas().postscript(file=PATH_IMG+".sierpinski_triangle.eps")
    window.exitonclick()
    image = Image.open(PATH_IMG+".sierpinski_triangle.eps")
    image.save(PATH_IMG+"sierpinski_triangle.png") 
    os.remove(PATH_IMG+".sierpinski_triangle.eps")

def draw_dragon_curve(instructions, angle, distance):
    """
    Draw with turtle, interpreting each literal in the instructions passed in.
    :param instructions: instructions that the turtle follows to paint.
    :param angle: angle at which the turtle will turns.
    :param distance: distance the turtle will travel.
    """
    window = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    turt = turtle.Turtle()
    turt.speed(0)
    turt.color('blue')
    turt.shape("turtle")
    turt.up()
    turt.left(90)
    turt.back(150)
    turt.right(90)
    turt.forward(80)
    turt.down()
    for task in instructions:
        if task == 'F':
            turt.forward(distance)
        elif task == 'G':
            turt.forward(distance)
        elif task == '+':
            turt.left(angle)
        elif task == '-':
            turt.right(angle)    
    cv = turt.getscreen()
    cv.getcanvas().postscript(file=PATH_IMG+".dragon_curve.eps")
    window.exitonclick()
    image = Image.open(PATH_IMG+".dragon_curve.eps")
    image.save(PATH_IMG+"dragon_curve.png") 
    os.remove(PATH_IMG+".dragon_curve.eps")

def draw_fractal_plant(instructions, angle, distance):
    """
    Draw with turtle, interpreting each literal in the instructions passed in.
    :param instructions: instructions that the turtle follows to paint.
    :param angle: angle at which the turtle will turns.
    :param distance: distance the turtle will travel.
    """
    window = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    turt = turtle.Turtle()
    turt.speed(0)
    turt.color('blue')
    turt.shape("turtle")
    turt.up()
    turt.back(250)
    turt.left(90)
    turt.back(270)
    turt.right(25)
    turt.down()
    stack = []
    for task in instructions:
        if task == 'F':
            turt.forward(distance)
        elif task == '+':
            turt.left(angle)
        elif task == '-':
            turt.right(angle)
        elif task == '[':
            stack.append((turt.heading(), [turt.xcor(), turt.ycor()]))
        elif task == ']':
            angl, pos = stack.pop()
            turt.setheading(angl)
            turt.up()
            turt.goto(pos[0], pos[1])
            turt.down()
    cv = turt.getscreen()
    cv.getcanvas().postscript(file=PATH_IMG+".fractal_plant.eps")
    window.exitonclick()
    image = Image.open(PATH_IMG+".fractal_plant.eps")
    image.save(PATH_IMG+"fractal_plant.png") 
    os.remove(PATH_IMG+".fractal_plant.eps")

if __name__ == '__main__':
    file = open(PATH_DOCS+"strings_generated.txt", "w")
    bt_instructions = create_l_system(grammar_binary_tree, '0', 5)
    file.write("Binary Tree:\n")
    file.write("\t" + bt_instructions + "\n\n")
    draw_binary_tree(bt_instructions, 45, 20)
    kc_instructions = create_l_system(grammar_koch_curve, 'F', 4)
    file.write("Koch Curve:\n")
    file.write("\t" + kc_instructions + "\n\n")
    draw_koch_curve(kc_instructions, 90, 8)
    sp_instructions = create_l_system(grammar_sierpinski_triangle, 'F-G-G', 5)
    file.write("Sierpinski Triangle:\n")
    file.write("\t" + sp_instructions + "\n\n")
    draw_sierpinski_triangle(sp_instructions, 120, 15)
    dc_instructions = create_l_system(grammar_dragon_curve, 'F', 11)
    file.write("Dragon Curve\n")
    file.write("\t" + dc_instructions + "\n\n")
    draw_dragon_curve(dc_instructions, 90, 9)
    fp_instructions = create_l_system(grammar_fractal_plant, 'X', 5)
    file.write("Fractal Plant:\n")
    file.write("\t" + fp_instructions)
    draw_fractal_plant(fp_instructions, 25, 8)
    file.close()
    print("You can see the image generated in the directory "+PATH_IMG)
    print("You can see strings generated in the file "+PATH_DOCS+"strings_generated.txt")

    