$(function(){												


    $('p').emoticonize();

	$('body').on('click','input[value="reply"]',function(event){
		$(this).parent('p').nextAll('form:first').children(":first").append('<tr><td><input type="text" class="form-control" name="reply"/></td></tr><tr><td><input type="submit" class="btn btn-primary" value="submit"/></tr></td>');
	});

    $('input[name="title"]').on('blur',function(event){
    	// body...
    	if($(this).val()=="")
    	{
    		$(this).focus();
    		$(this).css('border-color', 'red');
    	} 
    });

    $('textarea[name="content"]').on('blur',function(event){
    	// body...
    	if($(this).val()=="")
    	{
    		$(this).focus();
    		$(this).css('border-color', 'red');
    	}
    });

    $('input[type="submit"]').on('click',function(event){
    	// body...
    	if($(this).val()=="")
    	{
    		$(this).focus();
    		$(this).css('border-color', 'red');
    	} 
    	if($(this).val()=="")
    	{
    		$(this).focus();
    		$(this).css('border-color', 'red');
    	}
    });


    $('body').on('click','a:contains("like")',function(event){
    	// body...
    	//comment id
    	
    	var comment_id = $(this).next("span").text();
    	// user id
    	var user_id = $(this).next("span").next("span").text();

    	$.ajax({
		url: 'http://127.0.0.1:8006/user_action/like/?like=yes&comment_id='+comment_id+'&user_id='+user_id+'',
		type: 'get',
		dataType: 'json'
		})
		.done(function() {
			console.log("success");
		})
		.fail(function() {
			console.log("error");
		})
    	$(this).text("dislike");
    });


    $('body').on('click','a:contains("dislike")',function(event){
    	// body...
    	//comment id
    	var comment_id = $(this).next("span").text();
    	// user id
    	var user_id = $(this).next("span").next("span").text();

    	$.ajax({
		url: 'http://127.0.0.1:8006/user_action/like/?comment_id='+comment_id+'&user_id='+user_id+'',
		type: 'get',
		dataType: 'json'
		})
		.done(function() {
			console.log("success");
		})
		.fail(function() {
			console.log("error");
		})
    	$(this).text("like");
    });


     $('body').on('click','input[type="checkbox"]',function(event){
        var article_id = $(this).val();
        var user_id = $(this).next('span').text()
        alert(article_id);
     	if($(this).is(':checked'))
     	{
     		$.ajax({
			url: 'http://127.0.0.1:8006/user_action/mark/?mark=yes&article_id='+article_id+'&user_id='+user_id+'',
			type: 'get',
			dataType: 'json'
			})
			.done(function() {
				console.log("success");
			})
			.fail(function() {
				console.log("error");
			})
     	}
     	else
     	{
     		$.ajax({
			url: 'http://127.0.0.1:8006/user_action/mark/?article_id='+article_id+'&user_id='+user_id+'',
			type: 'get',
			dataType: 'json'
			})
			.done(function() {
				console.log("success");
			})
			.fail(function() {
				console.log("error");
			})
     	}

     	
     });





})



