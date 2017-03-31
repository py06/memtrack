#-*- coding: utf-8 -*-

class memarea:
    def __init__(self, base, end, perm, inode, name, offset, major, minor):
        self.name = name;
        self.base = base;
        self.end = end;
        self.perm = perm;
        self.inode = inode;
        self.offset = offset;
        self.dev_maj = major;
        self.dev_min = minor;

    def get_size(self):
        return self.end - self.base;

    def get_base(self):
        return self.base;

    def get_end(self):
        return self.end;

    def get_perm(self):
        return self.perm;

    def get_perm_readable(self):
        str = ""
        if (self.perm[0] == 'r'):
            str = "VM_READ | ";
        if (self.perm[1] == 'w'):
            str += "VM_WRITE | ";
        if (self.perm[2] == 'x'):
            str += "VM_EXEC | ";
        if (self.perm[3] == 'p'):
            str += "VM_PRIVATE";
        return str;

    def get_size(self):
        return int(self.end, 16) - int(self.base, 16);

    def get_inode(self):
        return self.inode;

    def get_name(self):
        return self.name;

    def get_offset(self):
        return self.offset;

    def get_device(self):
        return self.major+":"+self.minor;

    def display(self):
        print "Memory range: base = @"+self.get_base()+" (sz="+str(self.get_size())+")"
	print "	 permission = "+self.get_perm_readable()+" inode = "+\
                self.get_inode()+" name = "+self.name

