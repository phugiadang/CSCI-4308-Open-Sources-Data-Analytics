// Declares the initial angular module "meanMapApp". Module grabs other controllers and services.
var app = angular.module('ngc', ['addCtrl', 'queryCtrl', 'headerCtrl', 'gservice', 'ngRoute'])

    // Configures Angular routing -- showing the relevant view and controller when needed.
    .config(function($routeProvider){

        // Join Team Control Panel
        $routeProvider
        //route for home page
        .when('/', {
            templateUrl: "home.html",
            controller: 'HomeController'
        })
        .when('/trump', {
            controller: 'trumpController',
            templateUrl: 'partials/trump.html'

        // Find Teammates Control Panel
        }).when('/cruz', {
            controller: 'cruzController',
            templateUrl: 'partials/cruz.html'

        // All else forward to the Join Team Control Panel
        }).when('/rubio', {
            controller: 'rubioController',
            templateUrl: 'partials/rubio.html'

        // All else forward to the Join Team Control Panel
        }).when('/clinton', {
            controller: 'clintonController',
            templateUrl: 'partials/clinton.html'

        // All else forward to the Join Team Control Panel
        }).when('/sanders', {
            controller: 'sandersController',
            templateUrl: 'partials/sanders.html'

        // All else forward to the Join Team Control Panel
        }).when('/kasich', {
            controller: 'kasichController',
            templateUrl: 'partials/kasich.html'

        }).when('/analysis', {
              controller: 'analysisController',
              templateUrl: 'partials/analysis.html'

        // All else forward to the Join Team Control Panel
      }).otherwise({redirectTo: '/'});
    });
//
// Controller Section
//
//Controller for Home Page
app.controller('HomeController', function($scope, $location){
  var gdelt = new FusionCharts( "FusionCharts/msline.swf",
                                        "gdeltId", "100%", "500", "0", "0");
			gdelt.setJSONUrl("GDELTAll.json");
			gdelt.render("gdeltChart");

	var candidatesChart = new FusionCharts( "FusionCharts/msline.swf",
                                        "candidateChartId", "100%", "500", "0", "0");
			candidatesChart.setJSONUrl("TwitterAll.json");
			candidatesChart.render("candidatesChart");
});

app.controller('mainController', function($scope, $location){});

app.controller('trumpController', function($scope, $location){
	$scope.message = 'Donald Trump Analysis'
	});
app.controller('cruzController', function($scope, $location){
	$scope.message = 'Ted Cruz Analysis'
	});
app.controller('rubioController', function($scope, $location){
	$scope.message = 'Marco Rubio Analysis'
	});
app.controller('kasichController', function($scope, $location){
	$scope.message = 'John Kasich Analysis'
	});
app.controller('sandersController', function($scope, $location){
	$scope.message = 'Bernie Sanders Analysis'
  var myChart = new FusionCharts( "FusionCharts/line.swf",
                                    "myChartId", "100%", "500", "0", "0");
  myChart.setJSONUrl("sandersJson.json");
  myChart.render("chartContainer");
	});
app.controller('clintonController', function($scope, $location){
	$scope.message = 'Hillary Clinton Analysis'
	});
app.controller('analysisController', function($scope, $location){
  $scope.message = 'Analyses and Correlations'

  $scope.img=[
      // {id:'Twitter vs. GDELT',source:'../images/report.png'},
      // {id:'Trump Top 10',source:'../images/top_ten_webclinton.png'},
      // {id:'Clinton Top 10',source:'../images/top_ten_webtrump.png'},
  ];

  });

app.controller('navCtrl', function ($location, $scope) {
  $scope.currentPage = "home";

  $scope.go = function (page) {
    $location.path('/' + page);
  };
});
app.controller('nav2Ctrl', function ($location, $scope) {
  $scope.currentPage = "home";

  $scope.go = function (page) {
    $location.path('/' + page);
  };
});
//image slider code
