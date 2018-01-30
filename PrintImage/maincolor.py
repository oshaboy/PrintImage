from PIL import Image
import termcolor
import math
scale = ["█","▓","▒", "░", " "]
colors = ["grey", "red", "green", "yellow", "blue", "magenta" ,"cyan", "white"]
def contrast(fullpixel):
    return (fullpixel[0] + fullpixel[1] + fullpixel[2]) // 3

def variance(fullpixel):
    avrg = contrast(fullpixel)
    #return math.sqrt(((fullpixel[0]-avrg)*(fullpixel[0]-avrg)+(fullpixel[1]-avrg)*(fullpixel[1]-avrg)+(fullpixel[2]-avrg)*(fullpixel[2]-avrg))/2)
    return ((fullpixel[0]-avrg)+(fullpixel[1]-avrg)+(fullpixel[2]-avrg))/3
def color(fullpixel):
    threshhold = contrast(fullpixel)
    color_index = 0
    varians = variance(fullpixel)
    if (fullpixel[0] >= (threshhold)):
        color_index += 1
    if (fullpixel[1] >= (threshhold)):
        color_index += 2
    if (fullpixel[2] >= (threshhold)):
        color_index += 4
    return colors[color_index]


def main(filename, dither=True, inverse = False, pixelWidth = 2):
    image = Image.open(filename).convert("RGB")
    imgdump = image.load()
    for y in range(image.height):
        string = ""
        for x in range(image.width):
            pixel = imgdump[x,y]
            contras = contrast(pixel)
            col = color(pixel)
            if (contras > 256):
                contras = 256
            if (inverse):
                string += termcolor.colored(scale[4-contras//52]*pixelWidth, col)
            else:
                string += termcolor.colored(scale[contras//52]*pixelWidth, col)
            if dither:
                #red
                rederror=pixel[0]%52
                greenerror=pixel[0]%52
                blueerror=pixel[0]%52
                if x!=image.width-1:
                    r=imgdump[x+1,y][0] + math.floor(rederror*7/16)
                    g = imgdump[x + 1, y][1] + math.floor(greenerror * 7 / 16)
                    b = imgdump[x + 1, y][2] + math.floor(blueerror * 7 / 16)
                    imgdump[x+1,y] = (r,g,b)
                if y!=image.height-1 and x!=image.width-1:
                    r=imgdump[x+1,y+1][0] + math.floor(rederror*1/16)
                    g = imgdump[x + 1, y+1][1] + math.floor(greenerror * 1 / 16)
                    b = imgdump[x + 1, y+1][2] + math.floor(blueerror * 1 / 16)
                    imgdump[x+1,y+1] = (r,g,b)
                if y!=image.height-1:
                    r=imgdump[x,y+1][0] + math.floor(rederror*5/16)
                    g = imgdump[x, y+1][1] + math.floor(greenerror * 5 / 16)
                    b = imgdump[x, y+1][2] + math.floor(blueerror * 5 / 16)
                    imgdump[x,y+1] = (r,g,b)
                if x!=0 and y!=image.height-1:
                    r=imgdump[x-1,y+1][0] + math.floor(rederror*3/16)
                    g = imgdump[x - 1, y+1][1] + math.floor(greenerror * 3 / 16)
                    b = imgdump[x - 1, y+1][2] + math.floor(blueerror * 3 / 16)
                    imgdump[x-1,y+1] = (r,g,b)
        print(string)

main("/home/noambackup/Desktop/sonic_small.bmp", dither=True, inverse=True, pixelWidth = 2)
