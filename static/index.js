// Time and Date
let time = document.getElementById("time");
let date = document.getElementById("date");
let date_now = new Date();
date.innerHTML = date_now.toLocaleDateString('en-GB');
setInterval(function(){
    let time_now = new Date();
    time.innerHTML = time_now.toLocaleTimeString();
},1000);


// Line Done Jobs
document.querySelectorAll("#mycheck").forEach(function(checkbox){

    checkbox.addEventListener("click", function(){

        if (checkbox.checked) {
            checkbox.parentElement.classList.add("checked");
        } else {
            checkbox.parentElement.classList.remove("checked");
        }

    });
});
