from PIL import Image
import math
figure=" "
regular=" "
em = " "
en = " "
scale = ["█" ,"▓","▒", "░", " "]
def main(filename, output="", dither=True, inverse = False, pixelWidth = 2, space = ""):
    if space != "":
        scale[4] = space
    image = Image.open(filename).convert("L")
    imgdump = image.load()
    if output != "":
        output_file = open(output,"wb")
    for y in range(image.height):
        string = ""
        #output_file.write(bytes([9]))
        for x in range(image.width):
            pixel = imgdump[x,y]

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
            output_file.write(string.encode('utf_8'))
            output_file.write(bytes([13,10]))
    if output != "":
        output_file.close()

main("D:\\Noam10\\Documents\\Desktop\\Parapluie\\__sonic_team_anime_style___by_tamber_mizuki-d4ae8z1.png", output="D:\\Noam10\\Documents\\Desktop\\Parapluie\\sonic3.txt", dither=True, inverse=False, pixelWidth = 1)