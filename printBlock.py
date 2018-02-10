from PIL import Image
import math
figure=" "
regular=" "
em = " "
en = " "
blocks = [" ", "▘", "▝", "▀", "▖","▍", "▞", "▛", "▗", "▚", "▐", "▜", "▄", "▙", "▜", "█"]
def algebraicBool(bool):
    if bool:
        return 1
    return 0
def main(filename, output="", dither=True, inverse = False, space=""):
    image = Image.open(filename).convert("1", dither=(1 if dither else 0))
    imgdump = image.load()
    if space != "":
        blocks[0] = space
    if output != "":
        output_file = open(output,"wb")
    for y in range(0, image.height, 2):
        string = ""
        for x in range(0, image.width, 2):
            charnum = algebraicBool(inverse) * 15
            if imgdump[(x,y)] == 0:
                charnum+=1 * (algebraicBool(not inverse) - algebraicBool(inverse))
            if x+1 != image.width and imgdump[(x+1,y)] == 0:
                charnum+=2 * (algebraicBool(not inverse) - algebraicBool(inverse))
            if y+1 != image.height and imgdump[(x,y+1)] == 0:
                charnum += 4 * (algebraicBool(not inverse) - algebraicBool(inverse))
            if x+1 != image.width and y+1 != image.height and imgdump[(x+1,y+1)] == 0:
                charnum+=8 * (algebraicBool(not inverse) - algebraicBool(inverse))
            string += blocks[charnum]

        if output == "":
            print(string)
        else:
            output_file.write(string.encode('utf_8'))
            output_file.write(bytes([13,10]))
    if output != "":
        output_file.close()

main("D:\\Noam10\\Documents\\Desktop\\Parapluie\\__sonic_team_anime_style___by_tamber_mizuki-d4ae8z1.png", output="D:\\Noam10\\Documents\\Desktop\\Parapluie\\sonic4.txt", dither=True, inverse=False)