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

  it('Should initialize the scope', function () {
    expect(scope.error).to.be.null;
    expect(scope.url).to.be.null;
    exepct(scope.generated).to.be.false;
    exepct(scope.url_copied).to.be.false;
  });
  
});