#-*- coding: utf-8 -*-
import sys
import struct
from memarea import memarea
from page import page

class process:

    def _parse_line(self, line, aid):
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
            name = ""
        new = memarea(aid, base, end, perm, inode, name, offset=offset,\
                major=major, minor=minor)
        return new

    def parse_maps(self, pid):
        memmap = []
        with open("/proc/"+pid+"/maps", 'r') as file:
            aid = 0
            for line in file:
                line = line.rstrip()
                area = self._parse_line(line, aid)
                memmap.append(area)
                if area == "[heap]":
                    if self.heap == None:
                        self.heap = area
                    else:
                        print "Error: More than one heap?"
                if area == "[stack]":
                    if self.stack == None:
                        self.stack = area
                    else:
                        print "Error: More than one stack?"
                aid = aid + 1
        return memmap

    def get_md5(self):
        return self.maps_md5

    def set_memareas(self, newmap):
        self.memareas = newmap

    def get_memareas(self):
        return self.memareas

    def get_pagemap(self):
        return self.pagemap

    def set_md5(self, md5):
        self.maps_md5 = md5

    def get_stack(self):
        return self.stack

    def get_heap(self):
        return self.heap

    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def extract_name(self, pid):
        with open("/proc/"+pid+"/comm", 'r') as file:
            return file.read().rstrip()

    def display(self):
        print "pid: {} - name: {} - areas: {}".format(self.pid,
                self.name, len(self.areas))

    def __init__(self, pid):
        self.pid = pid
        self.name = self.extract_name(pid)
        self.areas = self.parse_maps(pid);
        self.heap = None
        self.stack = None
        self.maps_md5 = 0
