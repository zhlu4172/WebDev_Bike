// // document.querySelector("fake_bike_pic").src = "{{medias.0.Storage_location}}";
// var elements = document.querySelectorAll(".stars-inner");
// console.log(elements[0].style.width)
// elements[0].style.width = (100 * 5) / 5 + "%";
// console.log(elements[0].style.width)

function changeCheckbox() {
  var modelCbs = document.querySelectorAll(
    ".checkbox-group input[type='checkbox']"
  );
  var filters = {
    models: getClassOfCheckedCheckboxes(modelCbs),
  };
  // var filters = getClassOfCheckedCheckboxes(modelCbs)
  filterResults(filters);
}

function getClassOfCheckedCheckboxes(checkboxes) {
  var classes = [];

  if (checkboxes && checkboxes.length > 0) {
    for (var i = 0; i < checkboxes.length; i++) {
      var cb = checkboxes[i];

      if (cb.checked) {
        classes.push(cb.getAttribute("rel"));
      }
    }
  }
  return classes;
  // console.log(classes)
}

function searchFilter(el, input, hiddenElems) {
  console.log(el.querySelector(".bike-name").textContent.includes(input));
  if (
    !el.querySelector(".bike-name").textContent.toLowerCase().includes(input.toLowerCase()) &&
    !el.querySelector(".discription").textContent.toLowerCase().includes(input.toLowerCase())
  ) {
    hiddenElems.push(el);
  }
}

function filterResults(filters) {
  var rElems = document.querySelectorAll(".bike-card");
  var hiddenElems = [];

  if (!rElems || rElems.length <= 0) {
    return;
  }

  console.log(filters.models);
  console.log(filters.models.includes("flexCheckless500buy"));
  for (var i = 0; i < rElems.length; i++) {
    var el = rElems[i];
    // console.log(el)
    const gettinginput = document.getElementById("searchProduct").value;
    console.log(gettinginput);
    console.log(el.querySelector(".stars-inner").style.width);
    var num = (
      (parseFloat(el.querySelector(".stars-inner").style.width.slice(0, -1)) /
        100) *
      5
    ).toFixed(1);
    console.log(num);

    searchFilter(el, gettinginput, hiddenElems);
    if (!filters.models.includes("ratingFive")) {
      if (Math.floor(num) == 5) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("ratingFour")) {
      if (Math.floor(num) == 4) {
        hiddenElems.push(el);
      }
    }
    if (!filters.models.includes("ratingThree")) {
      if (Math.floor(num) == 3) {
        hiddenElems.push(el);
      }
    }
    if (!filters.models.includes("ratingTwo")) {
      if (Math.floor(num) == 2) {
        hiddenElems.push(el);
      }
    }
    if (!filters.models.includes("ratingOne")) {
      if (Math.floor(num) == 1) {
        hiddenElems.push(el);
      }
    }
    if (!filters.models.includes("ratingZero")) {
      if (Math.floor(num) == 0) {
        hiddenElems.push(el);
      }
    }
    if (!filters.models.includes("flexCheckless500buy")) {
      if (
        parseFloat(el.querySelector(".sell-price").textContent.substring(1)) <
        500
      ) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck500To1000buy")) {
      console.log(
        parseFloat(el.querySelector(".sell-price").textContent.substring(1))
      );
      if (
        parseFloat(el.querySelector(".sell-price").textContent.substring(1)) >=
          500 &&
        parseFloat(el.querySelector(".sell-price").textContent.substring(1)) <
          1000
      ) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck1000To1500buy")) {
      if (
        parseFloat(el.querySelector(".sell-price").textContent.substring(1)) >=
          1000 &&
        parseFloat(el.querySelector(".sell-price").textContent.substring(1)) <
          1500
      ) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck1500To2000buy")) {
      console.log(
        parseFloat(el.querySelector(".sell-price").textContent.substring(1))
      );
      if (
        parseFloat(el.querySelector(".sell-price").textContent.substring(1)) >=
          1500 &&
        parseFloat(el.querySelector(".sell-price").textContent.substring(1)) <
          2000
      ) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheckAbove2000buy")) {
      console.log(
        parseFloat(el.querySelector(".sell-price").textContent.substring(1))
      );
      if (
        parseFloat(el.querySelector(".sell-price").textContent.substring(1)) >=
        2000
      ) {
        hiddenElems.push(el);
      }
    }

    ///////////////////////////////////////////////////////////////////////////////

    if (!filters.models.includes("flexCheckless50rent")) {
      var rentprice = parseFloat(
        el.querySelector(".rent-price").textContent.substring(1)
      );
      if (rentprice < 50) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck50To100rent")) {
      var rentprice = parseFloat(
        el.querySelector(".rent-price").textContent.substring(1)
      );
      if (rentprice >= 50 && rentprice < 100) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck100To150rent")) {
      var rentprice = parseFloat(
        el.querySelector(".rent-price").textContent.substring(1)
      );
      if (rentprice >= 100 && rentprice < 150) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck150To200rent")) {
      var rentprice = parseFloat(
        el.querySelector(".rent-price").textContent.substring(1)
      );
      if (rentprice >= 150 && rentprice < 200) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheckAbove200rent")) {
      var rentprice = parseFloat(
        el.querySelector(".rent-price").textContent.substring(1)
      );
      if (rentprice >= 200) {
        hiddenElems.push(el);
      }
    }


    //////////////////////////////////////////////////////////
    if (!filters.models.includes("flexCheckless500")) {
      var len = el.querySelector(".distance").textContent.length
      var realDistance = parseFloat(
        el.querySelector(".distance").textContent.substring(0,len-2)
      );
      console.log(realDistance)
      if (realDistance < 0.5) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck500To1")) {
      var len = el.querySelector(".distance").textContent.length
      var realDistance = parseFloat(
        el.querySelector(".distance").textContent.substring(0,len-2)
      );
      console.log(realDistance)
      if (realDistance >= 0.5 && realDistance < 1) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck500To1")) {
      var len = el.querySelector(".distance").textContent.length
      var realDistance = parseFloat(
        el.querySelector(".distance").textContent.substring(0,len-2)
      );
      console.log(realDistance)
      if (realDistance >= 0.5 && realDistance < 1) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck1To2")) {
      var len = el.querySelector(".distance").textContent.length
      var realDistance = parseFloat(
        el.querySelector(".distance").textContent.substring(0,len-2)
      );
      console.log(realDistance)
      if (realDistance >= 1 && realDistance < 2) {
        hiddenElems.push(el);
      }
    }

    if (!filters.models.includes("flexCheck2To5")) {
      var len = el.querySelector(".distance").textContent.length
      var realDistance = parseFloat(
        el.querySelector(".distance").textContent.substring(0,len-2)
      );
      console.log(realDistance)
      if (realDistance >= 2 && realDistance < 5) {
        hiddenElems.push(el);
      }
    }
    if (!filters.models.includes("flexCheck5To10")) {
      var len = el.querySelector(".distance").textContent.length
      var realDistance = parseFloat(
        el.querySelector(".distance").textContent.substring(0,len-2)
      );
      console.log(realDistance)
      if (realDistance >= 5 && realDistance < 10) {
        hiddenElems.push(el);
      }
    }
    if (!filters.models.includes("flexCheckMore10")) {
      var len = el.querySelector(".distance").textContent.length
      var realDistance = parseFloat(
        el.querySelector(".distance").textContent.substring(0,len-2)
      );
      console.log(realDistance)
      if (realDistance >= 10) {
        hiddenElems.push(el);
      }
    }
  }

  for (var i = 0; i < rElems.length; i++) {
    rElems[i].style.display = "block";
  }

  if (hiddenElems.length <= 0) {
    return;
  }

  for (var i = 0; i < hiddenElems.length; i++) {
    hiddenElems[i].style.display = "none";
  }
}
