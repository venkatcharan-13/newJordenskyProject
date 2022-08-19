const endpoint = 'api/balsheetData';
var choosen_month = sessionStorage.getItem("choosen_month") ? sessionStorage.getItem("choosen_month") : "2022-06-30";

$(document).ready(function() {
    if (sessionStorage.getItem("choosen_month")) {
        $('#periodSelector').val(sessionStorage.getItem("choosen_month").substring(0, 7));
    } else {
        $('#periodSelector').val("Choose Month");
    }
});

$.ajax({
    method: "GET",
    url: endpoint,
    data: {
        selected_date: choosen_month
    },
    success: function(response) {
        console.log("Success Balance Sheet");
        document.getElementById("current_month_date").innerHTML = response.current_period;
        document.getElementById("previous_month_date").innerHTML = response.previous_period;

        fillBalsheetRows(response.response_data.cash, 'cash');
        fillBalsheetRows(response.response_data.bank, 'bank');
        fillBalsheetRows(response.response_data.accounts_receivable, 'acc_rec');
        fillBalsheetRows(response.response_data.fixed_asset, 'fixasset');
        fillBalsheetRows(response.response_data.other_current_asset, 'ocasset');
        fillBalsheetRows(response.response_data.other_asset, 'othasset');
        fillBalsheetRows(response.response_data.stock, 'stock');
        fillBalsheetRows(response.response_data.accounts_payable, 'acc_pay');
        fillBalsheetRows(response.response_data.long_term_liability, 'ltliab');
        fillBalsheetRows(response.response_data.other_current_liability, 'ocliab');
        fillBalsheetRows(response.response_data.other_liability, 'othliab');
        fillBalsheetRows(response.response_data.equity, 'equity');
        document.getElementById('head_equity').innerHTML = response.response_data.total_equity;
        document.getElementById('head_liabilities').innerHTML = response.response_data.total_liabilities;
        document.getElementById('head_assets').innerHTML = response.response_data.total_assets;
    },
    error: function(error_data) {
        console.log("Error2");
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


function fillBalsheetRows(data, tid) {
    var table = document.getElementById(tid);
    data.forEach(function(object) {
        var tr = document.createElement('tr');
        tr.innerHTML = '<th style="width:40%">' + object.account_header + '</th>' +
            '<td style="width: 20%; text-align:right;">' + object.current + '</td>' +
            '<td style="width: 20%; text-align:right;">' + object.previous + '</td>' +
            '<td style="width: 20%; text-align:center;">' + object.per_change + '%</td>';
        table.appendChild(tr);
    })
}