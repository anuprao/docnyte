import re

import markdown
from markdown.preprocessors import Preprocessor

pattern_start = None
pattern_end = None

class MyPreprocessor(Preprocessor):			
	def run(self,lines):
		global pattern_start
		global pattern_end
		
		print "running through floats"
		
		new_lines = []
		
		#print len(lines), lines
		
		for line in lines:
			m_start = pattern_start.match(line)
			m_end = pattern_end.match(line)
			
			#print m_start,m_end,line
			#print
			
			if None==m_start and None==m_end :
				new_lines.append(line)
				
			else:
				# print m_start,line
				if m_start:
					print "start ..."
					new_lines.append('<div markdown="1" style="display:float; float:right">')
				
				if m_end:
					print "end ..."
					new_lines.append('</div>')
		
		return new_lines
        
class MyFloatRight(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
		global pattern_start
		global pattern_end
		
		pattern_start = re.compile(r'(--)(floatright-start)--')
		pattern_end = re.compile(r'(--)(floatright-end)--')
		
		md.preprocessors.add('floatright', MyPreprocessor(md), "_begin")        
		
def makeExtension(configs=[]):
    return MyFloatRight(configs=configs)  
