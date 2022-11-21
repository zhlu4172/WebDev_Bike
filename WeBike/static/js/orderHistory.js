//popup feedback
function openForm(val) {
    document.getElementById("myForm").style.display = "block";
    document.getElementById("name_orderNum").innerHTML = 
        document.getElementById("orderTable").rows[val.rowIndex].cells[3].innerHTML + 
        " -- Order No: " +
        document.getElementById("orderTable").rows[val.rowIndex].cells[5].innerHTML;
    document.getElementById('suid').value = document.getElementById("orderTable").rows[val.rowIndex].cells[3].innerHTML;
}
   
function reviewFormat(rating_value, rating_id) {
    var stars = Math.floor(rating_value);


    var myTable = document.getElementById("orderTable");
    for (var i = 1; i < myTable.rows.length; i ++) {

        if ((myTable.rows[i].cells[5]).innerHTML == rating_id) {
            generateStars(stars, i);
        }
    }

}

// Function to generate the stars
function generateStars(amount_gold, row_index) {
    document.getElementById("orderTable").rows[row_index].cells[6].innerHTML = "";

    var div_element = document.createElement("div");
    div_element.setAttribute("id", "div_element");

    // create golden stars
    for (var i = 0; i < amount_gold; i++) {
        // coudln't find how to load locally
        var img = document.createElement("img");
        img.setAttribute("id", "star_image");
        img.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Gold_Star.svg/2048px-Gold_Star.svg.png";
        div_element.appendChild(img);
    }

    // create blank stars
    for (var i = 0; i < 5 - amount_gold; i++) {
        var img = document.createElement("img");
        img.setAttribute("id", "star_image");
        img.src = "https://uxwing.com/wp-content/themes/uxwing/download/arts-graphic-shapes/star-line-yellow-icon.png";
        div_element.appendChild(img);
    }

    
    document.getElementById("orderTable").rows[row_index].cells[6].appendChild(div_element);

}


function closeForm() {
    document.getElementById("myForm").style.display = "none";
    
    //Clear Text
    document.getElementById("review_text").value = "";

    //Clear Star Checked
    radiobtn = "";
    for (let i = 0; i < 5; i++) {
        radio = "rating-" + (i+1);
        // alert(radio);
        radiobtn = document.getElementById(radio);
        radiobtn.checked = false;
      }
}

function orderFunction() {
    var table = document.getElementById("orderTable");
    var arr = [];

    for (let i = 1; i < table.rows.length; i++) {
        var clone = table.rows[i].cloneNode(true);
        arr.push(clone);
    }

    var reversed = arr.reverse();

    for (let i = 0; i < arr.length; i++) {
        table.deleteRow(1);
        table.appendChild(reversed[i]);
    }

    let text = document.getElementById("OrderText").innerHTML;
    const str = "Showing Latest Purchase";
    console.log(text.localeCompare(str));
    
    if (text.localeCompare(str) == 0) {
        document.getElementById("OrderText").innerHTML = "Showing Earliest Purchase";
    } else {
        document.getElementById("OrderText").innerHTML = "Showing Latest Purchase";
    }
}