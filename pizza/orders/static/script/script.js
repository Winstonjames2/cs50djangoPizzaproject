document.addEventListener("DOMContentLoaded",()=>{
    var request=new XMLHttpRequest();
    request.open("GET","/json");
    request.onload =()=>{
        var data = JSON.parse(request.responseText);
        const food_id=document.querySelector("#food_id")
        localStorage.setItem("data",data[food_id])
    };
    request.send();
    document.querySelector("#smith").innerHTML=localStorage.data
})