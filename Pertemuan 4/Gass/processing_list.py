from PIL import Image, ImageOps
import math

def ImgNegative(img_input,coldepth):
    #solusi 1 
    # img_output=ImageOps.invert(img_input) 
    #solusi 2 
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
    #solusi 1 
    #img_output=img_input.rotate(deg) 
    #solusi 2 
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
    pixels = img_output.load()
    
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if direction=="C":
                r, g, b = img_input.getpixel((j,img_output.size[0]-i-1))
            else:
                r, g, b = img_input.getpixel((img_input.size[1]-j-1,i))
            pixels[i,j] = (r, g, b)

    return img_output

def ImgThreshold(img_input,coldepth):
    #solusi 1
    # img_output=ImageOps.invert(img_input) 
    #solusi 2
    if coldepth!=24:
        img_input = img_input.convert('RGB')
    
    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i,j))
            if(r>127) and (g>127) and (b>127):
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
    #solusi 1
    # img_output=ImageOps.invert(img_input) 
    #solusi 2
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
    #solusi 1
    # img_output=ImageOps.invert(img_input) 
    #solusi 2
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
    #solusi 1
    # img_output=ImageOps.invert(img_input) 
    #solusi 2
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
    #solusi 1
    # img_output=ImageOps.invert(img_input) 
    #solusi 2
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
    #solusi 1
    # img_output=ImageOps.invert(img_input) 
    #solusi 2
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
    #solusi 1
    # img_output=ImageOps.invert(img_input) 
    #solusi 2
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
    #solusi 1
    # img_output=ImageOps.invert(img_input) 
    #solusi 2
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
    

