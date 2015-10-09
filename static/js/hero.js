'use strict';

$(function() {

	var $heroes = $('.hero');

	$heroes.bind('click', function(){
		location.href += $(this).attr('data-hero-id');
	})
});