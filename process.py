#-*- coding: utf-8 -*-
import sys
import struct
from memarea import memarea
from page import page

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

    def parse_pagemap(self, pid, start, count):
        pagemap = []
	offset  = (start / 4096) * 8
        with open("/proc/"+pid+"/pagemap", 'r') as file:
		file.seek(offset, 0)
		for i in range(1, count):
			entry = struct.unpack('Q', file.read(8))[0]
			if not entry:
				break;
	                pagemap.append(page(entry))
        return pagemap

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

    def __init__(self, pid):
        self.areas = self.parse_maps(pid);
	start = 0
	count = 10
        self.pagemap = self.parse_pagemap(pid, start, count);
