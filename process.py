#-*- coding: utf-8 -*-
import sys
from memarea import memarea

class process:

    memareas = []
    pagemap = []
    maps_md5 = ""

    def _parse_line(self, line):
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
        new = memarea(base, end, perm, inode, name, offset=offset,\
                major=major, minor=minor)
        return new

    def parse_maps(self, pid):
        memmap = []
        with open("/proc/"+pid+"/maps", 'r') as file:
            for line in file:
                line = line.rstrip()
                memmap.append(self._parse_line(line))
        return memmap

    def get_md5(self):
        return self.maps_md5

    def set_memareas(self, newmap):
        self.memareas = newmap

    def get_memareas(self):
        return self.memareas

    def set_md5(self, md5):
        self.maps_md5 = md5

    def __init__(self, pid):
        self.areas = self.set_memareas(self.parse_maps(pid));
