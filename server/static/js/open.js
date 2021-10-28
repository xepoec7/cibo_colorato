// Menu Navigation 
$('.nav-link').click(function(event) {
	event.preventDefault();
	var uri = event.target.href;
	
	$.ajax({
		url: uri, 
		type: 'GET',
		success: function(data) {
			console.log(data);
		},
		error: function(e) {
			console.error(e);
		}
	})
});