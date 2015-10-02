'use strict';

$(function() {
	// Manage navigation tabs
	var $tabulationElements = $('div.search-nav > ul.nav > li');
	var $targetElements = $('#searchContainer form')
    $tabulationElements.bind('click', function(){
    	$tabulationElements.removeClass('active');
    	$targetElements.hide();

    	var targetSelector = $(this).attr('data-target');
    	var $target = $targetElements.filter('#' + targetSelector).show();
    	$(this).addClass('active');
    });



});

// Handle search attempt

/*
 * TODO: VALIDATE
 * TODO: SEND REQUEST
*/
function submitSearch(invoker){
	var location = '';
	var $targetElement = $('#' + $(invoker).attr('data-target'))
	var battleTag = $targetElement.val();
	
	if (isValid(battleTag)){
		// proceed with submitting
		console.log('Will submit');
	} else {
		// Display error and highlight.	
		console.log('Invalid battletag');
	}
}

function isValid(tag){
	/* Validates that string is a valid
	*  Blizzard battle tag.
	*/
	var battleTagPattern = '([A-Za-z])+#([0-9]{4})';
	return !!tag.match(battleTagPattern);
}