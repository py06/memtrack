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
	
	def display(self):
		print "Memory range: base = @"+self.base+" end = @"+self.end
		print "	 permission: = "+self.perm
		print "	 inode: = "+self.inode
		print "	 name: = "+self.name
