$(document).ready(function(){

    ua = navigator.userAgent;
    event = "ciao";
    event = (ua.match(/iPad/i) != null) ? "touchend" : "click";
    if (event == "click") {
        event = (ua.match(/iPhone/i) != null) ? "touchend" : "click";
    }

    $('header, footer').on('touchmove', function (e) {
        e.preventDefault();
    });
    
    $('nav ul').on(event, function (e) {
        $(this).toggleClass("open");
    });
    
    function changeStyle(rel) {
	    $("#style").attr("href", "static/css/" + rel + ".css");
    }
    
    $('nav li').on(event, function (e) {
        $("nav .active").removeClass("active");
        $(this).addClass("active");
        $("#content > .list, .details, .form").hide();
        rel = $(this).attr("rel");
        $("." + rel).show();
        changeStyle(id);
    });
    
    $('#content').on(event, function (e) {
        $("nav ul").removeClass("open");
    });
    
    $('footer li').on(event, function (e) {
        $("footer .active").removeClass("active");
        $(this).addClass("active");
    });
    
    $('span.follow').on(event, function (e) {
        $(this).toggleClass("active");
    });
    
    $('.form input').on('focus', function (e) {
    	if(!$(this).hasClass("active"))
    	{
	    	$(this).val("");
	        $(this).addClass("active");
        }
    });
    
    $('.form input').on('blur', function (e) {
    	if($(this).val() == "")
    	{
    		$(this).val($(this).attr('aria-label'));
        	$(this).removeClass("active");
        }
    });
    
    $('.form textarea').on('focus', function (e) {
    	if(!$(this).hasClass("active"))
    	{
	    	$(this).html("");
	        $(this).addClass("active");
        }
    });
    
    $('.form textarea').on('blur', function (e) {
    	if($(this).html() == "")
    	{
    		$(this).html($(this).attr('aria-label'));
        	$(this).removeClass("active");
        }
    });
    
    $('#content > .list > section, .problems .list > section, .solutions .list > section').on(event, function (e) {
    	$("nav .active").removeClass("active");
    	rel = $(this).attr("rel");
        $("#" + rel).addClass("active");
    	$("#content > .list, .details").hide();
        $("." + rel).show();
        changeStyle(rel);
    });
    
    $('#back').on(event, function (e) {
        $(".details, .form").hide();
        $("#content > .list").show();
    });
    
    $('#add').on(event, function (e) {
        $("#content > .list, .details").hide();
        $(".form").show();
    });
});