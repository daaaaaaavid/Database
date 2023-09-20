$(document).ready(function(){
    form();
    $("#href_query").prop('select','true');
    $("#href_query").css('background-color','#9ca8b8');
    $("#href_query_p").css('font-weight','800');

})
function form(){

    document.getElementById('selectgame').addEventListener('change', function(evt) {

    var game = this.value;
    const list = document.getElementById("selectid");
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }
    for(var i=(game-1)*4+1;i<game*4+1;i++){
        let o=document.createElement('option');
        o.setAttribute("value",i);
        o.innerHTML=i;
        list.append(o);
    }
    id=$('#selectid').find(":selected").val();
    if($('#selectype').find(":selected").val()=='money'){
        money(id);
    }
    else if($('#selectype').find(":selected").val()=='assets'){
        assets(id);
    }
    else if($('#selectype').find(":selected").val()=='situation'){
        situation(id);
    }
    else if($('#selectype').find(":selected").val()=='typ_num'){
        typ_num(id);
    }

    });
    document.getElementById('selectid').addEventListener('change', function(evt) {
    console.log(evt);
        id=$('#selectid').find(":selected").val();
        if($('#selectype').find(":selected").val()=='money'){
            money(id);
        }
        else if($('#selectype').find(":selected").val()=='assets'){
            assets(id);
        }
        else if($('#selectype').find(":selected").val()=='situation'){
            situation(id);
        }
        else if($('#selectype').find(":selected").val()=='typ_num'){
            typ_num(id);
        }
    });

    document.getElementById('selectype').addEventListener('change', function(evt) {
        console.log(evt);
        id=$('#selectid').find(":selected").val();
        if($('#selectype').find(":selected").val()=='money'){
            money(id);
        }
        else if($('#selectype').find(":selected").val()=='assets'){
            assets(id);
        }
        else if($('#selectype').find(":selected").val()=='situation'){
            situation(id);
        }
        else if($('#selectype').find(":selected").val()=='typ_num'){
            typ_num(id);
        }
    });
}
function money(id){

    var round=[];
    for(var i=0;i<30;i++){
        round[i]=i+1;
    }

    const list = document.getElementById("canvas");
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }
    var c=document.createElement('canvas');
    list.append(c);
    var ctx = c.getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: round,
                datasets: [{
                    label: 'Balance in each round',
                    data: data[0][id-1],
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                }]
            },
        });

//    console.log(data[0][id-1]);
}
function assets(id){

    var round=[];
    for(var i=0;i<30;i++){
        round[i]=i+1;
    }

    const list = document.getElementById("canvas");
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }
    var c=document.createElement('canvas');
    list.append(c);
    var ctx = c.getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: round,
                datasets: [{
                    label: 'Assets in each round',
                    data: data[1][id-1],
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                }]
            },
        });
}
function situation(id){

    const list = document.getElementById("canvas");
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }
    var c=document.createElement('canvas');
    list.append(c);
    var ctx = c.getContext('2d');
    var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Turtle','Dog','None','God of luck','God of wealth'],
        datasets: [{
            label: 'Number of situation type',
            data: data[2][id-1]
        }]
    }
});
}
function typ_num(id){


    const list = document.getElementById("canvas");
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }
    var c=document.createElement('canvas');
    list.append(c);
    var ctx = c.getContext('2d');
    var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Mini House", "Medium-sized House", "Big House", "Mini Hotel", "Medium-sized Hotel", "Big Hotel",'Mini Mall','Medium-sized Mall','Big Mall'],
        datasets: [{
            label: 'Number of assets type',
            data: data[3][id-1]
        }]
    }
});
}