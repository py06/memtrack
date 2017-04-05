#-*- coding: utf-8 -*-
import os

class page:
	def __init__(self, entry, virt=0):
		self.virt = virt
		self.pfn = entry & ((1<<55) - 1)
		self.pagesize = os.sysconf("SC_PAGE_SIZE")
                self.swtyp = entry & (0x1f) #swap type (if swapped =1)
                self.swoff = (entry & ((1 << 55) -1) >> 4)
		self.dirty = (entry & (1 << 55)) >> 55
		self.exclusive = (entry & (1 << 56)) >> 56
		self.filepage = (entry & (1 << 61)) >> 61
		self.swapped = (entry & (1 << 62)) >> 62
		self.present = (entry & (1 << 63)) >> 63

	def is_contained(self, address):
		if self.virt <= int(address, 16) and\
			self.virt + self.pagesize > int(address, 16):
			return True
		return False

	def get_virt(self):
		return self.virt

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
		print "virt={} pfn={} dirt={} excl={} file-page={} swap={} pres={}"\
                               .format(hex(self.virt >> 12), hex(int(self.pfn)),
                                       self.dirty,\
                               self.exclusive,
                                        self.filepage, self.swapped,
                                        self.present)

	def find_memarea(self, memmap):
		for i in range(len(memmap)):
			if memmap[i].get_base() <= (self.pfn << 12)\
					<= memmap[i].get_end():
				return memmap[i]
