document.addEventListener("DOMContentLoaded",()=>{
    var request=new XMLHttpRequest();
    request.open("GET","/json");
    request.onload =()=>{
        var data = JSON.parse(request.responseText);
        var food_id=document.querySelectorAll(".food_id");
        var times=[];
        var sups=0;
        for(var i=0;i<data.length;i++){
            times.push(parseInt(data[i][2]))
        }
        const element=document.createElement("sup");
        for(var i=0;i<times.length;i++){
            sups=sups+times[i];
        };
        element.innerHTML=`+${sups}`;
        element.className="times"
        document.getElementById("cart").append(element);

        for(var i=0;i<food_id.length;i++){
            for(var j=0;j<data.length;j++){
                if(food_id[i].value==data[j][1]){
                    const element=document.createElement("sup");
                    element.innerHTML=`+${data[j][2]}`
                    if(element.innerHTML==0){
                        continue;
                    }
                    document.querySelector("#smith"+food_id[i].value).append(element);
                };
            };
        };
    };
    request.send();
});