#-*- coding: utf-8 -*-
import struct
from page import page

class memarea:
    def __init__(self, area_id, base, end, perm, inode, name, offset, major, minor):
        self.name = name
        self.area_id = area_id
        self.base = base
        self.end = end
        self.perm = perm
        self.inode = inode
        self.offset = offset
        self.dev_maj = major
        self.dev_min = minor

    def get_size(self):
        return self.end - self.base

    def get_base(self):
        return self.base

    def get_end(self):
        return self.end

    def get_perm(self):
        return self.perm

    def get_perm_readable(self):
        str = ""
        if (self.perm[0] == 'r'):
            str = "VM_READ | "
        if (self.perm[1] == 'w'):
            str += "VM_WRITE | "
        if (self.perm[2] == 'x'):
            str += "VM_EXEC | "
        if (self.perm[3] == 'p'):
            str += "VM_PRIVATE"
        return str

    def get_size(self):
        return int(self.end, 16) - int(self.base, 16)

    def get_inode(self):
        return self.inode

    def get_name(self):
        return self.name

    def get_area_id(self):
        return self.area_id

    def set_area_id(self, aid):
        self.area_id = aid

    def get_offset(self):
        return self.offset

    def get_device(self):
        return self.major+":"+self.minor

    def find_area_pages(self, pid, start, count):
        pagemap = []
	offset  = (start / 4096) * 8
        with open("/proc/"+pid+"/pagemap", 'r') as file:
		file.seek(offset, 0)
		for i in range(1, count):
			entry = struct.unpack('Q', file.read(8))[0]
			if not entry:
				break
	                pagemap.append(page(entry))
        return pagemap

    def dump_pages(self, pid, start=0, count=1):
       pages = self.find_area_pages(pid, int(self.base, 16), count)
       for i in range(len(pages)):
           pages[i].display()

    def display(self, short=True):
        if short == True:
            print "{} - @{} (sz={}) perm={} name={}".format(self.area_id,
                    self.base,\
                    self.get_size(), self.perm, self.name)
        else:
            print self.area_id+" Memory range: base = @"+self.get_base()+" (sz="+\
                    str(self.get_size())+")"
	    print "	 permission = "+self.get_perm_readable()+" inode = "+\
                    self.get_inode()+" name = "+self.name

