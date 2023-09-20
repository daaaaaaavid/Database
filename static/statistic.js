$(document).ready(function(){

    $("#href_statistic").prop('select','true');
    $("#href_statistic").css('background-color','#9ca8b8');
    $("#href_statistic_p").css('font-weight','800');
    build_pie();
    lucky_table();
})
function build_pie(){

    const list = document.getElementById("canvas");
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }
    var c=document.createElement('canvas');
    list.append(c);
    var ctx = c.getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
        datasets: [
          {
            label: 'Number of each role been used',
            data: data,
            backgroundColor: [
              'rgb(255, 99, 132)',
              'rgb(255, 159, 64)',
              'rgb(255, 205, 86)',
              'rgb(75, 192, 192)',
              'rgb(54, 162, 235)',
            ],
          },
        ],
        labels: ['A Tubo','Madam Qian','Sun Xiaomei','John Joe','Little Danny'],
      },
      options: {
        plugins: {
          datalabels: {
            formatter: (value) => {
              if (value < 15) return '';
              return value + '%';
            },
          },
        },
      },
   });
}
function lucky_table(){
    table_head=['ranking','playerID','Lucky Earned']


    let tb=document.createElement('table');
    tb.setAttribute("class","lucky_container_table");
    $('#lucky_container').append(tb);

    let tr=document.createElement('tr');
    tr.setAttribute('class','history_container_tr');
    let th=document.createElement('thead');
    th.setAttribute('class','history_container_th');
    th.append(tr);
    tb.append(th);
    for(var j=0;j<table_head.length;j++){
        let th=document.createElement('th');
        th.setAttribute('class','history_container_th');
        th.innerHTML=table_head[j];
        tr.append(th);
    }
    let tbod=document.createElement('tbody');
    tbod.setAttribute('class','history_container_tb');
    tb.append(tbod);
    for(var j=0;j<7;j++){
        let tr=document.createElement('tr');
        tr.setAttribute('class','history_container_tr');

        let td=document.createElement('td');
        td.setAttribute('class','history_container_td');
        if (j==0)
            td.innerHTML='1st';
        else if (j==1){
            td.innerHTML='2nd';
        }
        else if (j==2){
            td.innerHTML='3rd';
        }
        else{
            td.innerHTML=' ';
        }
        tr.append(td);

        for(var k=0;k<lucky[j].length;k++){

            td=document.createElement('td');
            td.setAttribute('class','history_container_td');
            if (k==0){
                td.innerHTML=lucky[j][k]+1;
            }
            else{
                td.innerHTML=lucky[j][k]*1000;
            }
            tr.append(td);
        }
        tbod.append(tr);
    }
}