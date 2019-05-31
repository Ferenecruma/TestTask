from PIL import Image
from itertools import chain 
import imagehash
import argparse
import glob

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--path", required = True,
    help = "path to input dataset of images")
args = vars(ap.parse_args())

# creating dictionary for storing images names and their hashes
dictionary = {}

# loop over the image dataset
for imagePath in glob.glob(args["path"] + "/*.jpg"):
    # load the image and compute the difference hash
    image = Image.open(imagePath)
    h = str(imagehash.dhash(image))

    # extract the filename from the path and uptade dictionary
    # using the hash as the key and the filename as value
    
    filename = imagePath[imagePath.rfind("/") + 1:]
    dictionary[filename]=h
    

# finding duplicate names and printing them
flipped = {} 
  
for key, value in dictionary.items(): 
    if value not in flipped: 
        flipped[value] = [key] 
    else: 
        flipped[value].append(key)
        print(flipped[value])





