var app = angular.module('myApp', []);

app.controller('myCtrl', function($http, $scope) {
   $scope.callRestService= function() {
   value = $("#searchbox").val()
  $http({method: 'GET', url: '/filter', params : {"searchstr":value}}).
    then(function(response) {
         $scope.records = response.data  //retrieve results and add to existing results
    })
}
    $scope.callRestService()
});


app.directive('myOnKeyDownCall', function () {
    return function ($scope, element) {
        element.bind("keyup", function (event) {
          var val = element.val();
          $scope.callRestService();
        });
    };
});