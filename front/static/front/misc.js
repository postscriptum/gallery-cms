$(document).ready(function() {
    $("#modalImage").on("hide.bs.modal", function() {
        $("#imageInfo").collapse("hide");
        $("#currentImage").css("opacity", 0);
    });
});


function showModalImage(ev, elem) {
    ev.preventDefault();
    var img_url = elem.getAttribute("data-url");
    document.getElementById("currentImage").setAttribute("src", img_url);
    $("#btnInfo").hide();
    if (elem.hasAttribute("data-img-name") || elem.hasAttribute("data-img-desc")) {
        var info = '';
        if (elem.hasAttribute("data-img-name"))
            info = '<h3>' + elem.getAttribute("data-img-name") + '</h3>';
        if (elem.hasAttribute("data-img-desc"))
            info += '<h5>' + elem.getAttribute("data-img-desc") + '</h5>';
        $("#imageInfo .panel-heading").html(info);
        $("#btnInfo").show();
    }
    $("#modalImage").modal();
}


function currentImageLoaded(img) {
    img.style.opacity = 1;
}
