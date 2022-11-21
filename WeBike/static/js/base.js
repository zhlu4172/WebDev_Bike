function menuSwitch() {
  var mobileMenuBtn = document.getElementsByClassName("mobile_menu_button")[0];
  var mobileMenu = document.getElementsByClassName("mobile_menu")[0];

  if (mobileMenu.style.display === "none") {
    mobileMenu.style.display = "flex";
    mobileMenuBtn.innerHTML = "Close";
  } else {
    mobileMenu.style.display = "none";
    mobileMenuBtn.innerHTML = "Menu";
  }
}

function openNav() {
  document.getElementsByClassName("search_menu_input")[0].focus();
  document.getElementsByClassName("search_menu")[0].style.height = "100%";
}

function closeNav() {
  document.getElementsByClassName("search_menu")[0].style.height = "0%";
}

if (localStorage.getItem("location") !== null) {
  console.log(localStorage.getItem("location"));
  document.getElementById("select_location").innerText = localStorage.getItem("location");
}

function closeLocationMenu() {
  var location = document.getElementById("pac-input").value;
  if (location !== "") {
    document.getElementById("select_location").innerText = location;
    localStorage.setItem("location", location);
  }
  document.getElementById('id01').style.display='none';
  window.location.href = window.location.href;
}

let geocoder;
let service;
let travelmode;

function initAutocomplete() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -33.8688, lng: 151.2195 },
    zoom: 13,
    mapTypeId: "roadmap",
  });
  geocoder = new google.maps.Geocoder();
  service = new google.maps.DistanceMatrixService();
  travelmode = google.maps.TravelMode.DRIVING;
  // Create the search box and link it to the UI element.
  const input = document.getElementById("pac-input");
  const searchBox = new google.maps.places.SearchBox(input);

  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
  // Bias the SearchBox results towards current map's viewport.
  map.addListener("bounds_changed", () => {
    searchBox.setBounds(map.getBounds());
  });

  let markers = [];

  // Listen for the event fired when the user selects a prediction and retrieve
  // more details for that place.
  searchBox.addListener("places_changed", () => {
    const places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }

    // Clear out the old markers.
    markers.forEach((marker) => {
      marker.setMap(null);
    });
    markers = [];

    // For each place, get the icon, name and location.
    const bounds = new google.maps.LatLngBounds();

    places.forEach((place) => {
      if (!place.geometry || !place.geometry.location) {
        console.log("Returned place contains no geometry");
        return;
      }

      const icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25),
      };

      // Create a marker for each place.
      markers.push(
        new google.maps.Marker({
          map,
          icon,
          title: place.name,
          position: place.geometry.location,
        })
      );
      if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    map.fitBounds(bounds);
  });

  document.getElementById("auto_getLocation").addEventListener("click", () => {
    getLocation(geocoder);
  });

  for (let i=0; i<document.getElementsByClassName("place").length; i++) {
    calcDistance(document.getElementsByClassName("distance")[i].id, document.getElementsByClassName("place")[i].innerHTML);
  }
}

function getLocation(geocoder) {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      const latlng = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
      };

      geocoder
        .geocode({ location: latlng })
        .then((response) => {
          if (response.results[0]) {
            var location = response.results[0].formatted_address;
            console.log(location);
            document.getElementById("select_location").innerText = location;
            localStorage.setItem("location", location);
            document.getElementById('id01').style.display='none';
            window.location.href = window.location.href;
          } else {
            window.alert("No results found");
          }
        })
        .catch((e) => window.alert("Geocoder failed due to: " + e));
        });
  }
}

function calcDistance(id, location) {
  const request = {
    origins: [localStorage.getItem("location")],
    destinations: [location],
    travelMode: travelmode,
  }
  service.getDistanceMatrix(request).then((response) => {
    console.log(response.rows[0].elements[0].distance.text);
    document.getElementById(id).innerText = response.rows[0].elements[0].distance.text;
  });
}

window.initAutocomplete = initAutocomplete;