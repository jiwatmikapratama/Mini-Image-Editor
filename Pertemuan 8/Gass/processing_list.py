from PIL import Image, ImageOps
import math

from numpy import size

def ImgNegative(img_input,coldepth):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1])) 
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j)) 
            pixels[i,j] = (255-r, 255-g, 255-b) 
    
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB") 
    
    return img_output

def ImgRotate(img_input,coldepth,deg,direction): 
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
    pixels = img_output.load()
    
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if(direction=="CW"):
                if deg==90:
                    r, g, b = img_input.getpixel((j,img_output.size[0]-i-1))
                elif deg==180:
                    r, g, b = img_input.getpixel((img_output.size[0]-i-1,img_input.size[1]-j-1))
                elif deg==270:
                    r, g, b = img_input.getpixel((img_output.size[0]-j-1,i))
            
            elif(direction=="CCW"):
                if deg == 90:
                    r, g, b = img_input.getpixel((img_output.size[0]-j-1,i))
                elif deg == 180:
                    r, g, b = img_input.getpixel((img_output.size[0]-i-1,img_input.size[1]-j-1))
                elif deg == 270:
                    r, g, b = img_input.getpixel((j,img_output.size[0]-i-1))
            pixels[i,j] = (r, g, b)

    return img_output

def ImgThreshold(img_input,coldepth,value):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i,j))
            if(r>value) and (g>value) and (b>value):
                pixels[i,j] = (255,255,255)
            else:
                pixels[i,j] = (0,0,0)
    
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    
    return img_output

def PenjumlahanCitra(img_input,coldepth,value):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i,j))
            r = r+value
            g = g+value
            b = b+value
            if(r>255):
                r=255
            if(g>255):
                g=255
            if(b>255):
                b=255
            pixels[i,j] = (r,g,b)
                
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output
    
def PenguranganCitra(img_input,coldepth,value):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i,j))
            r = r-value
            g = g-value
            b = b-value
            if(r<0):
                r=0
            if(g<0):
                g=0
            if(b<0):
                b=0
            pixels[i,j] = (r,g,b)
                
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
    
def PenguranganCitra(img_input,coldepth,value):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i,j))
            r = r-value
            g = g-value
            b = b-value
            if(r<0):
                r=0
            if(g<0):
                g=0
            if(b<0):
                b=0
            pixels[i,j] = (r,g,b)
                
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
    
def PerkalianCitra(img_input,coldepth,value):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i,j))
            r = r*value
            g = g*value
            b = b*value
            if(r>255):
                r=255
            if(g>255):
                g=255
            if(b>255):
                b=255
            pixels[i,j] = (r,g,b)
                
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
    
def PembagianCitra(img_input,coldepth,value):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i,j))
            r = r//value
            g = g//value
            b = b//value
            if(r<0):
                r=0
            if(g<0):
                g=0
            if(b<0):
                b=0
            pixels[i,j] = (r,g,b)
                
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def LogarithmicTransform(img_input,coldepth,value):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            r = value*(math.log(1+r))
            g = value*(math.log(1+g))
            b = value*(math.log(1+b))
            if(r>255):
                r=255
            if(g>255):
                g=255
            if(b>255):
                b=255
                
            if(r<0):
                r=0
            if(g<0):
                g=0
            if(b<0):
                b=0
            pixels[i,j] = (int(r),int(g),int(b))
                
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
    
def PowerLawTransform(img_input,coldepth,value):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            r = value*(r/value)**0.5
            g = value*(g/value)**0.5
            b = value*(b/value)**0.5

            if(r>255):
                r=255
            if(g>255):
                g=255
            if(b>255):
                b=255

            if(r<0):
                r=0
            if(g<0):
                g=0
            if(b<0):
                b=0
            pixels[i,j] = (int(r),int(g),int(b))
                
    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
    
def ImgTranslasi(img_input,coldepth,translasi_x,translasi_y): 
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i,j))
            if(img_output.size[0] > i+translasi_x):
                x = i+translasi_x
            else:
                x = img_output.size[1]-1
            
            if(img_output.size[1] > j+translasi_y):
                y = j+translasi_x
            else:
                y = img_output.size[0]-1
            pixels[x,y] = (r, g, b)

    return img_output

def ImgFlip(img_input,coldepth,direction):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1])) 
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if direction==1:
                pixels[i,j] = img_input.getpixel((img_output.size[0]-1-i,j))
            elif direction==2:
                pixels[i,j] = img_input.getpixel((i,img_output.size[1]-j-1))
            elif direction==3:
                pixels[i,j] = img_input.getpixel((img_output.size[0]-1-i,img_output.size[1]-j-1))
    
    return img_output

def ImgRotate(img_input,coldepth,deg,direction): 
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
    pixels = img_output.load()
    
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if(direction=="CW"):
                if deg==90:
                    r, g, b = img_input.getpixel((j,img_output.size[0]-i-1))
                elif deg==180:
                    r, g, b = img_input.getpixel((img_output.size[0]-i-1,img_input.size[1]-j-1))
                elif deg==270:
                    r, g, b = img_input.getpixel((img_output.size[0]-j-1,i))
            
            elif(direction=="CCW"):
                if deg == 90:
                    r, g, b = img_input.getpixel((img_output.size[0]-j-1,i))
                elif deg == 180:
                    r, g, b = img_input.getpixel((img_output.size[0]-i-1,img_input.size[1]-j-1))
                elif deg == 270:
                    r, g, b = img_input.getpixel((j,img_output.size[0]-i-1))
            pixels[i,j] = (r, g, b)

    return img_output

def ZoomOut(img_input,coldepth,value):
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    rowOut = img_input.size[0]//value
    colOut = img_input.size[1]//value
    img_output = Image.new('RGB',(rowOut, colOut))
    pixels = img_output.load()

    for i in range(0, rowOut-1):
        for j in range(0, colOut-1):
            r, g, b = img_input.getpixel((i*value,j*value))
            pixels[i,j] = (r,g,b)
    
    return img_output

def ZoomIn(img_input,coldepth,value):
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 
 
    rowOut = img_input.size[0]*value
    colOut = img_input.size[1]*value
    img_output = Image.new('RGB',(rowOut,colOut)) 
    pixels = img_output.load() 

    for i in range(rowOut-1): 
        for j in range(colOut-1):
            r, g, b = img_input.getpixel((int(i/value),int(j/value)))

            pixels[i,j] = (r,g,b)
    
    return img_output

def Median(img_input, coldepth, value):
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 
 
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1])) 
    pixels = img_output.load()
    if value == 3:
        mask = [(0,0)] * 3 * 3
        size = 3 * 3
        sort = int(size/2)
        for i in range(img_output.size[0]-1):
            for j in range(img_output.size[1]-1):
                mask[0] = img_input.getpixel((i-1,j-1))
                mask[1] = img_input.getpixel((i-1,j))
                mask[2] = img_input.getpixel((i-1,j+1))

                mask[3] = img_input.getpixel((i,j-1))
                mask[4] = img_input.getpixel((i,j))
                mask[5] = img_input.getpixel((i,j+1))

                mask[6] = img_input.getpixel((i+1,j-1))
                mask[7] = img_input.getpixel((i+1,j))
                mask[8] = img_input.getpixel((i+1,j+1))

                mask.sort()
                pixels[i,j] = (mask[sort])
            
    if value == 5:
        mask = [(0,0)] * 5 * 5
        size = 5 * 5
        sort = int(size/2)
        for i in range(img_output.size[0]-2):
            for j in range(img_output.size[1]-2):
                mask[0] = img_input.getpixel((i-2,j-2))
                mask[1] = img_input.getpixel((i-2,j-1))
                mask[2] = img_input.getpixel((i-2,j))
                mask[3] = img_input.getpixel((i-2,j+1))
                mask[4] = img_input.getpixel((i-2,j+2))

                mask[5] = img_input.getpixel((i-1,j-2))
                mask[6] = img_input.getpixel((i-1,j-1))
                mask[7] = img_input.getpixel((i-1,j))
                mask[8] = img_input.getpixel((i-1,j+1))
                mask[9] = img_input.getpixel((i-1,j+2))

                mask[10] = img_input.getpixel((i,j-2))
                mask[11] = img_input.getpixel((i,j-1))
                mask[12] = img_input.getpixel((i,j))
                mask[13] = img_input.getpixel((i,j+1))
                mask[14] = img_input.getpixel((i,j+2))

                mask[15] = img_input.getpixel((i+1,j-2))
                mask[16] = img_input.getpixel((i+1,j-1))
                mask[17] = img_input.getpixel((i+1,j))
                mask[18] = img_input.getpixel((i+1,j+1))
                mask[19] = img_input.getpixel((i+1,j+2))

                mask[20] = img_input.getpixel((i+2,j-2))
                mask[21] = img_input.getpixel((i+2,j-1))
                mask[22] = img_input.getpixel((i+2,j))
                mask[23] = img_input.getpixel((i+2,j+1))
                mask[24] = img_input.getpixel((i+2,j+2))

                mask.sort()
                pixels[i,j] = (mask[sort])

    if value == 7:
        mask = [(0,0)] * 7 * 7
        size = 7 * 7
        sort = int(size/2)
        for i in range(img_output.size[0]-3):
            for j in range(img_output.size[1]-3):
                mask[0] = img_input.getpixel((i-3,j-3))
                mask[1] = img_input.getpixel((i-3,j-2))
                mask[2] = img_input.getpixel((i-3,j-1))
                mask[3] = img_input.getpixel((i-3,j))
                mask[4] = img_input.getpixel((i-3,j+1))
                mask[5] = img_input.getpixel((i-3,j+2))
                mask[6] = img_input.getpixel((i-3,j+3))

                mask[7] = img_input.getpixel((i-2,j-3))
                mask[8] = img_input.getpixel((i-2,j-2))
                mask[9] = img_input.getpixel((i-2,j-1))
                mask[10] = img_input.getpixel((i-2,j))
                mask[11] = img_input.getpixel((i-2,j+1))
                mask[12] = img_input.getpixel((i-2,j+2))
                mask[13] = img_input.getpixel((i-2,j+3))

                mask[14] = img_input.getpixel((i-1,j-3))
                mask[15] = img_input.getpixel((i-1,j-2))
                mask[16] = img_input.getpixel((i-1,j-1))
                mask[17] = img_input.getpixel((i-1,j))
                mask[18] = img_input.getpixel((i-1,j+1))
                mask[19] = img_input.getpixel((i-1,j+2))
                mask[20] = img_input.getpixel((i-1,j+3))

                mask[21] = img_input.getpixel((i,j-3))
                mask[22] = img_input.getpixel((i,j-2))
                mask[23] = img_input.getpixel((i,j-1))
                mask[24] = img_input.getpixel((i,j))
                mask[25] = img_input.getpixel((i,j+1))
                mask[26] = img_input.getpixel((i,j+2))
                mask[27] = img_input.getpixel((i,j+3))

                mask[28] = img_input.getpixel((i+1,j-3))
                mask[29] = img_input.getpixel((i+1,j-2))
                mask[30] = img_input.getpixel((i+1,j-1))
                mask[31] = img_input.getpixel((i+1,j))
                mask[32] = img_input.getpixel((i+1,j+1))
                mask[33] = img_input.getpixel((i+1,j+2))
                mask[34] = img_input.getpixel((i+1,j+3))

                mask[35] = img_input.getpixel((i+2,j-3))
                mask[36] = img_input.getpixel((i+2,j-2))
                mask[37] = img_input.getpixel((i+2,j-1))
                mask[38] = img_input.getpixel((i+2,j))
                mask[39] = img_input.getpixel((i+2,j+1))
                mask[40] = img_input.getpixel((i+2,j+2))
                mask[41] = img_input.getpixel((i+2,j+3))

                mask[42] = img_input.getpixel((i+3,j-3))
                mask[43] = img_input.getpixel((i+3,j-2))
                mask[44] = img_input.getpixel((i+3,j-1))
                mask[45] = img_input.getpixel((i+3,j))
                mask[46] = img_input.getpixel((i+3,j+1))
                mask[47] = img_input.getpixel((i+3,j+2))
                mask[48] = img_input.getpixel((i+3,j+3))

                mask.sort()
                pixels[i,j] = (mask[sort])

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def Mean(img_input, coldepth, value):
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 
 
    rowOut = img_input.size[0]
    colOut = img_input.size[1]
    img_output = Image.new('RGB',(rowOut,colOut)) 
    pixels = img_output.load() 

    if value == 3:
        mask = [(0,0)] * 3 * 3
        maskbaru = [(0,0)] * 3 * 3

        for i in range(1, rowOut-1): 
            for j in range(1, colOut-1):
                red = 0
                green = 0
                blue = 0
                mask[0] = img_input.getpixel((i-1,j-1))
                mask[1] = img_input.getpixel((i-1,j))
                mask[2] = img_input.getpixel((i-1,j+1))

                mask[3] = img_input.getpixel((i,j-1))
                mask[4] = img_input.getpixel((i,j))
                mask[5] = img_input.getpixel((i,j+1))

                mask[6] = img_input.getpixel((i+1,j-1))
                mask[7] = img_input.getpixel((i+1,j))
                mask[8] = img_input.getpixel((i+1,j+1))

                def div(mask):
                    r,g,b = mask
                    r = int (r/9)
                    g = int (g/9)
                    b = int (b/9)
                    newmask = (r,g,b)
                    return newmask

                for k in range(8):
                    maskbaru[k] = div(mask[k])
                    r,g,b = maskbaru[k]
                    red = red + r
                    green = green + g
                    blue = blue + b
        
                pixels[i,j] = (red,green,blue)

    elif value == 5:
        mask = [(0,0)] * 5 * 5
        maskbaru = [(0,0)] * 5 * 5

        for i in range(1, rowOut-2): 
            for j in range(1, colOut-2):
                red = 0
                green = 0
                blue = 0
                mask[0] = img_input.getpixel((i-2,j-2))
                mask[1] = img_input.getpixel((i-2,j-1))
                mask[2] = img_input.getpixel((i-2,j))
                mask[3] = img_input.getpixel((i-2,j+1))
                mask[4] = img_input.getpixel((i-2,j+2))

                mask[5] = img_input.getpixel((i-1,j-2))
                mask[6] = img_input.getpixel((i-1,j-1))
                mask[7] = img_input.getpixel((i-1,j))
                mask[8] = img_input.getpixel((i-1,j+1))
                mask[9] = img_input.getpixel((i-1,j+2))

                mask[10] = img_input.getpixel((i,j-2))
                mask[11] = img_input.getpixel((i,j-1))
                mask[12] = img_input.getpixel((i,j))
                mask[13] = img_input.getpixel((i,j+1))
                mask[14] = img_input.getpixel((i,j+2))

                mask[15] = img_input.getpixel((i+1,j-2))
                mask[16] = img_input.getpixel((i+1,j-1))
                mask[17] = img_input.getpixel((i+1,j))
                mask[18] = img_input.getpixel((i+1,j+1))
                mask[19] = img_input.getpixel((i+1,j+2))

                mask[20] = img_input.getpixel((i+2,j-2))
                mask[21] = img_input.getpixel((i+2,j-1))
                mask[22] = img_input.getpixel((i+2,j))
                mask[23] = img_input.getpixel((i+2,j+1))
                mask[24] = img_input.getpixel((i+2,j+2))

                def div(mask):
                    r,g,b = mask
                    r = int (r/25)
                    g = int (g/25)
                    b = int (b/25)
                    newmask = (r,g,b)
                    return newmask

                for k in range(24):
                    maskbaru[k] = div(mask[k])
                    r,g,b = maskbaru[k]
                    red = red + r
                    green = green + g
                    blue = blue + b
        
                pixels[i,j] = (red,green,blue)

    elif value == 7:
        mask = [(0,0)] * 7 * 7
        maskbaru = [(0,0)] * 7 * 7

        for i in range(1, rowOut-3): 
            for j in range(1, colOut-3):
                red = 0
                green = 0
                blue = 0
                mask[0] = img_input.getpixel((i-3,j-3))
                mask[1] = img_input.getpixel((i-3,j-2))
                mask[2] = img_input.getpixel((i-3,j-1))
                mask[3] = img_input.getpixel((i-3,j))
                mask[4] = img_input.getpixel((i-3,j+1))
                mask[5] = img_input.getpixel((i-3,j+2))
                mask[6] = img_input.getpixel((i-3,j+3))

                mask[7] = img_input.getpixel((i-2,j-3))
                mask[8] = img_input.getpixel((i-2,j-2))
                mask[9] = img_input.getpixel((i-2,j-1))
                mask[10] = img_input.getpixel((i-2,j))
                mask[11] = img_input.getpixel((i-2,j+1))
                mask[12] = img_input.getpixel((i-2,j+2))
                mask[13] = img_input.getpixel((i-2,j+3))

                mask[14] = img_input.getpixel((i-1,j-3))
                mask[15] = img_input.getpixel((i-1,j-2))
                mask[16] = img_input.getpixel((i-1,j-1))
                mask[17] = img_input.getpixel((i-1,j))
                mask[18] = img_input.getpixel((i-1,j+1))
                mask[19] = img_input.getpixel((i-1,j+2))
                mask[20] = img_input.getpixel((i-1,j+3))

                mask[21] = img_input.getpixel((i,j-3))
                mask[22] = img_input.getpixel((i,j-2))
                mask[23] = img_input.getpixel((i,j-1))
                mask[24] = img_input.getpixel((i,j))
                mask[25] = img_input.getpixel((i,j+1))
                mask[26] = img_input.getpixel((i,j+2))
                mask[27] = img_input.getpixel((i,j+3))

                mask[28] = img_input.getpixel((i+1,j-3))
                mask[29] = img_input.getpixel((i+1,j-2))
                mask[30] = img_input.getpixel((i+1,j-1))
                mask[31] = img_input.getpixel((i+1,j))
                mask[32] = img_input.getpixel((i+1,j+1))
                mask[33] = img_input.getpixel((i+1,j+2))
                mask[34] = img_input.getpixel((i+1,j+3))

                mask[35] = img_input.getpixel((i+2,j-3))
                mask[36] = img_input.getpixel((i+2,j-2))
                mask[37] = img_input.getpixel((i+2,j-1))
                mask[38] = img_input.getpixel((i+2,j))
                mask[39] = img_input.getpixel((i+2,j+1))
                mask[40] = img_input.getpixel((i+2,j+2))
                mask[41] = img_input.getpixel((i+2,j+3))

                mask[42] = img_input.getpixel((i+3,j-3))
                mask[43] = img_input.getpixel((i+3,j-2))
                mask[44] = img_input.getpixel((i+3,j-1))
                mask[45] = img_input.getpixel((i+3,j))
                mask[46] = img_input.getpixel((i+3,j+1))
                mask[47] = img_input.getpixel((i+3,j+2))
                mask[48] = img_input.getpixel((i+3,j+3))
                
                def div(mask):
                    r,g,b = mask
                    r = int (r/49)
                    g = int (g/49)
                    b = int (b/49)
                    newmask = (r,g,b)
                    return newmask

                for k in range(48):
                    maskbaru[k] = div(mask[k])
                    r,g,b = maskbaru[k]
                    red = red + r
                    green = green + g
                    blue = blue + b
        
                pixels[i,j] = (red,green,blue)
 
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB") 
 
    return img_output