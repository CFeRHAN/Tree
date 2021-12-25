// var symbol = "";

// $(document).ready(function() {
//   var query;
//   var foundId;
//    $('#search-submit').click(function(e){
//        e.preventDefault();
//        query = $("#search-box").val();
//        if (query.length > 0) {
//          foundId = $('section:contains('+query+')').attr('id');
//          $("#info_display").load('info.html #' + foundId);
//        }
//        else {
//          alert("Oops, you forgot to enter a search term.");
//        }
//    });
// });

// $("#search-submit").bind('keyup mouseup', function () {
//   var search = $("#search-box").val();
//   $("#info-display").text(search);

// });

$(document).ready(function () {
  $('.buy').removeClass('selected');
  $('.buy').addClass('buyHover');
  $('.transfer').removeClass('action-botton , actionsell')
  $('.transfer').addClass('actionbuy')
  $('.transfer').text("BUY")
})


$('.isolatedClass').on('click', function () {
  $('.isolatedClass').removeClass('selected');
  $(this).addClass('isolatedCrossHover');
  $('.crossClass,crossNumber').removeClass('isolatedCrossHover');
  $('.crossClass').addClass('crossClass')
  $('.crossNumber').addClass('crossNumber')

});

$('.crossClass').on('click', function () {
  $('.crossClass').removeClass('selected');
  $(this).addClass('isolatedCrossHover');
  $('.isolatedClass,.crossNumber').removeClass('isolatedCrossHover');
  $('.isolatedClass').addClass('isolatedClass')
  $('.crossNumber').addClass('crossNumber')

  alert("Are you sure?")
});

// $('.submitBtn').on('click', function(){
//   $('.submitBtn').removeClass('selected');
//     $(this).addClass('submitBtnHover');
// });

// $( "body" ).click(function( event ) {
//   event.preventDefault('.submitBtn');

// });


$("#dialog").dialog({
  modal: true,
  autoOpen: false
});
$("#opener").click(function () {
  $("#dialog").dialog("open");

  return false;
});


// $(":input").bind('keyup mouseup', function () {
//   var coins = $("#amountInput").val();
//   $("#opener").text(coins);
// });

$(".submitBtn").click(function (e) {
  e.preventDefault();
  $("#dialog").dialog("close");
  $(":input").bind('keyup mouseup', function () {
    var coins = $("#amountInput").val() + 'x';
    $("#opener").text(coins);
  });
  return false;
});




$('.crossNumber').on('click', function () {
  $('.crossNumber').removeClass('selected');
  $(this).addClass('crossNumberHover');
  $('.isolatedClass,.crossClass').removeClass('isolatedCrossHover');
  $('.isolatedClass').addClass('isolatedClass')
  $('.crossClass').addClass('crossClass')
});




$('.buy').on('click', function () {
  $('.buy').removeClass('selected');
  $(this).addClass('buyHover');
  $('.sell').removeClass('sellHover');
  $('.sell').addClass('bottons')
  $('.transfer').removeClass('action-botton , actionsell')
  $('.transfer').addClass('actionbuy')
  $('.transfer').text("BUY")
});

$('.sell').on('click', function () {
  $('.sell').removeClass('selected');
  $(this).addClass('sellHover');
  $('.buy').removeClass('buyHover');
  $('.buy').addClass('bottons')
  $('.transfer').removeClass('action-botton , actionbuy')
  $('.transfer').addClass('actionsell')
  $('.transfer').text("SELL")
});

$('.limit').on('click', function () {
  $('.limit').removeClass('selected');
  $(this).addClass('marketLimitHover');
  $('.market, .stop-limit').removeClass('marketLimitHover');
  $('.market, .stop-limit').addClass('market-limit')
});

$('.market').on('click', function () {
  $('.market').removeClass('selected');
  $(this).addClass('marketLimitHover');
  $('.limit, .stop-limit').removeClass('marketLimitHover');
  $('.limit, .stop-limit').addClass('market-limit')
});

$('.stop-limit').on('click', function () {
  $('.stop-limit').removeClass('selected');
  $(this).addClass('marketLimitHover');
  $('.limit, .market').removeClass('marketLimitHover');
  $('.limit, .market').addClass('market-limit')
});

$("#marketClick").on('click',function(){
  
  $(".priceAmount").removeClass('amount-input')
  $(".priceAmount").addClass('hidden')
});
$(".stop-limit , #limitClick").on('click',function(){
  $(".priceAmount").removeClass('hidden')
  $(".priceAmount").addClass('amount-input')
})


$(function () {
  $("#speed").selectmenu();

  $("#files").selectmenu();

  $("#number")
    .selectmenu()
    .selectmenu("menuWidget")
    .addClass("overflow");

  $("#salutation").selectmenu();
});


$('document').ready(function () {
  $('#takeProfit, #stopLoss').attr('disabled', 'disabled');
});

$(function () {
  $('#TPSL').change(function () {
    if ($(this).is(':checked')) {
      $('#takeProfit, #stopLoss').removeAttr('disabled')
    } else {
      $('#takeProfit, #stopLoss').attr('disabled', 'disabled');
    }
  });
});

$(function () {
  if ($('.market').click()) {
    $('#price').attr('disabled', 'disabled');


  } else {
    $('#price').removeAttr('disabled')
  }
});

$(function () {
  if ($('.limit').click()) {
    $('#price').removeAttr('disabled')

  } else {
    $('#price').attr('disabled', 'disabled');
  }
});


function validate(evt) {
  var theEvent = evt || window.event;

  // Handle paste
  if (theEvent.type === 'paste') {
    key = event.clipboardData.getData('text/plain');
  } else {
    // Handle key press
    var key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode(key);
  }
  var regex = /[0-9]|\./;
  if (!regex.test(key)) {
    theEvent.returnValue = false;
    if (theEvent.preventDefault) theEvent.preventDefault();
  }
}
document.querySelector("#volume").addEventListener("change", function (e) {
  document.querySelector(".volume").textContent = e.currentTarget.value + '%';
})


$(function () {
  $("#tabs").tabs();
});


var order = {
  side: "",
  type: "",
  symbol: "",
  price: 0,
  amount: 0,
  TPSL: false,
  takeProfit: 0,
  stopLoss: 0
};

$(".transfer").click(function () {
    if ($('.market').hasClass('marketLimitHover')) {

        if ($(this).hasClass('actionbuy')) {
            orderSide = 'buy'
        } else if ($('.transfer').hasClass('actionsell')) {
            orderSide = 'sell'
        }

        orderTPSL = !!$('#TPSL').is(':checked');
        orderObj = createMarketOrderObj('BTC-USDT',
                                        orderSide,
                                        $('#amount').val(),
                                        orderTPSL,
                                        $('#takeProfit').val(),
                                        $('#stopLoss').val());

        createMarketOrder('BTC-USDT', orderObj)
        console.log(orderObj)
    }
});


// new jquery  code
$(document).ready(function () {

  // FETCHING DATA FROM JSON FILE
  $.getJSON("test.json",
    function (data) {
      var pos = '';

      // ITERATING THROUGH OBJECTS
      $.each(data, function (key, value) {

        //CONSTRUCTION OF ROWS HAVING
        // DATA FROM JSON OBJECT
        pos += '<tr>';
        pos += '<td>' +
          value.symbol + '</td>';

        pos += '<td>' +
          value.brackets[0].bracket + '</td>';

        pos += '<td>' +
          value.brackets[0].initialLeverage + '</td>';

        pos += '<td>' +
          value.brackets[0].notionalCap + '</td>';

        pos += '</tr>';


      });

      //INSERTING ROWS INTO TABLE 
      $('.positionSubHeader').append(pos);
    });
});


function createMarketOrderObj(symbol, side, amount, TPSL = false, takeProfit = none, stopLoss = none) {
    const obj = {};
    obj.symbol = symbol;
    obj.side = side;
    obj.type = "MARKET";
    obj.amount = amount;
    obj.TPSL = TPSL;
    if (TPSL) {
        obj.takeProfit = takeProfit;
        obj.stopLoss = stopLoss;
    }

    return obj;
}


function createLimitOrderObj(symbol, side, amount, price, TPSL = false, takeProfit = none, stopLoss = none) {
    const obj = {};
    obj.symbol = symbol;
    obj.side = side;
    obj.type = "LIMIT";
    obj.amount = amount;
    obj.price = price;
    obj.TPSL = TPSL;
    obj.takeProfit = takeProfit;
    obj.stopLoss = stopLoss;
    return obj;
}

function getOpenPositions(symbol = "BTCUSDT") {
    $.ajax({
        type: 'GET',
        url: '/market/openPositions/' + symbol,
        contentType: 'application/json; charset=utf-8',
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        }
    })
};

function getOpenOrders(symbol = "BTCUSDT") {
    $.ajax({
        type: 'GET',
        url: '/market/openOrders/' + symbol,
        contentType: 'application/json; charset=utf-8',
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        }
    })
};

function cancelAllOrders(symbol = "BTCUSDT") {
    $.ajax({
        type: 'GET',
        url: '/market/cancelAllOrders/' + symbol,
        contentType: 'application/json; charset=utf-8',
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        }
    })
};

function cancelOrder(symbol = "BTCUSDT") {
    $.ajax({
        type: 'GET',
        url: '/market/cancelOrder/' + symbol + "/" + orderId,
        contentType: 'application/json; charset=utf-8',
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        }
    })
};

function closePosition(symbol = "BTCUSDT") {
    $.ajax({
        type: 'GET',
        url: '/market/marketOpenPosition/' + symbol,
        contentType: 'application/json; charset=utf-8',
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        }
    })
};

function createMarketOrder(symbol = "BTCUSDT", order) {
    $.ajax({
        type: 'POST',
        url: '/market/createMarketOrder/' + symbol,
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(order),
        success: function (response) {
            // console.log(response)
            positions = response
            console.log("_____________________________________")
            console.log(positions)
        },
        error: function (error) {
            console.log(error)
        }
    })
};

function createLimitOrder(symbol = "BTCUSDT", order) {
    $.ajax({
        type: 'POST',
        url: '/market/createLimitOrder/' + symbol,
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(order),
        success: function (response) {
            // console.log(response)
            positions = response
            console.log("_____________________________________")
            console.log(positions)
        },
        error: function (error) {
            console.log(error)
        }
    })
};
