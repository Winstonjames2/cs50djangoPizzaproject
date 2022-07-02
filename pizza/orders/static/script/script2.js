document.addEventListener("DOMContentLoaded",()=>{
    var request=new XMLHttpRequest();
    request.open("GET","/json");
    request.onload =()=>{
        var data = JSON.parse(request.responseText);
        var food_id=document.querySelectorAll(".food_id");
        var totalAmount=[];
        var total=0;
        for(var i=0;i<food_id.length;i++){
            for(var j=0;j<data.length;j++){
                if(food_id[i].value==data[j][1]){
                    const element=document.createElement("sup");
                    element.innerHTML=`+${data[j][2]}`
                    if(element.innerHTML==0){
                        continue;
                    };
                    document.querySelector("#smith"+food_id[i].value).append(element);

                    var price=document.querySelector("#price"+food_id[i].value);
                    var total=(price.innerHTML)*data[j][2];
                    price.innerHTML=`$${price.innerHTML} x ${data[j][2]}=$${total.toFixed(2)}`;
                    totalAmount.push(parseFloat(total.toFixed(2)));
                };
            };
        };
        for(var i=0;i<totalAmount.length;i++){
            total=total+totalAmount[i];
        };
        document.querySelector(".amount").innerHTML=total.toFixed(2)
        // document.querySelector(".amount2").value=total.toFixed(2)
    };
    request.send();
});