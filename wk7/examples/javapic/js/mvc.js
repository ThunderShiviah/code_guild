; // Defensive semicolon

"use strict";

function MVC () {

    var Photo = {
    	defaults: {
    		src: "./images/pdxcg_01.jpg" // Why does a ; break here?
        },

        setPhotos () {
            var num;
            var x;
            var photos = [];

            for (x = 1; x < 61; x++) {  // 60 image available (more or less)
                num = x.toString();
                if (num.length < 2) {
                    num = "0" + num;
                }
                photos[x] = "images/pdxcg_" + num + ".jpg";

            }
            return photos;
        }

    }
    

    var Controller =  { 
    	getFileNames(Photo) {
            console.log("this equals", this);
            fileNames = Photo.setPhotos();
            return fileNames;
        },

        handleEvent (e) {
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
        }
    }

    var View = {
        setView (Controller, Photo) {
            var fileNames = Controller.getFileNames(Photo);
            var num;
            var x;
        

            for (x = 1; x < fileNames.length; x++) {
                $(".gallery").append("<li><img src=" + fileNames[x] + " /></li>");
            }
        },
     
        listenForClick () {
            $(".gallery").click(Controller.handleEvent);
            $("li img").attr("class", "picture")
            .attr("onerror", "src = 'images/pdxcg_01.jpg'");

        }
    }

    View.setView(Controller, Photo);
    View.listenForClick();

}

MVC();