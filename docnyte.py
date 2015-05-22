import sys
import codecs

import markdown
from markdown.preprocessors import Preprocessor
from jinja2 import Template

if 2 > len(sys.argv) :
	print "Usage syntax : docnyte input_file"
	
# print sys.argv

fpMD = codecs.open(sys.argv[1],"r", "utf-8")
strMarkDown = fpMD.read()
fpMD.close()

fpTemplate = codecs.open("template.html","r", "utf-8")
strTemplate = fpTemplate.read()
fpTemplate.close()

oTemplate = Template(strTemplate)

mdProcessor = markdown.Markdown(output_format="html5", extensions=['extra','codehilite', 'myextension', 'floatright', 'footer', 'referencerequest', 'gendatefooter'])
html_md = mdProcessor.convert(strMarkDown)
htmltext = oTemplate.render(markdown_content=html_md)

fpHTML = codecs.open("sample.html","w", "utf-8")
fpHTML.write(htmltext)
fpMD.close()
