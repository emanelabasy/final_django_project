var email;
var emailer;

$(function() {
	email = $('#email');
	emailer = $('#emailer');
	// echo email;
	email.on('blur', function(event) {
		event.preventDefault();
		var user={};
		$.ajax({
			url: 'validate.php?email='+$(this).val(),
			type: 'POST',
			data: user,
			success: function (response) {
				 if(response==1)
				 {
				 	  emailer.html("invaild");
				 }
				 else
				 {
				 	emailer.html("avalibal");
				 }
			
			},
			error: function (error) {
				 console.log(error);
			}
		});
	});
});