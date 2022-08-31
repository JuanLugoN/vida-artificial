from PIL import Image, ImageDraw

WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,128,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PINK = (255,192,203)
PURPLE = (160,32,240)
ORANGE = (255,165,0)
MAROON = (128,0,0)
TEAL = (0, 128, 128)
VIOLET = (143, 0, 255)
WIDTH = 0
HEIGHT = 0

def collatz(number):
    lst=[]
    lst.append(number)
    while(number!=1):
        if(number%2==0):
            number=number//2
            lst.append(number)
        else:
            number=number*3+1
            lst.append(number)
    return lst

def obtener_valores_dibujo(collatz):
    coordenas = []
    yi = 0
    yf = 50
    xmax = 0
    for numero in collatz:
        numero = [int(d) for d in str(numero)]
        xi = 0
        xf = 50
        for digito in numero:
            coordenas.append(([xi, yi, xf, yf], digito))
            xi+=50
            xf+=50
        if xf > xmax: xmax = xf
        yi+=50
        yf+=50
    return coordenas, xmax, yf

if __name__ == "__main__":
    coloracion = {1:RED, 2:GREEN, 3:BLUE, 4: YELLOW, 5: PINK, 
                  6: PURPLE, 7: ORANGE, 8:MAROON, 9: TEAL, 0: VIOLET}
    n = 0
    while n <= 0:
        n = input('Ingrese un número: ')
        n = n = int(n) if n.isdigit() else 0
    print(collatz(n))
    coordenadas, WIDTH, HEIGHT = obtener_valores_dibujo(collatz(n))
    img = Image.new( 'RGB', (WIDTH,HEIGHT), WHITE)
    draw = ImageDraw.Draw(img)
    for xy, z in coordenadas:
        color = coloracion[z]
        draw.rectangle(xy, fill = color, outline = color)
    img.show()
