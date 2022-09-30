$('#two').waypoint(function () {

   $(".container ul li").children().removeClass("active");
   $("#sec-2").addClass("active");

}, { offset: 101 });


$('#three').waypoint(function () {
   $(".container ul li").children().removeClass("active");
   $("#sec-3").addClass("active");
}, { offset: 101 });


$('#one').waypoint(function () {
   $(".container ul li").children().removeClass("active");
   $("#sec-1").addClass("active");
}, { offset: 0 });

$('#four').waypoint(function () {
   $(".container ul li").children().removeClass("active");
   $("#sec-4").addClass("active");
}, { offset: 0 });

