# ------------------------------
#			Printutils
#	Author: memer-s @devMimer
#		cursor is required
# ------------------------------

import cursor

class Loader:
	def __init__(self, steps, total_segments, segment_char="#", empty_character=" ", loader_name="", overide_last=False):
		self.steps = steps
		self.total_segments = total_segments
		self.segment_length = steps / total_segments
		self.current_segment = 0
		self.loader_progress = 0
		self.loadbar = "["+self.current_segment*segment_char+empty_character*(self.total_segments-self.current_segment)+"]"
		self.segment_char = segment_char
		self.empty_character = empty_character
		self.loader_name = loader_name
		self.overide_last = overide_last
		
	def progress(self):
		cursor.hide()
		self.loader_progress+=1
		if(self.loader_progress > self.current_segment*self.segment_length):
			self.current_segment+=1
			self.loadbar = "["+self.current_segment*self.segment_char+self.empty_character*(self.total_segments-self.current_segment)+"]"
		if(self.loader_progress!=self.steps):
			last_line(str(self.loader_name)+" "+self.loadbar +" "+ str(self.loader_progress)+"/"+str(self.steps)+"                 ")
		else:
			if(self.overide_last):
				last_line(str(self.loader_name)+" "+self.loadbar +" "+ str(self.loader_progress)+"/"+str(self.steps)+"\t DONE")
			else:
				last_line(str(self.loader_name)+" "+self.loadbar +" "+ str(self.loader_progress)+"/"+str(self.steps)+"\t DONE\n")
			cursor.show()

def last_line(string):
	print("\r"+str(string), end="")