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


var typingTimer;                //timer identifier
var doneTypingInterval = 100;  //time in ms need to wait after user stops typing

//user is "finished typing"
function doneTyping (scope) {
  scope.callRestService()
}

app.directive('myOnKeyDownCall', function () {
    return function ($scope, element) {
        element.bind("keyup", function (event) {
          clearTimeout(typingTimer);
  typingTimer = setTimeout(function() { doneTyping($scope) }, doneTypingInterval);
        });

        element.bind("keydown", function (event) {
          clearTimeout(typingTimer);
        });
    };
});