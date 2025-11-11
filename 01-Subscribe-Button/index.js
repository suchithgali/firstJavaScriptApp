let subscribe_state = document.getElementById("Subscriber").innerHTML
console.log(subscribe_state)

function doSubscribe(){
    if (subscribe_state == "Subscribe"){
        subscribe_state = document.getElementById("Subscriber").innerHTML = "Subscribed";
    }
    else{
        subscribe_state = document.getElementById("Subscriber").innerHTML = "Subscribe";
    }
}