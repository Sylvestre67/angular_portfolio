/**
 * Created by sylvestre on 11/28/15.
 */
var blogApp = angular.module('blogApp',['ngRoute','ngCookies','postControl','contactFormControl']);

blogApp.config(['$locationProvider',function($locationProvider) {
	$locationProvider.html5Mode({enabled: false}).hashPrefix('');
}]);

blogApp.config(['$sceDelegateProvider',function($sceDelegateProvider) {
  $sceDelegateProvider.resourceUrlWhitelist([
    'self',
    'https://sg-portfolio.s3.amazonaws.com/**'
  ]);

  $sceDelegateProvider.resourceUrlBlacklist([

  ]);
}]);


blogApp.config(['$routeProvider',
    function($routeProvider){
        $routeProvider
            .when('/',{
                templateUrl: 'static/views/about-me.html',
                controller: 'aboutMeCtrl'
            })
            .when('/blogs/',{
                templateUrl: 'static/views/blog-index.html',
                controller: 'blogListCtrl'
            })
            .when('/blogs/:postId',{
                templateUrl:'static/views/blog-post.html',
                controller: 'blogDetailCtrl'
            })
            .when('/portfolio/',{
                templateUrl: 'static/views/pfolio-index.html',
                controller: 'pfolioListCtrl'
            })
            .when('/pfolio/:postId',{
                templateUrl:'static/views/pfolio-post.html',
                controller: 'portfolioDetailCtrl'
            })
            .when('/contact/',{
                templateUrl:'static/views/contact.html',
                controller: 'contactFormController'
            })
            .otherwise({
                redirectTo:'/admin'
        	});
   		}
	]);




