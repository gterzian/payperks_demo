var urlShortenerApp = angular.module('urlShortenerApp', ['ngClipboard']).config(function ($interpolateProvider, $httpProvider, ngClipProvider){
  $interpolateProvider.startSymbol('{[').endSymbol(']}');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

urlShortenerApp.controller('urlShortenerCreateUrlCtrl', ['$scope', '$rootScope', '$http', function ($scope, $rootScope, $http) {
  
  $scope.resetUrl = function () {
    $scope.url = null;
    $scope.error = null;
    $scope.generated = false;
    $scope.url_copied = false;
  };
  
  //init the scope
  $scope.resetUrl();
  
  $scope.showCopySuccessMessage = function () {
    $scope.url_copied = true;
  };
  
  $scope.generateShortUrl = function () {
    if ($scope.url == null) {
      $scope.error = 'Please input an url'
      return false;
    }
    if (!(_.includes($scope.url, 'http://') || _.includes($scope.url, 'https://'))) {
      $scope.error = 'Please input a valid url starting with http:// or https://'
      return false;
    }
    
    if (_.endsWith($scope.url, '/')) {
     
    $http.post('/api/short_urls', {original:$scope.url, shortened:''}).
      success(function(data, status, headers, config) {
        // this callback will be called asynchronously
        // when the response is available
        console.log(data)
      }).
      error(function(data, status, headers, config) {
        console.log(data)
        // called asynchronously if an error occurs
        // or server returns response with an error status.
      });  
      $scope.generated = true;
      $scope.error = null;
    }
    
 
  };
    
}]);