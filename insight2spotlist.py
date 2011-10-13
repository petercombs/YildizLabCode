from __future__ import print_function
from Mapping import loadmapping
from glob import glob
from math import floor
from collections import defaultdict
from csv import reader as csv_reader

dist = 2
stop = 8

def get_int(prompt):
    while True:
        val = raw_input(prompt)
        try:
            return int(val)
        except ValueError:
            print("'%s' doesn't seem to be an integer" % val)

def get_filename(prompt, guess='', list = None):
    if list is None:
        list = glob(guess)
    for i, fname in enumerate(list):
        print('[%2d] %s' % (i+1, fname))
    choice = raw_input(prompt)
    try:
        return list[int(choice) - 1]
    except:
        return choice


def get_imagename():
    imlist = glob('*.tif')
    for i, im in enumerate(imlist):
        print('[%2d] %s' % (i+1, im))
    choice = raw_input("Select image from list above, or give filename:")
    try:
        return imlist[int(choice) - 1]
    except ValueError as oops:
        print(oops)
        return choice

def get_insight_file(filelist = None):
    if filelist is None:
        filelist = glob('*.txt')
    for i, fname in enumerate(filelist):
        print('[%2d] %s' % (i+1, fname))
    choice = raw_input("Select datafile from Insight, or give filename: ")
    try:
        return filelist[int(choice) - 1]
    except ValueError as oops:
        print(oops)
        return choice

def get_framemap(map_name):
    map_file = open(map_name)

    framemap = {}

    for line in csv_reader(map_file):
        boframe = line[0]
        start = line[2]
        stop = line[3]
        framemap[boframe] = (start, stop)
    return framemap

def main():
    mapfile_name = get_filename('Select mapfile, or give filename: ',
                                guess = '*_1_20')

    #length = get_int('Number of frames per frameset')
    framemap_name = get_filename('Select Insight to tif mapping file, '
                                 'or give filename: ',
                            guess = '*.tsv')

    framemap = get_framemap(framemap_name)


    mapping = loadmapping(mapfile_name)

    spotlistname = raw_input("Name for the spotlist file?")
    spotlist = open(spotlistname, 'w')

    spotlist.write('FileName=%s;\n\n' % get_imagename())

    spotlist.write('Sx\tSy\tStart\tEnd\tFlag\tPeak\n')

    datalist = glob('*.txt')
    n = 1

    fname = get_insight_file(datalist) 
    try:
       datalist.remove(fname)
    except ValueError:
       pass


    insight = open(fname)
    insight.readline()
    x,y, frame = zip(*((line.split()[1], line.split()[2], line.split()[12]) 
                      for line in insight))
    x = map(float, x)
    y = map(float, y)

    framesets = defaultdict(list)

    for xi, yi, framei in zip(x, y, frame):
       framesets[framei].append((xi, yi))

    for frameset in framesets:
        try:
           start, stop = framemap[frameset]
           start = int(start)
           stop = int(stop)
        except:
           print("Can't find start and stops for frame %s" % frameset)
           start = get_int('Enter start frame ')
           stop = get_int('Enter stop frame ')

        x, y = zip(*framesets[frameset])
        xprime, yprime = mapping(x, y)
        for x1, y1 in zip(x, y):
            for x2, y2, x2p, y2p in zip(x, y, xprime, yprime):
               if ((x2p - x1)**2 + (y2p - y1)**2) < dist**2:
                   spotlist.write('%d\t%d\t%d\t%d\t%d\t%d\n' %
                                  (round(x1), round(y1), start, stop, 655, n))
                   spotlist.write('%d\t%d\t%d\t%d\t%d\t%d\n' %
                                  (round(x2), round(y2), start, stop, 585, n))
                   n += 1
                   break #out of the inner loop

        n = floor(n/1000) * 1000 + 1000
    spotlist.close()

if __name__ == "__main__":
    main()
