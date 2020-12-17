from shutil import copyfile

n = 'positives.txt'
folderName = "images/"
outFolder = "pos/"
f = open(n,'r')
for filename in f:
    name = filename.split('/')[1]
    copyfile(filename.rstrip(),outFolder + name.rstrip())