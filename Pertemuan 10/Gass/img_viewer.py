import PySimpleGUI as sg
import os.path
from PIL import Image, ImageOps
from processing_list import *

sg.theme('TanBlue')

# Kolom Area No 1: Area open folder and select image
file_list_column = [
 [
 sg.Text("Open Image Folder :"),
 ],
 [
 sg.In(size=(20, 1), enable_events=True, key="ImgFolder"),
 sg.FolderBrowse(),
 ],
 [
 sg.Text("Choose an image from list :"),
 ],
 [
 sg.Listbox(
 values=[], enable_events=True, size=(18, 10), key="ImgList"
 )
 ],
]
# Kolom Area No 2: Area viewer image input
image_viewer_column = [
 [sg.Text("Image Input :")],
 [sg.Text(size=(40, 1), key="FilepathImgInput")],
 [sg.Image(key="ImgInputViewer")],
]
# Kolom Area No 3: Area Image info dan Tombol list of processing
list_processing = [
 [
 sg.Text("Image Information:"),
 ],
 [
 sg.Text(size=(20, 1), key="ImgSize"),
 ],
 [
 sg.Text(size=(20, 1), key="ImgColorDepth"),
 ],
 [
 sg.Text("List of Processing:"),
 ],
 [
 sg.Button("Image Negative", size=(20, 1), key="ImgNegative"),
 ],
 [
 sg.Text("Image Rotate",size=(20, 1)),
 ],
 [
 sg.Radio('90', 1,True,key="90"),
 sg.Radio('180', 1,key="180"),
 sg.Radio('270', 1,key="270"),
 ],
 [
 sg.Text('Pilih Arah'),
 sg.Radio('CW', 2,True,key="CW"),
 sg.Radio('CCW', 2,key="CCW"),
 ],
 [
 sg.Button("Image Rotate", size=(10, 1), key="ImgRotate"),
 ],
 [
 sg.InputText(size=(5, 1), enable_events=True, key="value_threshold"),
 sg.Button("Img Threshold", size=(10, 1), key="ImgThreshold"),
 ],
 
 [
 sg.InputText(size=(5, 1), enable_events=True, key="value_penjumlahan"),
 sg.Button("Brightness", size=(10, 1), key="PenjumlahanCitra"),
 ],
 
 [
 sg.InputText(size=(5, 1), enable_events=True, key="value_pengurangan"),
 sg.Button("Darken", size=(10, 1), key="PenguranganCitra"),
 ],
 
 [
 sg.InputText(size=(5, 1), enable_events=True, key="value_perkalian"),
 sg.Button("Perkalian", size=(10, 1), key="PerkalianCitra"),
 ],
 
 [
 sg.InputText(size=(5, 1), enable_events=True, key="value_pembagian"),
 sg.Button("Pembagian", size=(10, 1), key="PembagianCitra"),
 ],
 
 [
 sg.InputText(size=(5, 1), enable_events=True, key="value_logarithmictransform"),
 sg.Button("Logarithmic Transform", size=(10, 1), key="LogarithmicTransform"),
 ],
 
 [
 sg.InputText(size=(5, 1), enable_events=True, key="value_powerlawtransform"),
 sg.Button("Power Law Transform", size=(10, 1), key="PowerLawTransform"),
 ],
 [
 sg.Text("Image Translasi",size=(20, 1)),
 ],
 [
 sg.Text("X",size=(3, 1)),
 sg.InputText(size=(5, 1), enable_events=True, key="nilai_x"),
 sg.Text("Y",size=(3, 1)),
 sg.InputText(size=(5, 1), enable_events=True, key="nilai_y"),
 ],
 [
 sg.Button("Image Translasi", size=(12, 1), key="ImgTranslasi"),
 ],
 [
 sg.Text("Image Flipping",size=(20, 1)),
 ],
 [
 sg.Radio('Horizontal', 1,True,key="1"),
 sg.Radio('Vertikal', 1,key="2"),
 ],
 [
 sg.Radio('Horizontal Vertikal', 1,key="3"),
 sg.Button("Image Flip", size=(10, 1), key="ImgFlip"),
 ],
 [
 sg.InputText(size=(5, 1), enable_events=True, key="value_zoomout"),
 sg.Button("Zoom Out", size=(10, 1), key="ZoomOut"),
 ],
 [
 sg.InputText(size=(5, 1), enable_events=True, key="value_zoomin"),
 sg.Button("Zoom In", size=(10, 1), key="ZoomIn"),
 ],
 [
 sg.Text("Image Filtering",size=(15, 1)),
 sg.InputText(size=(5, 1), enable_events=True, key="value_filter"),
 ],
 [
 sg.Button("Median", size=(7, 1), key="Median"),
 sg.Button("Mean", size=(7, 1), key="Mean"),
 sg.Button("Konvolusi", size=(7, 1), key="Konvolusi"),
 ],
 [
 sg.Button("Edge Detection", size=(7, 1), key="EdgeDetection"),
 ],
]
# Kolom Area No 4: Area viewer image output
image_viewer_column2 = [
 [sg.Text("Image Processing Output:")],
 [sg.Text(size=(40, 1), key="ImgProcessingType")],
 [sg.Image(key="ImgOutputViewer")],
]
# Gabung Full layout
layout = [
 [
 sg.Column(file_list_column),
 sg.VSeperator(),
 sg.Column(image_viewer_column),
 sg.VSeperator(),
 sg.Column(list_processing),
 sg.VSeperator(),
 sg.Column(image_viewer_column2),
 ]
]
window = sg.Window("Mini Image Editor", layout)
#nama image file temporary setiap kali processing output 
filename_out = "out.png"
# Run the Event Loop
while True:
 event, values = window.read()
 if event == "Exit" or event == sg.WIN_CLOSED:
     break
 # Folder name was filled in, make a list of files in the folder
 if event == "ImgFolder":
    folder = values["ImgFolder"]
    try:
 # Get list of files in folder
            file_list = os.listdir(folder)
    except:
            file_list = [] 
    fnames = [
            f 
            for f in file_list 
            if os.path.isfile(os.path.join(folder, f)) 
            and f.lower().endswith((".png", ".gif")) 
    ]  
    
    window["ImgList"].update(fnames)
 elif event == "ImgList": # A file was chosen from the listbox
    try:
        filename = os.path.join( 
            values["ImgFolder"], values["ImgList"][0] 
        )
        window["FilepathImgInput"].update(filename)
        window["ImgInputViewer"].update(filename=filename) 
        window["ImgProcessingType"].update(filename) 
        window["ImgOutputViewer"].update(filename=filename) 
        img_input = Image.open(filename) 
        #img_input.show() 
    
        #Size 
        img_width, img_height = img_input.size 
        window["ImgSize"].update("Image Size : "+str(img_width)+" x "+str(img_height)) 
    
        #Color depth 
        mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 
    24, "HSV": 24, "I": 32, "F": 32} 
        coldepth = mode_to_coldepth[img_input.mode] 
        window["ImgColorDepth"].update("Color Depth : "+str(coldepth)) 
    except: 
        pass
 elif event == "ImgNegative": 
    try: 
        window["ImgProcessingType"].update("Image Negative") 
        img_output= ImgNegative(img_input,coldepth) 
        img_output.save(filename_out) 
        window["ImgOutputViewer"].update(filename=filename_out) 
    except: 
        pass

 elif event == "ImgRotate":
    try:
        if(values["CW"]==True):
           direction = "CW"
        else:
            direction = "CCW"

        if(values["90"] == True):
            deg = 90
        elif(values["180"] == True):
            deg = 180
        elif(values["270"] == True):
            deg = 270

        window["ImgProcessingType"].update("Image Rotate")
        img_output=ImgRotate(img_input,coldepth,deg,direction)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "ImgThreshold":
    try:
        value = int (values['value_threshold'])
        window["ImgProcessingType"].update("Image Threshold")
        img_output=ImgThreshold(img_input,coldepth,value)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "PenjumlahanCitra":
    try:
        value = int (values['value_penjumlahan'])
        window["ImgProcessingType"].update("Brightness")
        img_output=PenjumlahanCitra(img_input,coldepth,value)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "PenguranganCitra":
    try:
        value = int (values['value_pengurangan'])
        window["ImgProcessingType"].update("Darken")
        img_output=PenguranganCitra(img_input,coldepth,value)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "PerkalianCitra":
    try:
        value = int (values['value_perkalian'])
        window["ImgProcessingType"].update("Perkalian")
        img_output=PerkalianCitra(img_input,coldepth,value)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "PembagianCitra":
    try:
        value = int (values['value_pembagian'])
        window["ImgProcessingType"].update("Pembagian")
        img_output=PembagianCitra(img_input,coldepth,value)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass
    
 elif event == "LogarithmicTransform":
    try:
        value = int (values['value_logarithmictransform'])
        window["ImgProcessingType"].update("Logarithmic Transform")
        img_output=LogarithmicTransform(img_input,coldepth,value)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass
    
 elif event == "PowerLawTransform":
    try:
        value = int (values['value_powerlawtransform'])
        window["ImgProcessingType"].update("Power Law Transform")
        img_output=PowerLawTransform(img_input,coldepth,value)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "ImgTranslasi":
    try:
        x = int (values['nilai_x'])
        y = int (values['nilai_y'])
        window["ImgProcessingType"].update("Image Translasi")
        img_output=ImgTranslasi(img_input,coldepth,x,y)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "ImgFlip":
    try:
        if(values["1"] == True):
            direction = 1
        elif(values["2"] == True):
            direction = 2
        elif(values["3"] == True):
            direction = 3

        window["ImgProcessingType"].update("Image Flip")
        img_output=ImgFlip(img_input,coldepth,direction)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "ZoomOut":
    try:
        value = int (values['value_zoomout'])
        window["ImgProcessingType"].update("Zoom Out")
        img_output=ZoomOut(img_input,coldepth,value)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "ZoomIn":
    try:
        value = int (values['value_zoomin'])
        window["ImgProcessingType"].update("Zoom In")
        img_output=ZoomIn(img_input,coldepth,value)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "Median": 
    try:
        value = int (values['value_filter'])
        window["ImgProcessingType"].update("Median") 
        img_output= Median(img_input,coldepth,value)
        img_output.save(filename_out) 
        window["ImgOutputViewer"].update(filename=filename_out) 
    except: 
        pass

 elif event == "Mean": 
    try:
        value = int (values['value_filter'])
        window["ImgProcessingType"].update("Mean") 
        img_output= Mean(img_input,coldepth, value) 
        img_output.save(filename_out) 
        window["ImgOutputViewer"].update(filename=filename_out) 
    except: 
        pass

 elif event == "Konvolusi": 
    try:
        value = int (values['value_filter'])
        window["ImgProcessingType"].update("Konvolusi") 
        img_output= Konvolusi(img_input,coldepth, value) 
        img_output.save(filename_out) 
        window["ImgOutputViewer"].update(filename=filename_out) 
    except: 
        pass

 elif event == "EdgeDetection": 
    try:
        window["ImgProcessingType"].update("Edge Detection") 
        img_output= EdgeDetection(img_input,coldepth) 
        img_output.save(filename_out) 
        window["ImgOutputViewer"].update(filename=filename_out) 
    except: 
        pass


window.close()