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
    
    $('nav li').on(event, function (e) {
        $("nav .active").removeClass("active");
        $(this).addClass("active");
    });
    
    $('#content').on(event, function (e) {
        $("nav ul").removeClass("open");
    });
    
    $('footer li').on(event, function (e) {
        $("footer .active").removeClass("active");
        $(this).addClass("active");
    });
    
    $('.list section span.icon').on(event, function (e) {
        $(this).toggleClass("follow");
    });
});