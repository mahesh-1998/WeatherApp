window.addEventListener("map:init", function (e) {
    var detail = e.detail;
   
    L.marker([41.49,-99.90]).addTo(detail.map);
 
}, false);
   
    function myFunction()
    {
        city = getElementById('city');
        console.log("hi");
    }