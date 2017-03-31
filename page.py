#-*- coding: utf-8 -*-

class page:
	def __init__(self, entry):
		self.pfn = entry & ((1<<55) - 1)
		self.dirty = entry & (1 << 55)
		self.exclusive = entry & (1 << 56);
		self.filepage = entry & (1 << 61);
		self.swapped = entry & (1 << 62);
		self.present = entry & (1 << 64);

	def get_pfn(self):
		return self.pfn

	def get_dirty(self):
		return self.dirty

	def get_exclusive(self):
		return self.exclusive

	def get_filepage(self):
		return self.filepage

	def get_swapped(self):
		return self.swapped

	def get_present(self):
		return self.present

	def display(self):
		print "pfn="+self.pfn+" dirt="+self.dirty+" excl="+\
				self.exclusive+\
				" file-page="+self.filepage+" swap="\
				+self.swapped+" pres="+self.present

	def find_memarea(self, memmap):
		for i in range(len(memmap)):
			if memmap[i].get_base() <= (self.pfn << 12)\
					<= memmap[i].get_end():
				return memmap[i]
