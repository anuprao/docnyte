//phantom.injectJs("static/jquery/jquery-1.10.2.js");
//$('body').css('background', 'white');

var page = require('webpage').create();
page.paperSize = {
    format: 'A4',
    orientation: 'portrait'
};


page.open('file:///home/anup/projects/docnyte/sample.html', function(status) {
	console.log("Status: " + status);
	
	if(status === "success") {
		page.render('sample.pdf');
	}

	phantom.exit();
});
