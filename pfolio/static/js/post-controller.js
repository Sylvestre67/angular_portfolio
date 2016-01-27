var postControl = angular.module('postControl', []);

postControl.controller('navigationMenuCtrl',['$scope','$location',
    function($scope,$location) {
        $scope.isActive = function (viewLocation){
            var active = (viewLocation === $location.path());
            return active;
        };
    }]);

postControl.controller('aboutMeCtrl',['$scope',
    function($scope){

    }]);

postControl.controller('blogListCtrl',['$scope','$http',
    function($scope,$http){
        $scope.loading = true;
        $scope.static_url = media_url;
        $http.get('/api/blogPosts/').success(function(data){
            $scope.blog_posts = angular.fromJson(data);

            if ($scope.blog_post.fields.image.length > 0){
                $scope.showImage = true;
             }
        }).finally(function () {
          // Hide loading spinner whether our call succeeded or failed.
          $scope.loading = false;
        });

    }]);

postControl.controller('pfolioListCtrl',['$scope','$http',
    function($scope,$http){
        $scope.loading = true;
        $scope.static_url = media_url;

        $http.get('api/portfolioPosts/').success(function(data){
            $scope.portfolio_posts = angular.fromJson(data);
            $scope.chekIfImage = function (post){
                if (post.fields.image.length > 0) {
                    return true;
                }
            }
        }).finally(function () {
            // Hide loading spinner whether our call succeeded or failed.
            $scope.loading = false;
        });
    }]);

postControl.controller('blogDetailCtrl',['$scope','$routeParams','$http','$sce',
    function($scope,$routeParams,$http,$sce){
        $scope.loading = true;
        $scope.static_url = media_url;

        $scope.postId = $routeParams.postId;
        $http.get('api/blogPosts/' + $scope.postId + '/').success(function(data) {
                $scope.blog_post = angular.fromJson(data)[0];
                if ($scope.blog_post.fields.image.length > 0){
                        $scope.showImage = true;
                }
                $scope.blogPostAsHtml = function(){
                    return $sce.trustAsHtml($scope.blog_post.fields.content);
                }
        }).finally(function () {
            // Hide loading spinner whether our call succeeded or failed.
            $scope.loading = false;
        });
    }]);

postControl.controller('portfolioDetailCtrl',['$scope','$routeParams','$http','$sce',
    function($scope,$routeParams,$http,$sce){
        $scope.loading = true;
        $scope.static_url = media_url;

        $scope.postId = $routeParams.postId;
        $http.get('api/pfolioPosts/' + $scope.postId + '/').success(function(data) {
                $scope.pfolio_post = angular.fromJson(data)[0];
                if ($scope.pfolio_post.fields.image.length > 0){
                        $scope.showImage = true;
                }
                $scope.pfolioPostAsHtml = function(){
                    return $sce.trustAsHtml($scope.pfolio_post.fields.content);
                }
        }).finally(function () {
            // Hide loading spinner whether our call succeeded or failed.
            $scope.loading = false;
        });
    }]);
