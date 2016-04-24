// Declares the initial angular module "ngc". Module grabs other controllers and services.
var app = angular.module('ngc', ['headerCtrl', 'ngRoute', 'ui.bootstrap'])

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

        }).when('/team', {
            controller: 'teamController',
            templateUrl: 'partials/team.html'

        }).when('/sponsor', {
            controller: 'sponsorController',
            templateUrl: 'partials/sponsor.html'
        // If none of the above, back to the FusionCharts and description
      }).otherwise({redirectTo: '/'});

    });
//
// Controller Section
//
//Controller for Home Page
app.controller('HomeController', function($scope, $location){
  var gdelt = new FusionCharts( "FusionCharts/msline.swf",
                                        "gdeltChartId", "100%","500","0","0");
			gdelt.setJSONUrl("GDELTAll.json");
			gdelt.render("gdeltChart");

  var candidates = new FusionCharts( "FusionCharts/msline.swf",
                                        "candidateChartId", "100%", "500", "0", "0");
			candidates.setJSONUrl("TwitterAllDaily.json");
			candidates.render("candidatesChart");

  var polls = new FusionCharts( "FusionCharts/msline.swf",
                                        "pollsChartId", "100%", "500", "0", "0");
			polls.setJSONUrl("PollsAll.json");
			polls.render("pollsChart");
});
//Main Page Controller
app.controller('mainController', function($scope, $location){});

//Controllers for all html pages in the partials folder
app.controller('trumpController', function($scope, $location){

  $scope.message = 'Donald Trump Analysis'
  $scope.myInterval = -1;
  $scope.noWrapSlides = false;
  $scope.active = 0;
  var slides = $scope.slides = [];
  var currIndex = 0;
  var images = [
  'reporttrumpGDELTPolls.png', 'reporttrumpGDELTTwitter.png', 'reporttrumpTwitterPolls.png'
  ]
  var text = [
    'reporttrumpGDELTPolls.txt', 'reporttrumpGDELTTwitter.txt', 'reporttrumpTwitterPolls.txt'
  ]
  $scope.addSlide = function() {
    var newWidth = 600 + slides.length;
    slides.push({
      image: '../analysis-images/' + images[currIndex],
      text: '../analysis-images/' + text[currIndex],
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

app.controller('cruzController', function($scope, $location){

  $scope.message = 'Ted Cruz Analysis'
  $scope.myInterval = -1;
  $scope.noWrapSlides = false;
  $scope.active = 0;
  var slides = $scope.slides = [];
  var currIndex = 0;
  var images = [
  'reportcruzGDELTPolls.png', 'reportcruzGDELTTwitter.png', 'reportcruzTwitterPolls.png'
  ]
  var text = [
    'reportcruzGDELTPolls.txt', 'reportcruzGDELTTwitter.txt', 'reportcruzTwitterPolls.txt'
  ]
  $scope.addSlide = function() {
    var newWidth = 600 + slides.length;
    slides.push({
      image: '../analysis-images/' + images[currIndex],
      text: '../analysis-images/' + text[currIndex],
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

app.controller('rubioController', function($scope, $location){
	$scope.message = 'Marco Rubio Analysis'
});

app.controller('kasichController', function($scope, $location){

  $scope.message = 'John Kasich Analysis'
  $scope.myInterval = -1;
  $scope.noWrapSlides = false;
  $scope.active = 0;
  var slides = $scope.slides = [];
  var currIndex = 0;
  var images = [
  'reportkasichGDELTPolls.png', 'reportkasichGDELTTwitter.png', 'reportkasichTwitterPolls.png'
  ]
  var text = [
    'reportkasichGDELTPolls.txt', 'reportkasichGDELTTwitter.txt', 'reportkasichTwitterPolls.txt'
  ]
  $scope.addSlide = function() {
    var newWidth = 600 + slides.length;
    slides.push({
      image: '../analysis-images/' + images[currIndex],
      text: '../analysis-images/' + text[currIndex],
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

app.controller('sandersController', function($scope, $location){

  $scope.message = 'Bernie Sanders Analysis'
  var myChart = new FusionCharts( "FusionCharts/line.swf",
                                    "myChartId", "100%", "500", "0", "0");
  myChart.setJSONUrl("sandersJson.json");
  myChart.render("chartContainer");
  $scope.myInterval = -1;
  $scope.noWrapSlides = false;
  $scope.active = 0;
  var slides = $scope.slides = [];
  var currIndex = 0;
  var images = [
  'reportsandersGDELTPolls.png', 'reportsandersGDELTTwitter.png', 'reportsandersTwitterPolls.png'
  ]
  var text = [
    'reportsandersGDELTPolls.txt', 'reportsandersGDELTTwitter.txt', 'reportsandersTwitterPolls.txt'
  ]
  $scope.addSlide = function() {
    var newWidth = 600 + slides.length;
    slides.push({
      image: '../analysis-images/' + images[currIndex],
      text: '../analysis-images/' + text[currIndex],
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

app.controller('clintonController', function($scope, $location){

  $scope.message = 'Hillary Clinton Analysis'
  $scope.myInterval = -1;
  $scope.noWrapSlides = false;
  $scope.active = 0;
  var slides = $scope.slides = [];
  var currIndex = 0;
  var images = [
  'reportclintonGDELTPolls.png', 'reportclintonGDELTTwitter.png', 'reportclintonTwitterPolls.png'
  ]
  var text = [
    'reportclintonGDELTPolls.txt', 'reportclintonGDELTTwitter.txt', 'reportclintonTwitterPolls.txt'
  ]
  $scope.addSlide = function() {
    var newWidth = 600 + slides.length;
    slides.push({
      image: '../analysis-images/' + images[currIndex],
      text: '../analysis-images/' + text[currIndex],
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
app.controller('analysisController', function($scope, $location){

  $scope.myInterval = -1;
  $scope.noWrapSlides = false;
  $scope.active = 0;
  var slides = $scope.slides = [];
  var currIndex = 0;
  var images = [
  'Tweet_Word2Vec_Analysis_kasich.png', 'Tweet_Word2Vec_Analysis_sanders.png', 'Clustering_Candidates.gif','Clustering_Candidates.png'
  ]
  var text = [
    'Tweet_Word2Vec_Analysis_kasich.txt', 'Tweet_Word2Vec_Analysis_sanders.txt', 'Clustering_Candidates.txt', 'Clustering_Candidates.txt'
  ]
  $scope.addSlide = function() {
    var newWidth = 600 + slides.length;
    slides.push({
      image: '../analysis-images/' + images[currIndex],
      text: '../analysis-images/' + images[currIndex],
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
	$scope.message = 'The Team!'
});
app.controller('sponsorController', function($scope, $location){
	$scope.message = 'Sponsor Page'
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
