$(document).ready(function(){
    footer();
    form()
    history();
})
function form(){
    let d=document.createElement('div');
    d.setAttribute("id","form_container");
    d.setAttribute("class","form_container");
    d.style.display='none';
//    f.style.display='none';
    $('#main').append(d);

    let f=document.createElement('form');
    f.setAttribute("id","form");
    f.setAttribute("class","form");
    f.setAttribute("action","/query");
    f.setAttribute("method","post");
    d.append(f);

    let s=document.createElement('select');
    s.setAttribute("id","form_player");
    s.setAttribute("name","selectid");
    f.append(s);

    for(var i=0;i<data[0].length;i++){
        let o=document.createElement('option');
        o.setAttribute("value",i+1);
        o.innerHTML=i+1;
        s.append(o);
    }

    s=document.createElement('select');
    s.setAttribute("id","form_type");
    s.setAttribute("name","selectype");
    f.append(s);

    var select_option=['Money','Assets','Special situation','Assets type'];

    for(var i=0;i<select_option.length;i++){
        let o=document.createElement('option');
        o.setAttribute("value",select_option[i]);
        o.innerHTML=select_option[i];
        s.append(o);
    }

    let b=document.createElement('button');
    b.setAttribute("type","submit");
    b.innerHTML="Go";
    f.append(b);

}



function history(){
    table_head=['ranking','playerID','Balance','Assets']
    for(var i=0;i<data.length;i++){
        let t = document.createElement('div');
        t.setAttribute("id","history"+(i+1).toString());
        t.setAttribute("class","history_container");
        let p = document.createElement('p');
        p.innerHTML='Game'+(i+1).toString();
        p.setAttribute("class","history_container_p");
        let tb=document.createElement('table');
        tb.setAttribute("class","history_container_table");
        $('#main').append(t);
        t.append(p);
        t.append(tb);
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
        for(var j=0;j<data[i].length;j++){
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

            for(var k=0;k<data[i][j].length;k++){

                td=document.createElement('td');
                td.setAttribute('class','history_container_td');
                td.innerHTML=data[i][j][k];
                tr.append(td);
            }
            tbod.append(tr);
        }
    }
}
function footer(){
    $("#href_history").prop('select','true');
    $("#href_history").css('background-color','#9ca8b8');
    $("#href_history_p").css('font-weight','800');

}