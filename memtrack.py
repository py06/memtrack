import argparse
import sys
import hashlib
import time
from memarea import memarea


areas = []
maps_md5 = ""


def parse_line(line):
    line = ' '.join(line.split())
    fields = line.strip(" +").split(" ")
    base = fields[0].split("-")[0]
    end = fields[0].split("-")[1]
    perm = fields[1]
    offset = fields[2]
    major = fields[3].split(":")[0]
    minor = fields[3].split(":")[1]
    inode = fields[4]
    if len(fields) > 5:
        name = fields[5]
    else:
        name = "unknown"
    new = memarea(base, end, perm, inode, name, offset=offset, major=major, minor=minor)
    return new

def md5_maps(pid):
    return hashlib.md5(open("/proc/"+pid+"/maps", 'r').read()).hexdigest()

def read_maps(pid):
    global areas

    with open("/proc/"+pid+"/maps", 'r') as file:
        for line in file:
            line = line.rstrip()
            areas.append(parse_line(line))

def memtrack(pid):
    global maps_md5

    print "Tracking memory usage of process " +pid

    while (1):
        md5 = md5_maps(pid)
        if md5 != maps_md5:
            read_maps(pid);

            for i in range(len(areas)):
                    areas[i].display()

            maps_md5 = md5;
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

