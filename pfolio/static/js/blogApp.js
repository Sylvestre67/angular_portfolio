/**
 * Created by sylvestre on 11/28/15.
 */
var blogApp = angular.module('blogApp',['ngRoute','ngCookies','postControl','contactFormControl']);

blogApp.config(['$locationProvider',function($locationProvider) {
	$locationProvider.html5Mode(true).hashPrefix('!');

}]);

blogApp.config(['$sceDelegateProvider',function($sceDelegateProvider) {
  $sceDelegateProvider.resourceUrlWhitelist([
    'self',
    'https://sg-pfolio.s3.amazonaws.com/**'
  ]);

  $sceDelegateProvider.resourceUrlBlacklist([

  ]);
}]);


blogApp.config(['$routeProvider',
    function($routeProvider){
        $routeProvider
            .when('/',{
                templateUrl: s_url + 'views/about-me.html',
                controller: 'aboutMeCtrl'
            })
            .when('/blogs/',{
                templateUrl: s_url + 'views/blog-index.html',
                controller: 'blogListCtrl'
            })
            .when('/blogs/:postId',{
                templateUrl: s_url + 'views/blog-post.html',
                controller: 'blogDetailCtrl'
            })
            .when('/portfolio/',{
                templateUrl: s_url + 'views/pfolio-index.html',
                controller: 'pfolioListCtrl'
            })
            .when('/pfolio/:postId',{
                templateUrl: s_url + 'views/pfolio-post.html',
                controller: 'portfolioDetailCtrl'
            })
            .when('/contact/',{
                templateUrl: s_url + 'views/contact.html',
                controller: 'contactFormController'
            })
			.when('/error404/',{
                templateUrl: s_url + 'views/error_404.html',
                controller: 'error404Ctrl'
            })
			.when('/admin/',{
                templateUrl: s_url + 'views/error_404.html',
                controller: 'adminAccess'
            })
            .otherwise({
                redirectTo:'/error404'
        	});
   		}
	]);




