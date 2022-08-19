const endpoint = 'api/pnlData/';
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
        console.log("Success PNL");
        document.getElementById('current_month').innerHTML = response.current_period;
        document.getElementById('previous_month').innerHTML = response.previous_period;
        fillPnlTableIncome(response.response_data.income.data, 'income');
        fillPnlTableCogs(response.response_data.cost_of_goods_sold, 'cogs', 'Costs of Goods Sold');
        fillPnlTableExpenses(response.response_data.expense, 'expense');
        fillPnlTableTotals(response.response_data.income, 'income_total', 'Income');
        fillPnlTableExpenseTotals(response.response_data.total_expense, 'expense_total', 'Expenses');
        fillPnlTableGrossProfit(response.response_data.gross_profit, 'grossprofit', 'Gross Profit');
        fillPnlTableIndividuals(response.response_data.ebitda, 'ebitda', 'EBITDA');
        fillPnlTableIndividuals(response.response_data.depreciation_expenses, 'dep_exp', 'Depreciation Expenses');
        fillPnlTableIndividuals(response.response_data.pbit, 'pbit', 'PBIT');
        fillPnlTableIndividuals(response.response_data.interest_expenses, 'int_exp', 'Interest Expenses');
        fillPnlTableIndividuals(response.response_data.pbt, 'pbt', 'PBT');
        //document.getElementById('head_sales').innerHTML = response.response_data.total_income.current;
        document.getElementById('head_grossprofit').innerHTML = response.response_data.gross_profit.current;
        document.getElementById('head_cogs').innerHTML = response.response_data.cost_of_goods_sold.current ? response.response_data.cost_of_goods_sold.current : 0;
        document.getElementById('head_exp').innerHTML = response.response_data.total_expense.current;
        document.getElementById('head_profit').innerHTML = response.response_data.pbt.current;
    },
    error: function(error_data) {
        console.log("Error1");
        console.log(error_data);
    }
})

function changePeriod(params) {
    console.log(params);
    var year = params.substring(0, 4);
    var month = params.substring(5, 7);
    var choosen_period = params + '-' + new Date(year, month, 0).getDate();
    sessionStorage.setItem("choosen_month", choosen_period);
    location.reload();
}

function checkStatus(percentageChagne, typeOfAccount) {
    tempRow = ''
    if (typeOfAccount == 'expenses') {
        if (percentageChagne < 0 || percentageChagne == '<-100') {
            tempRow = '<td style="widht:8%;text-align:center"><ion-icon name="caret-up-circle-outline" style="color:green"></ion-icon></td>'
        } else {
            tempRow = '<td style="widht:8%;text-align:center"><ion-icon name="caret-down-circle-outline" style="color:red"></ion-icon></td>'
        }
    } else {
        if (percentageChagne > 0 || percentageChagne == '>100') {
            tempRow = '<td style="widht:8%;text-align:center"><ion-icon name="caret-up-circle-outline" style="color:green"></ion-icon></td>'
        } else {
            tempRow = '<td style="widht:8%;text-align:center"><ion-icon name="caret-down-circle-outline" style="color:red"></ion-icon></td>'
        }
    }
    return tempRow
}

function fillPnlTableTotals(object, tid, head) {
    document.getElementById(tid).innerHTML = '<th style="width:35%">' + head + '</th>' +
        '<th style="width: 12%; text-align:right;">' + object.current + '</th>' +
        '<th style="width: 8%;text-align: center;">' + '' + '</th>' +
        '<th style="width: 12%; text-align:right;">' + object.previous + '</th>' +
        '<th style="width: 8%; text-align: center;">' + '' + '</th>' +
        '<th style="width: 8%; text-align: center;"data-f-bold="true" data-b-a-s="thin">' + '' + '</th>' +
        '<th style="width: 12%; text-align:center;">' + object.per_change + '%</th>' +
        '<th style="width: 15%; text-align:right;">' + object.three_month_avg + '</th>';
}

function fillPnlTableExpenseTotals(object, tid, head) {
    document.getElementById(tid).innerHTML = '<th style="width:35%">' + head + '</th>' +
        '<th style="width: 12%; text-align:right;">' + object.current + '</th>' +
        '<th style="width: 8%;text-align: center;">' + object.curr_per + '%</th>' +
        '<th style="width: 12%; text-align:right;">' + object.previous + '</th>' +
        '<th style="width: 8%; text-align: center;">' + object.prev_per + '%</th>' +
        '<th style="width: 8%; text-align: center;"data-f-bold="true" data-b-a-s="thin">' + '' + '</th>' +
        '<th style="width: 12%; text-align:center;">' + object.per_change + '%</th>' +
        '<th style="width: 15%; text-align:right;">' + object.three_month_avg + '</th>';
}

function fillPnlTableIncome(data, tid) {
    var table = document.getElementById(tid);
    data.forEach(function(object) {
        var tr = document.createElement('tr');
        tr.innerHTML = firstRow +
            '<td style="width: 12%; text-align:right;" data-b-a-s="thin">' + object.current + '</td>' +
            '<td style="width: 8%; text-align:right;" data-b-a-s="thin">' + '' + '</td>' +
            '<td style="width: 12%; text-align:right;" data-b-a-s="thin">' + object.previous + '</td>' +
            '<td style="width: 11%; text-align:center;" data-b-a-s="thin">' + '' + '</td>' + checkStatus(object.per_change, 'income') +
            '<td style="width: 12%; text-align:right;" data-b-a-s="thin">' + object.per_change + '</td>' +
            '<td style="width: 15%; text-align:right;" data-b-a-s="thin">' + object.three_month_avg + '</td>';
        table.appendChild(tr);
    })
}

function fillPnlTableCogs(object, tid, head) {
    document.getElementById(tid).innerHTML = '<th style="width:35%">' + head + '</th>' +
        '<td style="width: 12%; text-align:right;">' + object.current + '</td>' +
        '<td style="width: 8%;text-align: center;">' + '' + '</td>' +
        '<td style="width: 12%; text-align:right;">' + object.previous + '</td>' +
        '<td style="width: 8%; text-align: center;">' + '' + '</td>' +
        '<th style="width: 8%; text-align: center;"data-f-bold="true" data-b-a-s="thin">' + '' + '</th>' +
        '<td style="width: 12%; text-align:center;">' + object.per_change + '%</td>' +
        '<td style="width: 15%; text-align:right;">' + object.three_month_avg + '</td>';
}

function fillPnlTableGrossProfit(object, tid, head) {
    document.getElementById(tid).innerHTML = '<th style="width:35%">' + head + '</th>' +
        '<th style="width: 12%; text-align:right;">' + object.current + '</th>' +
        '<th style="width: 8%;text-align: center;">' + object.curr_per + '%</th>' +
        '<th style="width: 12%; text-align:right;">' + object.previous + '</th>' +
        '<th style="width: 8%; text-align: center;">' + object.prev_per + '%</th>' +
        '<th style="width: 8%; text-align: center;"data-f-bold="true" data-b-a-s="thin">' + '' + '</th>' +
        '<th style="width: 12%; text-align:center;">' + object.per_change + '%</th>' +
        '<th style="width: 15%; text-align:right;">' + object.three_month_avg + '</th>';
}

function fillPnlTableIndividuals(object, tid, head) {
    document.getElementById(tid).innerHTML = '<th style="width:35%">' + head + '</th>' +
        '<td style="width: 12%; text-align:right;">' + object.current + '</td>' +
        '<td style="width: 8%;text-align: center;">' + object.curr_per + '%</td>' +
        '<td style="width: 12%; text-align:right;">' + object.previous + '</td>' +
        '<td style="width: 8%; text-align: center;">' + object.prev_per + '%</td>' +
        '<th style="width: 8%; text-align: center;"data-f-bold="true" data-b-a-s="thin">' + '' + '</th>' +
        '<td style="width: 12%; text-align:center;">' + object.per_change + '%</td>' +
        '<td style="width: 15%; text-align:right;">' + object.three_month_avg + '</td>';
}

function fillPnlTableExpenses(data, tid) {
    var table = document.getElementById(tid);
    Object.keys(data).forEach(function(category, i) {
        var tr = document.createElement('tr');
        tr.setAttribute('id', i)
        tr.setAttribute('class', 'accordion-toggle')
        tr.setAttribute('data-bs-toggle', 'collapse')
        tr.setAttribute('data-bs-target', '#hiddenbody_' + i)
        tr.setAttribute('aria-expanded', 'true')
        tr.setAttribute('aria-controls', 'hiddenbody_' + i)

        tr.innerHTML = '<th style="width:35%" data-f-bold="true" data-b-a-s="thin">' + category + '</th>' +
            '<th style="width: 12%; text-align:right;" data-f-bold="true" data-b-a-s="thin">' + data[category]['current'] + '</th>' +
            '<th style="width: 8%;text-align: right;" data-f-bold="true" data-b-a-s="thin">' + data[category]['curr_per'] + '%</th>' +
            '<th style="width: 12%; text-align:right;" data-f-bold="true" data-b-a-s="thin">' + data[category]['previous'] + '</th>' +
            '<th style="width: 11.5%; text-align: center;" data-f-bold="true" data-b-a-s="thin">' + data[category]['prev_per'] + '%</th>' + checkStatus(data[category]['per_change'], 'expenses') +
            '<th style="width: 12%;text-align: right;" data-f-bold="true" data-b-a-s="thin">' + data[category]['per_change'] + '%</th>' +
            '<th style="width: 15%; text-align:right;" data-f-bold="true" data-b-a-s="thin">' + data[category]['three_month_avg'] + '</th>';
        table.appendChild(tr)

        var subTr = document.createElement('tr');
        table.appendChild(subTr);

        var SubTd = document.createElement('td');
        SubTd.setAttribute('colspan', 8);

        var subNewDiv = document.createElement('div');
        subNewDiv.setAttribute('id', 'hiddenbody_' + i);
        subNewDiv.setAttribute('class', 'accordion-collapse collapse');
        subNewDiv.setAttribute('aria-labelledby', i)

        subTr.appendChild(SubTd)
        SubTd.appendChild(subNewDiv)

        var tableInside = document.createElement('table');
        tableInside.setAttribute('class', 'table');
        tableInside.setAttribute('id', 'hiddenTable_' + i);
        subNewDiv.appendChild(tableInside)

        data[category]['data'].forEach(function(object) {
            var requiredTable = document.getElementById('hiddenTable_' + i);
            var subTableRow = document.createElement('tr')
            subTableRow.innerHTML = '<td style="width:35%;"> <a href="pnl/' + object.account_for_coding + '/?selected_date=' + choosen_month + '" style="text-decoration: none">' + object.account_header + '</a></td>' +
                '<td style="width: 12%; text-align:right;">' + object.current + '</td>' +
                '<td style="width: 8%; text-align:right;">' + '' + '</td>' +
                '<td style="width: 12%; text-align:right;">' + object.previous + '</td>' +
                '<td style="width: 12.1%; text-align:center;">' + '' + '</td>' + checkStatus(object.per_change, 'expenses') +
                '<td style="width: 12%; text-align:right;">' + object.per_change + '%</td>' +
                '<td style="width: 15%; text-align:right;">' + object.three_month_avg + '</td>';
            requiredTable.appendChild(subTableRow);
        })
    })
}








// function expandRows(btnID, eIDs) {
//     var theRows = document.querySelectorAll(eIDs);
//     var theButton = document.getElementById(btnID);
//     for (var i = 0; i < theRows.length; i++) {
//         theRows[i].classList.add("show");
//         theRows[i].classList.remove("hidden");
//     }
//     theButton.setAttribute("aria-expanded", "true");
// }

// function collapseRows(btnID, eIDs) {
//     var theRows = document.querySelectorAll(eIDs);
//     var theButton = document.getElementById(btnID);
//     for (var i = 0; i < theRows.length; i++) {
//         theRows[i].classList.add("hidden");
//         theRows[i].classList.remove("show");
//     }
//     theButton.setAttribute("aria-expanded", "false");
// }