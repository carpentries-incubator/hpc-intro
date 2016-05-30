// Make all tables striped by default.
$("table").addClass("table table-striped");

// Handle foldable challenges (on click and at start)
$(".challenge").click(function(event) {
    $(">*:not(h2)", this).toggle(400);
});
$(".challenge").each(function() {
    $(">*:not(h2)", this).toggle();
    var h2 = $("h2:first", this);
    h2.append("<span class='fold-unfold'>(click to fold/unfold)</span>");
});

// Handle searches.
// Relies on document having 'meta' element with name 'search-domain'.
function google_search() {
  var query = document.getElementById("google-search").value;
  var domain = $("meta[name=search-domain]").attr("value");
  window.open("https://www.google.com/search?q=" + query + "+site:" + domain);
}
