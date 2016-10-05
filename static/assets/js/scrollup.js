/**
 * Created by vitold on 26.04.16.
 */
$( document ).ready(function() {
	$('#scrollup img').mouseover( function(){
		$( this ).animate({opacity: 0.65},400);
	}).mouseout( function(){
		$( this ).animate({opacity: 1},400);
	}).click( function(){
		$('html, body').animate({
                scrollTop:0
            }, 400);
		return false;
	});

	$(window).scroll(function(){
		if ( $(document).scrollTop() > 0 ) {
			$('#scrollup').fadeIn('slow');
		} else {
			$('#scrollup').fadeOut('slow');
		}
	});
});
