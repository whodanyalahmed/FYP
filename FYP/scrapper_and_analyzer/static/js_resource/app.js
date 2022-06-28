function readTextFile(file, callback) {
  var rawFile = new XMLHttpRequest();
  rawFile.overrideMimeType("application/json");
  rawFile.open("GET", file, true);
  rawFile.onreadystatechange = function () {
    if (rawFile.readyState === 4 && rawFile.status == "200") {
      callback(rawFile.responseText);
    }
  };
  rawFile.send(null);
}

var totalData;
var len = 0;
var getItem = JSON.parse(sessionStorage.getItem("user"));
var title = document.getElementById("title");
var title1 = document.getElementById("title1");
var priceMin = document.getElementById("price");
var priceMax = document.getElementById("price1");
var descMin = document.getElementById("descmin");
var descMax = document.getElementById("descmax");
var img = document.getElementById("img");
var img1 = document.getElementById("img1");
var dis = document.getElementById("dis");
var cont = document.getElementById("cont");

readTextFile("/static/Resources/file.json", function (text) {
  var data = JSON.parse(text);
  totalData = data;
  len = Object.keys(totalData).length.toString();
  let count = 0;

  for (let index = 0; index < len; index++) {
    if (totalData[index].value.toLowerCase() == getItem) {
      // console.log(totalData[index])
      title.innerHTML = totalData[index].value;
      title1.innerHTML = totalData[index].value;
      priceMin.innerHTML = `Price:<b> ${totalData[index].min} PKR</b>`;
      priceMax.innerHTML = `Price:<b> ${totalData[index].max} PKR</b>`;
      descMin.innerHTML = totalData[index].descriptionMin;
      descMax.innerHTML = totalData[index].descriptionMax;
      img.setAttribute("src", totalData[index].path);
      img1.setAttribute("src", totalData[index].path);
      break;
    }
    count++;
  }
  if (count == len) {
    dis.style.display = "none";
    cont.style.display = "block";
  }
});
