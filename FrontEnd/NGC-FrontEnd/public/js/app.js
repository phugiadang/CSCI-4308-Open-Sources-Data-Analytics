// Declares the initial angular module "ngc". Module grabs other controllers and services.
var app = angular.module('ngc', ['queryCtrl', 'headerCtrl', 'ngRoute', 'ui.bootstrap'])

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
                                        "twitterChartId", "100%", "500", "0", "0");
			candidatesChart.setJSONUrl("TwitterAll.json");
			candidatesChart.render("candidatesChart");

  var pollsChart = new FusionCharts( "FusionCharts/msline.swf",
                                        "pollsChartId", "100%", "500", "0", "0");
			candidatesChart.setJSONUrl("PollsAll.json");
			candidatesChart.render("pollsChart");
});
//Main Page Controller
app.controller('mainController', function($scope, $location){});

//Controllers for all html pages in the partials folder
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

  $scope.myInterval = 5000;
  $scope.noWrapSlides = false;
  $scope.active = 0;
  var slides = $scope.slides = [];
  var currIndex = 0;
  var images = [
  'Twitter_vs_GDELT_clinton.png', 'Twitter_vs_GDELT_cruz.png', 'Twitter_vs_GDELT_kasich.png', 'Twitter_vs_GDELT_rubio.png', 'Twitter_vs_GDELT_sanders.png', 'Twitter_vs_GDELT_trump.png', 'Twitter_vs_GDELT.png', 'User_Sentiment_Analysis_kasich.png', 'User_Sentiment_Analysis_kasich.png'
  ]
  $scope.addSlide = function() {
    var newWidth = 600 + slides.length;
    slides.push({
      image: '../analysis-images/' + images[currIndex],
      text: ['Nice image','Awesome photograph','That is so cool','I love that'][slides.length % 4],
      id: currIndex++
    });
  };

  $scope.randomize = function() {
    var indexes = generateIndexesArray();
    assignNewIndexesToSlides(indexes);
  };

  for (var i = 0; i < images.length; i++) {
    $scope.addSlide();
  }

  // Randomize logic below

  function assignNewIndexesToSlides(indexes) {
    for (var i = 0, l = slides.length; i < l; i++) {
      slides[i].id = indexes.pop();
    }
  }
});
app.controller('teamController', function($scope, $location){
	$scope.message = 'Hillary Clinton Analysis'
});
app.controller('sponsorController', function($scope, $location){
	$scope.message = 'Hillary Clinton Analysis'
});
//Navigation Bar Functionality
  //This is what directs us to each dropdown page and changes routes
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
