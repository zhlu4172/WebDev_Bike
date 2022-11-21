var money = document.getElementsByClassName("money")[0];
var prices = document.getElementsByClassName("price");
var all = 0;
for (let i=0; i<prices.length; i++) {
    var price = prices[i].innerHTML.replace(/[^\d.-]/g, '');
    all += parseFloat(price);
}
money.innerHTML = "$" + all.toFixed(2);

if (document.getElementsByClassName("Cart_Item").length === 0) {
    document.getElementById("empty_cart").style.display = "block";
}