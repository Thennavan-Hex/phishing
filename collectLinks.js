function collectUniqueLinks(document_root) {
	var arr = [], l = document.links;

	for(var i=0; i<l.length; i++) {
  		arr.push(l[i].href);
	}

  // filter out duplicates
	var filteredLinks = arr.filter(function(item, pos) {
		return arr.indexOf(item) == pos;
	});

	return filteredLinks;
}


chrome.runtime.sendMessage({
    action: "getPageLinks",
    pageLinks: collectUniqueLinks(document)
});
