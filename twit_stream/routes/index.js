

/*
 * GET home page.
 */

module.exports = function(app) { 
    app.get('/', function(req, res){
	res.render('index', { title: 'Express' }) 
    });

    app.post('/request', function(req, res) {

	
	console.log(req.body);
    });
};
