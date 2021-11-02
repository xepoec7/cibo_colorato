// Menu Navigation 
$('.nav-link').click(function(event) {
	event.preventDefault();
	$('.active').removeClass('active');
	$(this).addClass('active');
	var uri = event.target.href;
	
	$.ajax({
		url: uri, 
		type: 'GET',
		success: function(data) {
			drawMenuList(data);
		},
		error: function(e) {
			console.error(e);
		}
	})
});


function drawMenuList(data) {
	$('#menuList').empty();
	
	for (var i=0; i<data.length; i++) {
		if (data[i]['fields']['zutaten'] == null) data[i]['fields']['zutaten'] = "";
		$('#menuList').append(
			'<div class="col-12 col-sm-12 col-md-12 col-lg-6">' +
			'<div class="card"><div class="row g-0"><div class="col-8">' +
			'<div class="card-body"><h5 class="card-title">' +data[i]['fields']['name']+ '</h5>' +
			'<p class="card-text">' + data[i]['fields']['zutaten'] + '</p></div></div>' +
			'<div class="col-4"><div class="card-body float-end">' +
			'<p class="card-price">' + data[i]['fields']['preis'] + '€</p>' +
			'</div></div></div></div></div>'
		);
	}
}


// Initialize and add the map
function initMap() {
  // The location of Uluru
  const uluru = { lat: -25.344, lng: 131.036 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: uluru,
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}
