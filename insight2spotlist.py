from __future__ import print_function
from Mapping import loadmapping
from glob import glob

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
    except:
        return choice

def get_insight_file(filelist = None):
    if filelist is None:
        filelist = glob('*.txt')
    for i, fname in enumerate(filelist):
        print('[%2d] %s' % (i+1, fname))
    choice = raw_input("Select datafile from Insight, or give filename:")
    try:
        return imlist[int(choice) - 1]
    except:
        return choice

def main():
    mapfile_name = get_filename('Select mapfile, or give filename', 
                                guess = '*_1_20')
    mapping = Mapping.loadmapping(mapfile_name)

    spotlistname = raw_input("Name for the spotlist file?")
    spotlist = open(spotlistname, 'w')

    spotlist.write('FileName=%s;\n\n' % get_imagename())

    spotlist.write('Sx\tSy\tStart\tEnd\tPeak\tFlag\n')

    datalist = glob('*.txt')

    while True:
       fname = get_insight_file(datalist) 
       try:
           datalist.remove(fname)
       except:
           pass

       start = get_int("Enter starting frame: ")
       start = get_int("Enter ending frame: ")

       insight = open(fname)
       insight.readline()
       x,y = zip(*((line.split()[1], line.split()[2]) for line in infile))
       x = map(float, x)
       y = map(float, y)

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

       again_q = raw_input("Another frame? [y]/n")
       if again_q.lower().startswith('n'):
           break

if __name__ == "__main__":
    main()
