#!/usr/bin/python3
from re import search
import sys
import numpy as np 
from matplotlib import pyplot as plt

def data_after_keyword(logfile,keyword):
    ''' Extract data from infile after the keyword. '''
    try:
        data = []
        patt = '%s (\d+\.?\d?)' % keyword
        with open(logfile, 'r') as fi:
            for eachLine in fi:
                s = search(patt, eachLine)
                if s is not None:
                    data.append(float(s.group(1)))
        return data
    except IOError:
        print("Open file [%s] or [%s] failed!" % (self.infile, self.outfile))
        return False

if __name__ == '__main__':
    logfile = sys.argv[1]
    keyword ="cpu"
    cpudata = data_after_keyword(logfile,keyword)
    keyword = "mem"
    memdata = data_after_keyword(logfile,keyword)

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.set(title='CPU',ylabel='free')
    ax2.set(title='MEM',ylabel='free', xlabel='time')
    ax1.plot(cpudata, '.r',)
    ax2.plot(memdata, '.r',)
    plt.show()

#print(data)

