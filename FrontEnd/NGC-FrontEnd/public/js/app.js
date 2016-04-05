// Declares the initial angular module "meanMapApp". Module grabs other controllers and services.
var app = angular.module('ngcFullstack', ['addCtrl', 'queryCtrl', 'headerCtrl', 'gservice', 'ngRoute'])

    // Configures Angular routing -- showing the relevant view and controller when needed.
    .config(function($routeProvider){

        // Join Team Control Panel
        $routeProvider
        //route for home page
        .when('/trump', {
            controller: 'trumpController',
            templateUrl: 'partials/trump.html',

        // Find Teammates Control Panel
        }).when('/cruz', {
            controller: 'cruzController',
            templateUrl: 'partials/cruz.html',

        // All else forward to the Join Team Control Panel
        }).when('/rubio', {
            controller: 'rubioController',
            templateUrl: 'partials/rubio.html',

        // All else forward to the Join Team Control Panel
        }).when('/clinton', {
            controller: 'clintonController',
            templateUrl: 'partials/clinton.html',

        // All else forward to the Join Team Control Panel
        }).when('/sanders', {
            controller: 'sandersController',
            templateUrl: 'partials/sanders.html',

        // All else forward to the Join Team Control Panel
        }).when('/kasich', {
            controller: 'kasichController',
            templateUrl: 'partials/kasich.html',

        }).when('/analysis', {
            controller: 'analysisController',
            templateUrl: 'partials/analysis.html',

        // All else forward to the Join Team Control Panel
      }).when('/', {
          controller: 'analysisController',
          templateUrl: 'partials/home.html',
        })
    });

app.controller('mainController', function($scope){

	var gdelt = new FusionCharts( "FusionCharts/msline.swf",
                                        "gdeltId", "1000", "600", "0", "0");
			gdelt.setJSONUrl("GDELTAll.json");
			gdelt.render("gdeltChart");

	var candidatesChart = new FusionCharts( "FusionCharts/msline.swf",
                                        "candidateChartId", "1000", "600", "0", "0");
			candidatesChart.setJSONUrl("TwitterAll.json");
			candidatesChart.render("candidatesChart");

	});
app.controller('trumpController', function($scope){
	$scope.message = 'Donald Trump Analysis'
	});
app.controller('cruzController', function($scope){
	$scope.message = 'Ted Cruz Analysis'
	});
app.controller('rubioController', function($scope){
	$scope.message = 'Marco Rubio Analysis'
	});
app.controller('kasichController', function($scope){
	$scope.message = 'John Kasich Analysis'
	});
app.controller('sandersController', function($scope){
	$scope.message = 'Bernie Sanders Analysis'
	});
app.controller('clintonController', function($scope){
	$scope.message = 'Hillary Clinton Analysis'
	});
app.controller('analysisController', function($scope){
  $scope.message = 'Analyses and Correlations'

  $scope.img=[
      {id:'Twitter vs. GDELT',source:'../images/report.png'},
      {id:'Trump Top 10',source:'../images/top_ten_webclinton.png'},
      {id:'Clinton Top 10',source:'../images/top_ten_webtrump.png'},
  ];

  });
