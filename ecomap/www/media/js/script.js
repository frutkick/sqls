var app=angular.module('app',['ui.bootstrap'])
app.controller('DatepickerDemoCtrl', function ($scope) {
  $scope.today = function() {
    $scope.dt = new Date();
  };
  $scope.today();

  $scope.clear = function () {
    $scope.dt = null;
  };

  // Disable weekend selection
  $scope.disabled = function(date, mode) {
    return ( mode === 'day' && ( date.getDay() === 0 || date.getDay() === 6 ) );
  };

  $scope.toggleMin = function() {
    $scope.minDate = $scope.minDate ? null : new Date();
  };


  $scope.open = function($event) {
    $scope.status.opened1 = true;
  };
  $scope.open2 = function($event) {
    $scope.status.opened2 = true;
  };
  

  $scope.setDate = function(year, month, day) {
    $scope.dt = new Date(year, month, day);
  };

  $scope.dateOptions = {
    formatYear: 'yy',
    startingDay: 1
  };

  $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
  $scope.format = $scope.formats[0];

  $scope.status = {
    opened: false
  };

  var tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  var afterTomorrow = new Date();
  afterTomorrow.setDate(tomorrow.getDate() + 2);
  $scope.events =
    [
      {
        date: tomorrow,
        status: 'full'
      },
      {
        date: afterTomorrow,
        status: 'partially'
      }
    ];

  $scope.getDayClass = function(date, mode) {
    if (mode === 'day') {
      var dayToCheck = new Date(date).setHours(0,0,0,0);

      for (var i=0;i<$scope.events.length;i++){
        var currentDay = new Date($scope.events[i].date).setHours(0,0,0,0);

        if (dayToCheck === currentDay) {
          return $scope.events[i].status;
        }
      }
    }

    return '';
  };
});
app.controller("UserController", function ($scope, $http){
  this.tab = 1;
  this.setTab = function(tab) {
    this.tab = tab;
  };

  this.isSet = function(tab) {
    return this.tab === tab;
  };

  $scope.register = function() {
    alert($scope.user.email);
    $http.post('/register', $scope.user).success(function(results) {
      alert(results);
    }).error(function(error) {
      alert(error);
    });
  };

  $scope.login = function() {
    alert($scope.user.email);
    $http.post('/login', $scope.user).success(function(results) {
      alert(results);
    }).error(function(error) {
      alert(error);
    });
  }
});
