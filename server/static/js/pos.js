// Main 
var board = $('#board');
var cart = $('#cart');
var cart_sum = $('#cart_sum');

// Modal 
var modalQtyLabel = $('#modalQtyLabel');
var modalNumberBlock = $('#modalNumberBlock');


var qty = 1;



function drawItemsOnBoard(data) {
	board.empty();
	if (data[0]['model'] != 'pos.kategorie') {
		board.append(
			'<div class="col-6 col-md-4 col-lg-2>"' +
			'<a href="/pos/ajax/" onclick="fetchData()">' +
			'<div class="card text-white bg-success h-100">' +
			'<div class="card-body text-center">Züruck</div></div></a></div>'
		);
	}
	for (var i = data.length - 1; i >= 0; i--) {
		board.append(
			'<div class="col-6 col-md-4 col-lg-2 card-btn"> '+
			'<a href="/pos/ajax/' +data[i]['model']+ '/' +data[i]['pk'] + '"' +
			'onclick="fetchData(event)"> ' +
			'<div class="card text-dark bg-warning h-100"><div class="card-body text-center">'+
			 data[i]['fields']['name'] + '</div></a></div>'
		);
	}
}


function fetchData(obj=null) {
	var url_string = '/pos/ajax/';
	if (obj != null) {
		obj.preventDefault();
		url_string = obj.currentTarget.href;
	}
	$.ajax({
		type: 'GET',
		url: url_string,
		success: function(data) {
			if (!url_string.includes('arti')) {
				drawItemsOnBoard(data);
			} else {
				fetchCart();
			}
		},
		error: function(er) {
			console.error(er);
		}
	});
}



function delItemCart(e) {
	e.preventDefault();
	url_string = e.currentTarget.href;
	$.ajax({
		type: 'GET',
		url: url_string,
		success: function() {
			fetchCart();
		}
	});
}



function drawCart(items) {
	cart.empty();
	for (var i = items.length - 1; i >= 0; i--) {
		cart.append('<li class="list-group-item list-group-item-dark">' +
			'<div class="row"><div class="col-8">' +
			items[i].name + '</div><div class="col-2">x' + 
			items[i].qty + '</div><div class="col-2">' +
			'<a href="/pos/ajax/cart/remove/'+items[i].id+
			'" onclick="delItemCart(event)">X</a></div></li>'
			);
	}
}



function fetchCart() {
	$.ajax({
		type: 'GET',
		url: '/pos/ajax/cart/', 
		success: function(data) {
			drawCart(data.items);
			cart_sum.empty();
			cart_sum.append(data.cart_total + '€');
		},
		error: function(er) {
			console.error(er);
		}
	});
}


$(document).ready(function() {
	fetchData();
	fetchCart();
	$('#qtyBtn').click(function() {
		modalQtyLabel.empty();
		modalQtyLabel.append(qty);
		$('#qtyModal').modal('show');
	});
});

function modalNumpadClicked(number) {
	modalQtyLabel.val(number.target.value);
}
