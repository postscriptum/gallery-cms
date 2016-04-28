function showModalImage(ev, elem) {
    ev.preventDefault();
    var img_url = elem.getAttribute("data-url");
    document.getElementById("currentImage").setAttribute("src", img_url);
    $("#modalImage").modal();
}
