var page = require("webpage").create();
 
var url= "file:///home/anup/projects/docnyte/sample.html";
 
page.open(url, function(success) {
	page.render('screenshot.pdf');
	slimer.exit();
})
