
function plot(before,after) {

    console.log(before);
    console.log(after);
    
    url = `/en/mbl/${before}`;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url = url, false ); 
    xmlHttp.send( null );
    result = xmlHttp.responseText;
    blocks = JSON.parse(result);
    blocks.forEach(function(res) {    
	bef = []
	res.forEach(function(x) {
	    bef.push([x[1],x[0]]);
	});    
	var linebef = new L.Polyline(bef, {
	    color: 'darkblue', weight: 2, opacity: 0.5, smoothFactor: 1
	});
	linebef.addTo(map);
    });
    
    url = `/en/mbl/${after}`;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url = url, false ); 
    xmlHttp.send( null );
    result = xmlHttp.responseText;
    blocks = JSON.parse(result);
    blocks.forEach(function(res) {        
	aft = []
	res.forEach(function(x) {
	    aft.push([x[1],x[0]]);
	});    
	var lineaft = new L.Polyline(aft, {
	    color: 'red', weight: 2, opacity: 0.5, smoothFactor: 1
	});
	lineaft.addTo(map);
    });

    url = `/en/mbl/2024/ukrdata/region_transnistria.json`;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url = url, false ); 
    xmlHttp.send( null );
    result = xmlHttp.responseText;
    res = JSON.parse(result);
    trlist = []
    res.forEach(function(x) {
	trlist.push([x[0],x[1]]);
    });    
    var linetr = new L.Polyline(trlist, {
	color: 'red', weight: 2, opacity: 0.5, smoothFactor: 1
    });
    linetr.addTo(map);
    
    
}

function init() {
    map = L.map('map').setView([48,37], 6);
    
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '<a href="https://www.google.com/maps/d/viewer?mid=1V8NzjQkzMOhpuLhkktbiKgodOQ27X6IV">Suriyak Maps</a>'
    }).addTo(map);

}


