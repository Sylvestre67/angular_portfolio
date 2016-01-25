/**
 * Created by sylvestre on 12/1/15.
 */
var formControl = angular.module('contactFormControl', []);

formControl.controller('contactFormController', ['$scope','$http','$cookies',
    function($scope,$http,$cookies){
        $scope.submittedForm = {};
        $scope.csrftoken = $cookies.get('csrftoken');

        $scope.hideContactForm = false;
        $scope.hideAjax = true;
        $scope.hideThankYou = true;

        function showSucessMessage(){
            console.log('POST is sucessfull');
        }

        function showErrorMessage(){
            console.log('POST Invalid');
        }

        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        $http.defaults.headers.post['X-CSRFToken'] = $scope.csrftoken;

        $scope.submittedForm.submitTheForm = function() {
                $scope.hideAjax = false;

                var formData = jQuery.param({
                    'subject' : $scope.submittedForm.subject,
                    'from' : $scope.submittedForm.from,
                    'message': $scope.submittedForm.message,
                    'copy_me': $scope.submittedForm.copy_me,
                    'csrfmiddlewaretoken': $scope.csrftoken
                });

                console.log(formData);

                $http.post('api/contactUsForm/', formData).success(function(data){
                    console.log(data);
                    $scope.hideAjax = true;
                    $scope.hideThankYou = false;
                    $scope.hideContactForm = true;
                });

        };

    }]);

