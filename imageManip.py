myImages = []
for i in range(9):
  file = pickAFile()
  pic = makePicture(file)
  myImages.append(pic)
  
width = getWidth(myImages[0])
height = getHeight(myImages[0])
newImage = makeEmptyPicture(width, height)

theRed = []
theGreen = []
theBlue = []

for j in range(width):
  for k in range(height):
    for image in range(9):
      r = getRed(getPixel(my_images[image], j, k))
      g = getGreen(getPixel(my_images[image], j, k))
      b = getBlue(getPixel(my_images[image], j, k))
      theRed.append(r)
      theGreen.append(g)
      theBlue.append(b)
    theRed.sort()
    theGreen.sort()
    theBlue.sort()
    r = theRed[len(theRed) / 2]
    g = theGreen[len(theGreen) / 2]
    b = theBlue[len(theBlue) / 2]
    setRed(getPixel(newImage, j, k), r)
    setGreen(getPixel(newImage, j, k), g)
    setBlue(getPixel(newImage, j, k), b)
    del theRed[:]
    del theGreen[:]
    del theBlue[:]    
    
show(newImage)