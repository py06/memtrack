#!/usr/bin/python
import argparse
import sys
import hashlib
import time
from process import process
from memarea import memarea


def md5_maps(pid):
    return hashlib.md5(open("/proc/"+pid+"/maps", 'r').read()).hexdigest()

def memtrack(pid):
    print "Tracking memory usage of process " +pid
    proc = process(pid)

    while (1):
        md5 = md5_maps(pid) #compute md5sum on /proc/<pid>/maps and
                            #see if antyhing changed
        if md5 != proc.get_md5():
            memmap = proc.parse_maps(pid);
            # do things with areas

            # commit them in proc object
            proc.set_memareas(memmap)
            proc.set_md5(md5_maps(pid))
            for i in range(len(memmap)):
                    memmap[i].display()

        time.sleep(1)

    return 0




def check_arg(args=None):
    parser = argparse.ArgumentParser(description='memtrack: process memory tracker')
    parser.add_argument('-p', '--pid', help='process id (pid)', required='True')

    results = parser.parse_args(args)
    return (results.pid)

if __name__ == '__main__':
    pid = check_arg(sys.argv[1:])
    memtrack(pid)

