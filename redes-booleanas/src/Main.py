from PIL import Image, ImageDraw
from random_boolean_network import RBN
import sys
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir('../img')
PATH_IMG = os.getcwd()+'/'

SIZE = 10

BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

def uso():
    print(f"Uso: python3 {sys.argv[0]} N")
    exit(1)

def main():
    if (len(sys.argv) < 2):
        uso()
    try:
        N = int(sys.argv[1])
    except: uso()
    if (N < 1):
        uso()  
    WIDTH = SIZE * N
    HEIGHT = SIZE * 20
    img = Image.new('RGB', (WIDTH,HEIGHT), BLACK)
    rbn = RBN()
    draw = ImageDraw.Draw(img)
    nodes = rbn.nodes
    enumerated_nodes = enumerate(nodes)
    for i in range(N):
        for j, node in enumerate(nodes):
            if node.state == 1:
                rect = (
                    i * SIZE,         # x1
                    j * SIZE,         # y1
                    i * SIZE + SIZE,  # x2
                    j * SIZE + SIZE   # y2
                )
                draw.rectangle(rect, fill=RED, outline=BLACK)
        rbn.iterate()
    img.save(PATH_IMG+'rbn.png')
    img.save(PATH_IMG+'rbn.eps')
    img.show()
    
if __name__ == "__main__":
    main()
    