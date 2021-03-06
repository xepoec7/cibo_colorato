// Main 
var selectedQty = $('#selectedQty');
var board = $('#board');
var cart = $('#cart');
var cart_sum = $('#cart_sum');
var cartFooter = $('#cartFooter');

// Modal 
var modalQtyLabel = $('#modalQtyLabel');
var modalNumberBlock = $('#modalNumberBlock');


var qty = 1;
var temp_qty = null;



function drawItemsOnBoard(data) {
	board.empty();
	if (data[0]['model'] != 'pos.kategorie') {
		board.append(
			'<div class="col-6 col-sm-4 col-md-3 col-lg-2>"' +
			'<a href="/pos/ajax/" onclick="fetchData()">' +
			'<div class="card text-white bg-success h-100">' +
			'<div class="card-body text-center">Züruck</div></div></a></div>'
		);
	}
	for (var i = data.length - 1; i >= 0; i--) {
		board.append(
			'<div class="col-6 col-sm-4 col-md-3 col-lg-2 card-btn"> '+
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
		if (url_string.includes('arti') && qty > 1) url_string = url_string + '/' + qty ;
	}
	$.ajax({
		type: 'GET',
		url: url_string,
		success: function(data) {
			if (!url_string.includes('arti')) {
				drawItemsOnBoard(data);
			} else {
				fetchData();
				fetchCart();
				qty = 1;
				temp_qty = null;
				selectedQty.hide();
				modalQtyLabel.empty();
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
			if (data.items.length == 0) {
				cartFooter.hide();
			} else {
				cartFooter.show();
			}
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
		$('#qtyModal').modal('show');
	});
});



// Modal



function modalNumpadClicked(number) {
	if (number.target.value == 'C') {
		var qtyStr = temp_qty.toString();
		if (qtyStr.length > 1) {
			qtyStr = qtyStr.substring(0, qtyStr.length -1);

		} else {
			qtyStr = "0" ;
		}
		temp_qty = parseInt(qtyStr);
	}
	else {
		if (temp_qty == null) temp_qty = parseInt(number.target.value);
		else {
			temp_qty = (temp_qty * 10) + parseInt(number.target.value);
		}
	}
	modalQtyLabel.text(temp_qty);
}

function modalOkBtnClicked() {
	if (temp_qty == 0) qty = 1;
	else qty = temp_qty;
	$('#qtyModal').modal('hide');
	selectedQty.text("X"+qty);
	selectedQty.show();
}