function headerOnChange(obj){
    //preview the uploaded image
    document.getElementById('header-preview').src = window.URL.createObjectURL(obj[0]);

    //hide the cloud image + text
    document.getElementById('cloud').style.opacity = '0';
    document.getElementById('header_id').style.opacity = '0';
}

function logoOnChange(obj){
    //preview the uploaded image
    document.getElementById('logo-preview').src = window.URL.createObjectURL(obj[0]);
}

function setupShop(abns){

    abn = document.getElementById("abn").value;

    //if ABN is invalid
    if(validateABN(abn) === false){
        //Invalid ABN error message
        document.getElementById("err").innerHTML = "Invalid ABN - Try Again";
        document.getElementById("abn").value = "";
        return false;
    }else{
        //Verify ABN exists
        if(verifyABN(abn) === false){
            //Not exists ABN
            document.getElementById("err").innerHTML = "ABN Does Not Exist - Try Again";
            document.getElementById("abn").value = "";
            return false;
        }else{
            document.getElementById("err").innerHTML = "";
        }
    }
    
    //Checkbox MUST be checked
    var checked = document.getElementById("detail-confirm").checked;
    if(checked === false){
        //Checkbox not checked error message
        document.getElementById("err").innerHTML = "Please confirm your details by ticking the box";
        return false;
    }else{
        document.getElementById("err").innerHTML = "";
    }

    //check duplicate abn
    if (checkDuplicateABN(abns) === false) {
        document.getElementById("error_menu").style.display = "block";
        document.getElementById("abn").value = "";
        return false;
    }

}

function verifyABN(abn){
    //Request the URL with ABR GUID
    //TODO: Replace authenticationGuid with your GUID
    var xmlHttp = new XMLHttpRequest();
    const authenticationGuid = "2c577f6a-9954-4b90-bee2-943e3ab8beaf";
    xmlHttp.open( "GET", "https://abr.business.gov.au/ABRXMLSearch/AbrXmlSearch.asmx/ABRSearchBy"+
    "ABN?searchString="+abn+"&includeHistoricalDetails="+"N"+"&authenticationGuid="+authenticationGuid, false);
    xmlHttp.send(null);

    //Find if ABN is active 
    try{
        //I'm so sorry for the following code
        var myArray = xmlHttp.responseText.split("<entityStatusCode>");
        var text = myArray[1].toString();
        var status = text.split("</entityStatusCode>")[0];

        //ABN must be active
        if(status.toLowerCase() == "active"){
            return true;
        }
    }catch(err){
        //if XML response invalid
        return false;
    }
    
    return false;
    
}

function validateABN(abn){

    //null check
    if(abn == null){
        return false;
    }

    //remove all/any white spaces
    abn = abn.replace(/\s/g, '');

    //replace value for view
    document.getElementById("abn").value = abn;

    //String to char array
    var digits = abn.split('');

    //Must be 11 digits
    if(digits.length != 11){
        return false;
    }

    //Parse char to int
    for (let i = 0; i < digits.length; i++) {
        digits[i] = parseInt(digits[i]);

        //if failed to parse char to int -> invalid ABN
        if(isNaN(digits[i])){
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
    for (var i = 0; i < abns.length; i ++) {
        if (abns[i] === parseInt(abn)) {
            return false;
        }
    }
}

//Trigger file upload on div click
function clickHeaderUpload(){
    document.getElementById("upload_header").click();
}