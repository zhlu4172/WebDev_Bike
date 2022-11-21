var uploadField = document.getElementsByName("avatar")[0];
uploadField.onchange = function() {
    if(this.files[0].size > 10 * 1000 * 1000){
       alert("File cannot exceed 10MB");
       this.value = "";
    };
};

const url = window.location.href;
if (!url.includes("profile")) {
    const reviews = document.getElementsByClassName("reviews")[0];
    reviews.style.display = "none";
}

if (url.includes("profile")) {
    clean();
    const tablink_reviews = document.getElementById("tablink_reviews");
    tablink_reviews.className += " active";
}

if (url.includes("orderHistory")) {
    clean();
    const tablink_orders = document.getElementById("tablink_orders");
    tablink_orders.className += " active";
}

if (url.includes("mycard")) {
    clean();
    const tablink_cards = document.getElementById("tablink_cards");
    tablink_cards.className += " active";
}

function clean() {
    const tablinks = document.getElementsByName("tablink");
    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
}