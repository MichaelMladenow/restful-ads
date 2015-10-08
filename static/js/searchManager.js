'use strict';

$(function() {
	// Manage navigation tabs
	var $tabulationElements = $('div.search-nav > ul.nav > li');
	var $targetElements = $('#searchContainer form')
	$tabulationElements.bind('click', function() {
		$tabulationElements.removeClass('active');
		$targetElements.hide();

		var targetSelector = $(this).attr('data-target');
		var $target = $targetElements.filter('#' + targetSelector).show();
		$(this).addClass('active');
	});

	// Validate tag in the search form
	$('#battleTag').bind('change keydown paste input', function() {
		var tag = $(this).val();
		if (isValid(tag)) {
			$(this)
				.addClass('valid-tag')
				.removeClass('invalid-tag')
				.notify("This does look like a valid tag.", 'success', {
					position: "top left"
				});
		} else {
			$(this)
				.addClass('invalid-tag')
				.removeClass('valid-tag')
				.notify("This battle tag does not match the Tag#ID pattern. E.g. Steve#1234.", 'warn', {
					position: "top left"
				});;
		}
	})

	// Clear syntax highlighting on cursor out
	$('#battleTag').bind('focusout', function() {
		var tag = $(this).val();
		$(this)
		.removeClass('invalid-tag')
		.removeClass('valid-tag');
	})


	// Handle submit/search player
	$('#searchPlayer').submit(function() {
		location.href = 'player/' + $(this).find('#battleTag').val().replace('#', '-');
		return false; // Prevent original form submit
	});

});

function isValid(tag) {
	/* Validates that string is a valid
	 * Blizzard battle tag.
	 * Params:
	 *		tag - string
	 * Return type: bool
	 */
	var battleTagPattern = '([A-Za-z])+#([0-9]{4})';
	return !!tag.match(battleTagPattern);
}
