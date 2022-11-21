/*
----------------------------------------------------------------
    Function to calculate the total for a single product
    Updates every product and the running subtotal and grandtotal 
    (Individual price * Quantity)
*/
function generateSingleProductTotal() {
    var table = document.getElementById("myTable");
    for (var i=1, row; row = table.rows[i]; i++) {
        var price = document.getElementById("myTable").rows[i].cells[2].innerHTML;
        var quantity = document.getElementById("myTable").rows[i].cells[3].children[0].value;
        var total = parseFloat(price) * parseFloat(quantity);
        document.getElementById("myTable").rows[i].cells[4].innerHTML = total;
        calculateBeforeGST();
        calculateGrandTotal();
    }
}

/*
----------------------------------------------------------------
    Function to calculate the sum of all product subtotals
*/
function calculateBeforeGST() {
    var table = document.getElementById("myTable");
    var total = 0;
    for (var i=1, row; row = table.rows[i]; i++) {
            var value = parseFloat(document.getElementById("myTable").rows[i].cells[4].innerHTML);
            total += value;    
    }
    document.getElementById("SubtotalAmount").innerHTML = total;
}

/*
----------------------------------------------------------------
    Function to calculate the grand total:
    (Subtotal + GST)
*/
function calculateGrandTotal() {
    let subtotal = parseFloat(document.getElementById("SubtotalAmount").innerHTML);
    let gst = parseFloat(document.getElementById("GST").innerHTML);
    let ans = subtotal+gst;
    document.getElementById("GrandTotal").innerHTML = ans;
}


/*
----------------------------------------------------------------
    Function to generate the table that shows all the
    information about the users cart
*/

function generateCart() {
    // Creating Table
    var x = document.createElement("TABLE");
    x.setAttribute("id", "myTable");
    document.getElementById("ProductsDiv").appendChild(x);

    // Createing Headers
    var header = x.createTHead();
    var row = header.insertRow(0);
    var cell = row.insertCell(0);
    cell.setAttribute("id", "TH");
    cell.innerHTML = "Product Image";

    cell = row.insertCell(1);
    cell.setAttribute("id", "TH");
    cell.innerHTML = "Product Name";

    cell = row.insertCell(2);
    cell.setAttribute("id", "TH");
    cell.innerHTML = "Individual Price";

    cell = row.insertCell(3);
    cell.setAttribute("id", "TH");
    cell.innerHTML = "Quantity";

    cell = row.insertCell(4);
    cell.setAttribute("id", "TH");
    cell.innerHTML = "Subtotal";
  
    // Lenght of cart would obviously not be hard-coded
    var cartLength = 2;
 
    // loop to populate each row with cart details
    // set to 1 as the 0th row is the headings
    for (let i = 1; i <= cartLength; i++) {
        // Creates the row
        var newRow = document.createElement("TR");
        var name = "TR" + i;
        newRow.setAttribute("id", name);
        document.getElementById("myTable").appendChild(newRow);

        // Product Image
        var z = document.createElement("TD");
        var t = document.createElement("img");
        z.setAttribute("id", "image");
        t.src= "../../static/images/fake_bike_pic.png";
        z.appendChild(t);
        document.getElementById(name).appendChild(z);

        // Product Name
        var z = document.createElement("TD");
        z.setAttribute("id", "element");
        var t = document.createTextNode("Product Name");
        z.appendChild(t);
        document.getElementById(name).appendChild(z);

        // Individual Price
        var z = document.createElement("TD");
        z.setAttribute("id", "element");
        var price = document.createTextNode("10");
        z.appendChild(price);
        document.getElementById(name).appendChild(z);

        // Quantity
        var z = document.createElement("TD");
        z.setAttribute("id", "element");
        var t = document.createElement("input");
        t.setAttribute("id", "quantityField");
        t.type = "number";
        t.value = "1";
        t.min = "1";
        z.appendChild(t);
        document.getElementById(name).appendChild(z);
        // event listener to update values if quantitiy changes
        t.addEventListener("change", (event) => {
            generateSingleProductTotal();
        });

        // Subtotal Column
        var z = document.createElement("TD");
        z.setAttribute("id", "element");
        
        var t = document.createTextNode(price.nodeValue);
        z.appendChild(t);
        document.getElementById(name).appendChild(z);
    }

    // import right fonts in css check and fix!!!!
}
