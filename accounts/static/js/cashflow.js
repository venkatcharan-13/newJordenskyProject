const endpoint = 'api/cashflowData';
var choosen_month = sessionStorage.getItem("choosen_month") ? sessionStorage.getItem("choosen_month"): "2022-06-30";

$(document).ready(function() {
  if(sessionStorage.getItem("choosen_month")){
    $('#periodSelector').val(sessionStorage.getItem("choosen_month").substring(0, 7));
  }
  else{
    $('#periodSelector').val("Choose Month");
  }
});

$.ajax({
  method: "GET",
  url: endpoint,
  data: {
    selected_date: choosen_month
  },
  success: function (response) {
    console.log("Success Cashflow");
    document.getElementById("current_month").innerHTML = response.current_period;
    document.getElementById("previous_month").innerHTML = response.previous_period;
    fillCashflowTotals(response.response_data.beginning_cash_balance, 'beg_cash_bal', 'Beginning Cash Balance');
    fillCashflowRows(response.response_data.cashflow_from_operating_activities, 'cashflowA');
    fillCashflowTotals(response.response_data.net_cash_a, 'netA', 'Cashflow from Operations');
    fillCashflowRows(response.response_data.cashflow_from_investing_activities, 'cashflowB');
    fillCashflowTotals(response.response_data.net_cash_b, 'netB', 'Cashflow from Investing');
    fillCashflowRows(response.response_data.cashflow_from_financing_activities, 'cashflowC');
    fillCashflowTotals(response.response_data.net_cash_c, 'netC', 'Cashflow from Financing');
    fillCashflowTotals(response.response_data.net_change_abc, 'netABC', 'Net Change in Cash (A)+(B)+(C)');
    fillCashflowTotals(response.response_data.ending_cash_balance, 'endbal', 'Ending Cash Balance');
  },
  error: function (error_data) {
    console.log("Error3");
    console.log(error_data);
  }
})

function changePeriod(params) {
  var year = params.substring(0, 4);
  var month = params.substring(5, 7);
  var choosen_period = params + '-' + new Date(year, month, 0).getDate(); 
  sessionStorage.setItem("choosen_month", choosen_period);
  location.reload();
}

function fillCashflowRows(data, tid) {
  var table = document.getElementById(tid);
  data.forEach(function (object) {
    var codings = '';
    if (object.related_acc_for_codings){
      object.related_acc_for_codings.forEach((coding) => {
        codings += `codings=${coding}&`;
      })
    }
    console.log(codings);
    var tr = document.createElement('tr');
    if (object.activity == "Net Income" || object.activity == "Plus: Depreciation & Amortization"){
      var href = '#';
    }else{
      var href = `${object.activity}/?${codings}selected_date=${choosen_month}`;
    }
    tr.innerHTML = `<th style="width:40%"><a href="${href}" 
    style="text-decoration: none">${object.activity}</a></th>` +
      '<td style="width: 20%; text-align:right;">' + object.current + '</td>' +
      '<td style="width: 20%; text-align:right;">' + object.previous + '</td>' +
      '<td style="width: 20%; text-align:center;">' + object.per_change + '%</td>';
    table.appendChild(tr);
  })
}

function fillCashflowTotals(object, tid, head) {
  document.getElementById(tid).innerHTML = '<th style="width:40%">' + head + '</th>' +
    '<th style="width: 20%; text-align:right;">' + object.current + '</th>' +
    '<th style="width: 20%; text-align:right;">' + object.previous + '</th>' +
    '<th style="width: 20%; text-align:center;">' + object.per_change + '%</th>';
}