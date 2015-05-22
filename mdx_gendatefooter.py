import re
import datetime

import markdown
from markdown.preprocessors import Preprocessor

pattern = None

class MyPreprocessor(Preprocessor):			
	def run(self,lines):
		global pattern
		
		print "running through gendates"
		
		new_lines = []
		
		#print len(lines), lines
		
		today = datetime.date.today()
		
		for line in lines:
			m_start = pattern.match(line)
			
			#print m_start,m_end,line
			#print
			
			if None==m_start :
				new_lines.append(line)
				
			else:
				# print m_start,line
				if m_start:
					new_lines.append('<div markdown="1" class="gendatefooter">')
					new_lines.append("*Revised on: **" + today.strftime('%d %b %Y') + "***")
					new_lines.append("<br/>")
					new_lines.append("*Created using [https://github.com/anuprao/docnyte](https://github.com/anuprao/docnyte)*")
					new_lines.append('</div>')
		
		return new_lines
        
class MyFloatRight(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
		global pattern
		
		pattern = re.compile(r'(--)(gendatefooter)--')
		
		md.preprocessors.add('gendatefooter', MyPreprocessor(md), "_begin")        
		
def makeExtension(configs=[]):
    return MyFloatRight(configs=configs)  
