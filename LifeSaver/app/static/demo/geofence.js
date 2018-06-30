var map = null;
  var radius_circle = null;
  var markers_on_map = [];

  //all_locations is just a sample, you will probably load those from database
  var all_locations = [
	  {type: "Restaurant", name: "Restaurant 1", lat: 40.723080, lng: -73.984340},
	  {type: "School", name: "School 1", lat: 40.724705, lng: -73.986611},
	  {type: "School", name: "School 2", lat: 40.724165, lng: -73.983883},
	  {type: "Restaurant", name: "Restaurant 2", lat: 40.721819, lng: -73.991358},
	  {type: "School", name: "School 3", lat: 40.732056, lng: -73.998683}
  ];

  //initialize map on document ready
  $(document).ready(function(){
      var latlng = new google.maps.LatLng(40.723080, -73.984340); //you can use any location as center on map startup
      var myOptions = {
        zoom: 14,
        center: latlng,
        mapTypeControl: true,
        mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
        navigationControl: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      };
      map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

	  google.maps.event.addListener(map, 'click', showCloseLocations);
  });

  function showCloseLocations(e) {
  	var i;
  	var radius_km = $('#radius_km').val();
  	var address = $('#address').val();

  	//remove all radii and markers from map before displaying new ones
  	if (radius_circle) {
  		radius_circle.setMap(null);
  		radius_circle = null;
  	}
  	for (i = 0; i < markers_on_map.length; i++) {
  		if (markers_on_map[i]) {
  			markers_on_map[i].setMap(null);
  			markers_on_map[i] = null;
  		}
  	}

  	var address_lat_lng = e.latLng;
  	radius_circle = new google.maps.Circle({
  		center: address_lat_lng,
  		radius: radius_km * 1000,
  		clickable: false,
  		map: map
  	});
	if(radius_circle) map.fitBounds(radius_circle.getBounds());
  	for (var j = 0; j < all_locations.length; j++) {
  		(function (location) {
  			var marker_lat_lng = new google.maps.LatLng(location.lat, location.lng);
  			var distance_from_location = google.maps.geometry.spherical.computeDistanceBetween(address_lat_lng, marker_lat_lng); //distance in meters between your location and the marker
  			if (distance_from_location <= radius_km * 1000) {
  				var new_marker = new google.maps.Marker({
  					position: marker_lat_lng,
  					map: map,
  					title: location.name
  				});
  				google.maps.event.addListener(new_marker, 'click', function () {
  					alert(location.name + " is " + distance_from_location + " meters from my location");
  				});
  				markers_on_map.push(new_marker);
  			}
  		})(all_locations[j]);
  	}
  }
