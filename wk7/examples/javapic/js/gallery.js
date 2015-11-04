;  // Defense, yo.

function wrapper() {

    var num;
    var x;
    var sentName = window.location.search.substr(1);

    if (sentName) {
        $(".tagline").text(sentName + ", develop something beautiful");
    }

    for (x = 1; x < 61; x++) {  // 60 image available (more or less)
        num = x.toString();
        if (num.length < 2) {
            num = "0" + num;
        }
        var fileName = "images/pdxcg_" + num + ".jpg";
        $(".gallery").append("<li><img src=" + fileName + " /></li>");
        $("li img").attr("class", "picture")
                   .attr("onerror", "src = 'images/pdxcg_01.jpg'");

    }

    $(".gallery").click(function(e) {
        var clickedImg = e.target;

        // Check to see if click was on a picture.
        if (clickedImg.className === "picture") {
            var imShow = $("#image_show");
            imShow.children().first().attr('src', clickedImg.src);
            imShow.attr('class', 'display_img');
            imShow.click(function(f) {

                // Check to see if second click was outside blown up picture
                if (f.target !== imShow.children().first()[0]) {
                   imShow.attr('class', 'display_none');
                }
            });
        }
    });

}

wrapper();