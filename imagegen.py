from wand.image import Image
import time
from tqdm import tqdm
import os
from os import listdir, mkdir
from os.path import isfile, join, isdir, dirname, splitext
from pathlib import Path
import sys

def generate():
    arg = sys.argv[1]
    photos = [join(arg, f) for f in listdir(arg) if isfile(join(arg, f))];
    if not isdir(join(arg,"thumbs")):
        mkdir(join(arg,"thumbs"));
        for photo in tqdm(photos):
            thumb(photo);
            time.sleep(0.1)
    print("Thumbnails generated.")
    if not isdir(join(arg,"smallthumbs")):
        mkdir(join(arg,"smallthumbs"));
        for photo in tqdm(photos):
            smallthumb(photo);
            time.sleep(0.1)
    print("Small thumbnails generated.")
    if not isdir(join(arg,"main")):
        mkdir(join(arg,"main"));
        for photo in tqdm(photos):
            main(photo);
            time.sleep(0.1)
    print("Mains generated.")

def thumb(photo):
    with Image(filename=photo) as p:
        factor = 800/p.width
        p.resize(width=int(p.width * factor), height=int(p.height * factor));
        p.save(filename="".join((dirname(photo),"/thumbs/",Path(photo).stem,"t",splitext(photo)[1])));

def smallthumb(photo):
    with Image(filename=photo) as p:
        factor = 400/p.width
        p.resize(width=int(p.width * factor), height=int(p.height * factor));
        p.save(filename="".join((dirname(photo),"/smallthumbs/",Path(photo).stem,"st",splitext(photo)[1])));

def main(photo):
    with Image(filename=photo) as p:
        factor = 1600/p.width
        p.resize(width=int(p.width * factor), height=int(p.height * factor));
        p.save(filename="".join((dirname(photo),"/main/",Path(photo).stem,"m",splitext(photo)[1])));


if __name__ == '__main__':
    generate()
