import re

import markdown
from markdown.preprocessors import Preprocessor

pattern = None

class MyPreprocessor(Preprocessor):			
	def run(self,lines):
		global pattern
		
		print "running through page-breaks"
		
		new_lines = []
		
		for line in lines:
			m = pattern.match(line)
			# print m,line
			if m:
				new_lines.append('<p class="pagebreakhere"></p>')
				# print "appending..."
			else:
				new_lines.append(line)
		
		return new_lines
        
class MyExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
		global pattern
		
		pattern = re.compile(r'(--)(pagebreak)--')
		md.preprocessors.add('pagebreaker', MyPreprocessor(md), "_begin")        
		
def makeExtension(configs=[]):
    return MyExtension(configs=configs)  
