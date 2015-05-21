# docnyte

A simple python based markdown processor to generate documents.


## Usage

Supported:

### Step 1

>$ python docnyte

### Step 2

>$ /opt/phantomjs-webfonts/phantomjs --debug=true pdfrender_phantom.js

Not supported: 

>$ docnyte -i resume.md -t pdf -o resume.pdf

## Issues 

Web fonts currently not rendering when using PhantomJS. Alternatively, open genereated HTML in browser and print to PDF.


