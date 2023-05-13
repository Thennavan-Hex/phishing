chrome.runtime.onMessage.addListener(function(request, sender) {
  if (request.action == "getPageLinks") {
    pageLinks = request.pageLinks;
    buildTable(pageLinks, linkTable);
    message.innerHTML = "<h5><i>Colected " + pageLinks.length + " links</i></h5>";
  }
});


function onWindowLoad() {
  var pageLinks = [];
  var message = document.querySelector('#message');
  var linkTable = document.querySelector('#linkTable');
  // adding event listeners
  document.querySelector('#exportBtn').addEventListener('click', exportTable);
  document.querySelector('#filterInput').addEventListener('keyup', filterTable);

  chrome.tabs.executeScript(null, {
    file: "collectLinks.js"
  }, function() {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error with script : \n' + chrome.runtime.lastError.message;
    }
  });
}

function buildTable(links, t) {
  links.forEach(function(link){
    //console.log(link);
    var row = t.insertRow(0);
    var cell = row.insertCell(0);
    cell.innerHTML = link;
  });
}

function exportTable() {
  var csvFile;
  var downloadLink;
  var filename = 'pagelinks.csv';
  csvFile = new Blob([pageLinks.join("\n")], {type: "text/csv"});
  downloadLink = document.createElement("a");
  downloadLink.download = filename;
  downloadLink.href = window.URL.createObjectURL(csvFile);
  downloadLink.style.display = "none";
  document.body.appendChild(downloadLink);//here we need to make it download automaticly
  downloadLink.click();
}

function filterTable() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("filterInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("linkTable");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

window.onload = onWindowLoad;

//developed by thens