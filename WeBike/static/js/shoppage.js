// document.querySelector(".edit").addEventListener("click", function () {
//   document.querySelector(".cancel").style.display = "inline";
//   document.querySelector(".save").style.display = "inline";
//   document.querySelector(".edit").style.display = "none";
//   document.querySelector(".forms").style.display = "block";
//   document.querySelector(".forms__right").style.display = "block";
//   // document.getElementById("shop-details-form").style.display = "block";
//   document.querySelector(".all_info").style.display = "none";
//   document.querySelector(".all_info__right").style.display = "none";
//   document.querySelector(".bike_list").style.display = "none";
//   document.querySelector(".shop_products_form").style.display = "block";
//   // setValue();
//   // setFakeBikeValue();
//   document.getElementById("avater-input").style.display = "block";
//   document.querySelector(".info-banner").style.height = "auto";
//   // console.log(document.querySelector(".info-banner").style.height.value);
// });

// document.querySelector(".save").addEventListener("click", function () {
//   document.querySelector(".cancel").style.display = "none";
//   document.querySelector(".save").style.display = "none";
//   document.querySelector(".edit").style.display = "inline";
//   const form = document.getElementById("shop-details-form");
//   // form.style.display = "none";
//   document.querySelector(".forms").style.display = "none";
//   document.querySelector(".forms__right").style.display = "none";
//   document.querySelector(".bike_list").style.display = "block";
//   document.querySelector(".shop_products_form").style.display = "none";
//   document.querySelector(".all_info").style.display = "block";
//   document.querySelector(".all_info__right").style.display = "block";
//   // updateValue(form);
//   // updateFakeBikeValue();
//   document.getElementById("avater-input").style.display = "none";
// });

// document.querySelector(".cancel").addEventListener("click", function () {
//   document.querySelector(".cancel").style.display = "none";
//   document.querySelector(".save").style.display = "none";
//   document.querySelector(".edit").style.display = "inline";
//   // document.getElementById("shop-details-form").style.display = "none";
//   document.querySelector(".forms").style.display = "none";
//   document.querySelector(".forms__right").style.display = "none";
//   document.querySelector(".all_info").style.display = "block";
//   document.querySelector(".all_info__right").style.display = "block";
//   document.querySelector(".bike_list").style.display = "block";
//   document.querySelector(".shop_products_form").style.display = "none";
//   document.getElementById("avater-input").style.display = "none";
// });

function changeThemeColor(getColor) {
  let themeBackground1 = document.querySelector(".logo_banner");
  let themeBackground2 = document.querySelector(".each_bike");
  let themeBackground3 = document.getElementById("product_form");
  let editButton = document.getElementById("edit");
  let saveButton = document.getElementById("save");
  let wordColor = document.body;
  console.log(getColor.value);
  if (getColor.value === "bright") {
    console.log("hi");
    themeBackground1.style.background = "#f7f7f7";
    themeBackground2.style.background = "#f7f7f7";
    themeBackground3.style.background = "#f7f7f7";
    wordColor.style.color = "black";
  } else if (getColor.value === "dark") {
    themeBackground1.style.background = "#1c2f40";
    themeBackground2.style.background = "#1c2f40";
    themeBackground3.style.background = "#1c2f40";
    editButton.style.background = "#1c2f40";
    saveButton.style.background = "#1c2f40";
    editButton.style.color = "white";
    saveButton.style.color = "white";
    wordColor.style.color = "black";
  } else if (getColor.value === "green-blue") {
    themeBackground1.style.background = "#2db8c5";
    themeBackground2.style.background = "#2db8c5";
    themeBackground3.style.background = "#2db8c5";
    editButton.style.background = "#2db8c5";
    saveButton.style.background = "#2db8c5";
    editButton.style.color = "black";
    saveButton.style.color = "black";
    wordColor.style.color = "black";
  } else if (getColor.value === "pink") {
    themeBackground1.style.background = "#daabb5";
    themeBackground2.style.background = "#daabb5";
    themeBackground3.style.background = "#daabb5";
    editButton.style.background = "#daabb5";
    saveButton.style.background = "#daabb5";
    editButton.style.color = "3a3a3a";
    saveButton.style.color = "3a3a3a";
    wordColor.style.color = "#3a3a3a";
  } else if (getColor.value === "green") {
    themeBackground1.style.background = "#98bf64";
    themeBackground2.style.background = "#98bf64";
    themeBackground3.style.background = "#98bf64";
    editButton.style.background = "#98bf64";
    saveButton.style.background = "#98bf64";
    editButton.style.color = "3a3a3a";
    saveButton.style.color = "3a3a3a";
    wordColor.style.color = "#3a3a3a";
  } else if (getColor.value === "purple") {
    themeBackground1.style.background = "#b2a4d8";
    themeBackground2.style.background = "#b2a4d8";
    themeBackground3.style.background = "#b2a4d8";
    editButton.style.background = "#b2a4d8";
    saveButton.style.background = "#b2a4d8";
    editButton.style.color = "3a3a3a";
    saveButton.style.color = "3a3a3a";
    wordColor.style.color = "#3a3a3a";
  }
}

function headerOnChange(obj) {
  //preview the uploaded image
  document.getElementById("header-preview").src = window.URL.createObjectURL(
    obj[0]
  );

  // //hide the cloud image + text
  // document.getElementById('cloud').style.opacity = '0';
  // document.getElementById('header_id').style.opacity = '0';
}

function setupShop(abns) {
  var abn = document.getElementById("abn").value;
  if (abn.length != 0) {
    //if ABN is invalid
    if (validateABN(abn) === false) {
      //Invalid ABN error message
      console.log("invalid");
      document.getElementById("err").innerHTML = "Invalid ABN - Try Again";
      document.getElementById("abn").value = "";
      document.querySelector(".submit_btn").style.display = "none";
      return false;
    } else {
      //Verify ABN exists
      if (verifyABN(abn) === false) {
        //Not exists ABN
        console.log("invalid");
        document.getElementById("err").innerHTML =
          "ABN Does Not Exist - Try Again";
        document.getElementById("abn").value = "";
        document.querySelector(".submit_btn").style.display = "none";
        return false;
      } else {
        document.getElementById("err").innerHTML = "";
      }
    }

    //check duplicate abn
    if (checkDuplicateABN(abns) === false) {
      document.getElementById("err").innerHTML = "Duplicate ABN!";
      document.getElementById("abn").value = "";
      document.querySelector(".submit_btn").style.display = "none";
      return false;
    }
  }
  console.log("hi");
  document.querySelector(".submit_btn").style.display = "block";
}

function validateABN(abn) {
  //null check
  if (abn == null) {
    return false;
  }

  //remove all/any white spaces
  abn = abn.replace(/\s/g, "");

  //replace value for view
  document.getElementById("abn").value = abn;

  //String to char array
  var digits = abn.split("");

  //Must be 11 digits
  if (digits.length != 11) {
    return false;
  }

  //Parse char to int
  for (let i = 0; i < digits.length; i++) {
    digits[i] = parseInt(digits[i]);

    //if failed to parse char to int -> invalid ABN
    if (isNaN(digits[i])) {
      return false;
    }
  }

  //Assigned weights by index given from ATO
  const weights = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19];

  //subtract 1 from first element
  digits[0] = digits[0] - 1;

  //multiply elements by ATO weights
  var sum = 0;
  for (var i = 0; i < weights.length; i += 1) {
    var weight = weights[i];
    var value = digits[i] * weights[i];
    sum += value;
  }

  var result = sum % 89;

  return result == 0;
}

function checkDuplicateABN(abns) {
  var abn = document.getElementById("abn").value;
  for (var i = 0; i < abns.length; i++) {
    if (abns[i] === parseInt(abn)) {
      return false;
    }
  }
}

function verifyABN(abn) {
  //Request the URL with ABR GUID
  //TODO: Replace authenticationGuid with your GUID
  var xmlHttp = new XMLHttpRequest();
  const authenticationGuid = "2c577f6a-9954-4b90-bee2-943e3ab8beaf";
  xmlHttp.open(
    "GET",
    "https://abr.business.gov.au/ABRXMLSearch/AbrXmlSearch.asmx/ABRSearchBy" +
      "ABN?searchString=" +
      abn +
      "&includeHistoricalDetails=" +
      "N" +
      "&authenticationGuid=" +
      authenticationGuid,
    false
  );
  xmlHttp.send(null);

  //Find if ABN is active
  try {
    //I'm so sorry for the following code
    var myArray = xmlHttp.responseText.split("<entityStatusCode>");
    var text = myArray[1].toString();
    var status = text.split("</entityStatusCode>")[0];

    //ABN must be active
    if (status.toLowerCase() == "active") {
      return true;
    }
  } catch (err) {
    //if XML response invalid
    return false;
  }

  return false;
}

// var object = document.getElementById("abn")
// object.addEventListener("change", hello());
// function hello(){
//   console.log("hello")
// }
