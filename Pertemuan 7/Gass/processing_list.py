from PIL import Image, ImageOps
import math

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

def Median(img_input, coldepth):
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 
 
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1])) 
    pixels = img_output.load() 

    for i in range(img_output.size[0]-1):
        for j in range(img_output.size[1]-1):
            mask = [img_input.getpixel((i-1, j-1)),
                    img_input.getpixel((i-1, j)),
                    img_input.getpixel((i-1, j+1)),
                    img_input.getpixel((i, j-1)),
                    img_input.getpixel((i, j)),
                    img_input.getpixel((i, j+1)),
                    img_input.getpixel((i+1, j-1)),
                    img_input.getpixel((i+1, j)),
                    img_input.getpixel((i+1, j+1)),
            ]
            mask.sort()
            pixels[i,j] = (mask[4])

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def Mean(img_input, coldepth):
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 
 
    rowOut = img_input.size[0]
    colOut = img_input.size[1]
    img_output = Image.new('RGB',(rowOut,colOut)) 
    pixels = img_output.load() 

    mask = [(0,0)] * 9
    maskbaru = [(0,0)] * 9

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
 
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB") 
 
    return img_output