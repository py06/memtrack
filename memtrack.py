#!/usr/bin/python
import argparse
import sys
import hashlib
import time
from process import process
from memarea import memarea


def md5_maps(pid):
    return hashlib.md5(open("/proc/"+pid+"/maps", 'r').read()).hexdigest()

def list_areas(proc, query):
    areas = proc.get_memareas()
    for i in range(len(areas)):
        areas[i].display()

def process_query(proc, query):
    proc.display()

def map_query(proc, query):
    result = set()
    areas = proc.get_memareas()
    if query[0] == 'l':
        #Get all mapped files
        for i in range(len(areas)):
            name = areas[i].get_name()
            if name != "" and name[0] != '[':
                result.add(name)
        for i in result:
            print i
    elif query[0] == 'f':
        #List all vmas linked to file
        for i in range(len(areas)):
            if len(query) >=2 and areas[i].get_name() == query[2:]:
                result.add(areas[i])
        for i in result:
            i.display()

def help_info():
    print "P - process info"
    print "    "
    print "L - List memory areas"
    print "    "
    print "M - Memory areas info"
    print " Ml - list mapped files by process"
    print " Mf <mapped filename> - list areas associated to mapped file"
    print "    "
    print "Q - Quit"


def console(proc):
    query = raw_input("$ ")
    if query == "":
        return
    if query[0] == 'V':
        return area_query(proc, query[1:])
    elif query[0] == 'P':
        return process_query(proc, query[1:])
    elif query[0] == 'L':
        return list_areas(proc, query[1:])
    elif query[0] == 'M':
        return map_query(proc, query[1:])
    elif query[0] == 'Q':
        sys.exit(0)
    else:
        return help_info()


def memtrack(pid):
    print "Tracking memory usage of process " +pid
    proc = process(pid)

    while (1):
        md5 = md5_maps(pid) #compute md5sum on /proc/<pid>/maps and
                            #see if antyhing changed
        if md5 != proc.get_md5():
            print "Event: memareas changed\n"
            memmap = proc.parse_maps(pid);
            # commit them in proc object
            proc.set_memareas(memmap)
            proc.set_md5(md5_maps(pid))

        console(proc)
    return 0




def check_arg(args=None):
    parser = argparse.ArgumentParser(description='memtrack: process memory tracker')
    parser.add_argument('-p', '--pid', help='process id (pid)', required='True')

    results = parser.parse_args(args)
    return (results.pid)

if __name__ == '__main__':
    pid = check_arg(sys.argv[1:])
    memtrack(pid)

