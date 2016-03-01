var express = require('express');
var router = express.Router();
var cassandra = require('cassandra-driver');

var client = new cassandra.Client({contactPoints: ['128.138.202.117','128.138.202.110']});
client.connect(function(err,result){
	console.log('index file: cassandra connected');
});

var getCruzWeekly = 'SELECT * FROM candidates.cruzweeklyaverages';
/* GET home page. */
router.get('/', function(req, res, next) {
  client.execute(getCruzWeekly,[], function(err,result){
	  if(err){
		  res.status(404).send({msg: err});
	  } else{
		  res.render('index', {
			  cruzweeklyaverages: result.rows
			  })
		  }
	  });
});

module.exports = router;
