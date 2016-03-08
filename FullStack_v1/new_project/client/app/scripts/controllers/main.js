'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
  .controller('MainCtrl', function () {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });

var app = angular.module('DemoApp', ["ng-fusioncharts"])
app.controller('DemoController', function($scope) {

  $scope.dataSource = { "chart":
        {
            "caption":"Sales - 2014 v 2015",
            "numberPrefix":"$",
            "captionFontSize":"14",
            "subcaptionFontSize":"14",
            "baseFontColor":"#666666",
            "baseFont":"Helvetica Neue,Arial",
            "baseFontSize":"11",
            "subcaptionFontBold":"0",
            "canvasBgAlpha":"0",
            "showValues":"0",
            "paletteColors":"#10a9ea,#ebd00f",
            "bgColor":"#f6f6f6",
            "bgAlpha":"100",
            "showBorder":"0",
            "showShadow":"0",
            "showAlternateHGridColor":"0",
            "showXAxisLine":"1",
            "xAxisLineThickness":"1",
            "xAxisLineColor":"#cdcdcd",
            "xAxisNameFontColor":"#8d8d8d",
            "yAxisNameFontColor":"#8d8d8d",
            "canvasBgColor":"#ffffff",
            "lineThickness":"4",
            "anchorBgColor":"#ffffff",
            "legendBgColor":"#ffffff",
            "legendBgAlpha":"100",
            "legendBorderAlpha":"50",
            "legendBorderColor":"#888888",
            "divlineAlpha":"100",
            "divlineColor":"#999999",
            "divlineThickness":"1",
            "divLineIsDashed":"1",
            "divLineDashLen":"1",
            "divLineGapLen":"1",
            "toolTipColor":"#ffffff",
            "toolTipBorderColor":"#ffffff",
            "toolTipBorderThickness":"1",
            "toolTipBgColor":"#000000",
            "toolTipBgAlpha":"80",
            "toolTipBorderRadius":"4",
            "toolTipPadding":"10",
            "toolTipFontSize":"20",
            "anchorRadius":"5",
            "anchorBorderThickness":"3",
            "anchorTrackingRadius":"15",
            "showHoverEffect":"1"
        },
        "categories":[
        {
            "category":[
                {"label":"Jan"},
                {"label":"Feb"},
                {"label":"Mar"},
                {"label":"Apr"},
                {"label":"May"},
                {"label":"Jun"},
                {"label":"Jul"},
                {"label":"Aug"},
                {"label":"Sep"},
                {"label":"Oct"},
                {"label":"Nov"},
                {"label":"Dec"}
            ]
        }],
        "dataset":[
            {"seriesname":"Bakersfield Central",
            "data":[
            {"value":"12123"},
            {"value":"8233"},
            {"value":"25507"},
            {"value":"9110"},
            {"value":"13529"},
            {"value":"8803"},
            {"value":"19202"},
            {"value":"13500"},
            {"value":"16202"},
            {"value":"19200"},
            {"value":"9202"},
            {"value":"11366"}]
        },
            {"seriesname":"Los Angeles Topanga",
            "data":[
            {"value":"13400"},
            {"value":"9800"},
            {"value":"22800"},
            {"value":"12400"},
            {"value":"15800"},
            {"value":"9800"},
            {"value":"21800"},
            {"value":"9310"},
            {"value":"12362"},
            {"value":"17230"},
            {"value":"10202"},
            {"value":"12366"}]
        }
    ]};
});
