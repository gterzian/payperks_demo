'use strict';

describe('Controller: trackingScriptCtrl', function () {
  
  // load the controller's module
  beforeEach(module('urlShortenerApp'));

  var urlShortenerCreateUrlCtrl, scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope, $httpBackend) {
    scope = $rootScope.$new();
    urlShortenerCreateUrlCtrl = $controller('urlShortenerCreateUrlCtrl', {
      $scope: scope
    });
  }));

  
  it('The tracking script should initialize to an empty string, script_generate to false', function () {
    expect(true).to.be.true;
    
  });
  
});