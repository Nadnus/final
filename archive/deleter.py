import xml.etree.ElementTree as ET
import os

filenames_positivos = []
dimensions = []
for file in os.listdir("./annotations"):
    doc = ET.parse("./annotations/"+file)
    root = doc.getroot()
    if len(root.findall("object")) == 1:
        a = root[4][0].text
        if a == "with_mask":
                filenames_positivos.append(file.split('.')[0] + ".png")

        
f = open("positives.txt", "w+")
for name in filenames_positivos:
    f.write('images/'+ name + '\n')

