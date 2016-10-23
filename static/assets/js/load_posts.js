/**
 * Created by vitold on 28.03.16.
 */
var current_page = 1;
/* function to load posts
* @page: offset for pages
* */
function load_posts(){
    var url = $("#posts").data('url');
    var data ={};
    data.page = current_page;
    $.get(url, data, function(data){
        $("#posts").append(data);
    });
    current_page += 1
}

$(document).ready(function () {
    load_posts();
});

$(window).scroll(function(){
/* scroll listener*/
		if ($(document).height() - $(window).height() <= $(window).scrollTop()) {
            if (!$("#footer").html())
            {
                load_posts();
            }

}});

