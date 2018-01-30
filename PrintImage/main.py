from PIL import Image
import math
scale = ["█" ,"▓","▒", "░",  " "]
def main(filename, output="", dither=True, inverse = False, pixelWidth = 2):
    image = Image.open(filename).convert("L")
    imgdump = image.load()
    if output != "":
        output_file = open(output,"wb")
    for y in range(image.height):
        string = ""
        #output_file.write(bytes([9]))
        for x in range(image.width):
            pixel = imgdump[x,y]
            print(pixel)
            if (pixel > 256):
                pixel = 256
            if (inverse):
                string += scale[4-(pixel // 52)] * pixelWidth
            else:
                string += scale[pixel // 52] * pixelWidth
            if dither:
                error=pixel%52
                if x!=image.width-1:
                   imgdump[x+1,y] += math.floor((7/16)*error)
                if y!=image.height-1 and x!=image.width-1:
                    imgdump[x+1,y+1] += math.floor((1/16)*error)
                if y!=image.height-1:
                    imgdump[x,y+1] += math.floor((5/16)*error)
                if x!=0 and y!=image.height-1:
                    imgdump[x-1,y+1] += math.floor((3/16)*error)
        if output == "":
            print(string)
        else:
            print("nl")
            output_file.write(string.encode('utf_8'))
            output_file.write(bytes([13,10]))
    if output != "":
        print("fin")
        output_file.close()

main("D:\\Noam10\\Documents\\Documents\\pichu\\lapis.jpg", output="D:\\Noam10\\Documents\\Documents\\pichu\\lp.txt", dither=True, inverse=False, pixelWidth = 2)