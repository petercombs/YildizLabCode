from glob import glob
import shutil
from os.path import isfile

_ip = get_ipython()

MAP = '0716-map_1_20'
OFFSETS = {'1_1': ['1_1','1_2','1_3','1_4'], 
           '1_2': ['1_5','1_6','1_7','1_8'],
           '2_1': ['2_1','2_2','2_3','2_4'],
           '2_2': ['2_5','2_6','2_7','2_8'],
           }
OSBASE = 'offsetsRed-s'
DYNBASE = 'Dyn99-s'

for os in OFFSETS:
    osf = glob(OSBASE + os + '*')[0]
    for dyn in OFFSETS[os]:
        print ("run CombineWHSpots -F -m %s -O 50 -2 %s %s/*.txt" 
                  % (MAP, osf, DYNBASE+dyn))
        print ("run WHData2XML %s.mat %s-FBF.xml -s %s_spotlist.txt"
                  % ((DYNBASE + dyn, )*3))
        _ip.magic("run CombineWHSpots -b 40000 -O 50 -F -m %s -2 %s %s/*.txt" 
                  % (MAP, osf, DYNBASE+dyn))
        _ip.magic("run WHData2XML %s.mat %s-FBF.xml -s %s_spotlist.txt"
                  % ((DYNBASE + dyn, )*3))
        if isfile('blank-MTs.txt'):
            shutil.copyfile('blank-MTs.txt', DYNBASE + dyn + '-MTs.txt')
