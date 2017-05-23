$(document).ready(function() {
    $("#tickle-start").click(function() {
	$.ajax({
	    type: "GET",
	    url:"/tickle_start/",
	    data: "start",
	    success: function(){
	      console.log("tickler tickling");
	     },
	    error: function(){
		alert("Łaskotnik nie jest dostępny!");
		}
	    });
	})

    $("#tickle-fast").click(function() {
	$.ajax({
	    type: "GET",
	    url:"/tickle_fast/",
	    data: {
	    'mock': 'fast'
	    },
	    success: function(){
	      console.log("tickler tickling");
	     },
	    error: function(){
		alert("Łaskotnik nie jest dostępny!");
		}
	    });
	})

    $("#tickle-medium").click(function() {
	$.ajax({
	    type: "GET",
	    url:"/tickle_normal/",
	    data: {
	    'speed': 'medium'
	    },
	    success: function(){
	      console.log("tickler tickling");
	     },
	    error: function(){
		alert("Łaskotnik nie jest dostępny!");
		}
	    });
	})

    $("#tickle-slow").click(function() {
	$.ajax({
	    type: "GET",
	    url:"/tickle_slow/",
	    data: {
	    'speed': 'slow'
	    },
	    success: function(){
	      console.log("tickler tickling");
	     },
	    error: function(){
		alert("Łaskotnik nie jest dostępny!");
		}
	    });
	})
});
