/**
 * Created by bonult on 2015/11/26.
 */
/**
 * Created by bonult on 2015/11/25.
 */
$(document).ready(function () {
    $(window).on("load", function () {

        imgLocation1();
		imgLocation();
    });
});


function imgLocation() {
    var box = $(".site");
    var boxWidth = box.eq(0).width();
    var num = Math.floor($("#sites").width() / boxWidth);
    var boxArr = [];
    box.each(function (index, value) {
        var boxHeight = box.eq(index).height();
        if (index < num) {
            boxArr[index] = boxHeight;
        } else {
            var minboxHeight = Math.min.apply(null, boxArr);
            var minboxIndex = $.inArray(minboxHeight, boxArr);
            var mbh =Math.max.apply(null, boxArr);

            $("body").css("height", 100 + mbh + "px");
            $(value).css({
                "position": "absolute",
                "top": minboxHeight,
                "left": box.eq(minboxIndex).position().left
            });
            boxArr[minboxIndex] += box.eq(index).height();
        }
    });
}

function imgLocation1() {
    var box = $(".site");
    var boxWidth = box.eq(0).width();
    var num = Math.floor($("#sites").width() / boxWidth);
    var boxArr = [];
    box.each(function (index, value) {
        var boxHeight = box.eq(index).height();
        if (index < num) {
            boxArr[index] = boxHeight;
            var leftt = index * boxWidth;
            var lefttt = leftt + "px";
            $(value).css({
                "position": "absolute",
                "top": "-5px",
                "left": lefttt
            });
        } else {
            var minboxHeight = Math.min.apply(null, boxArr);
            var mbh =Math.max.apply(null, boxArr);
            var minboxIndex = $.inArray(minboxHeight, boxArr);

            $(value).css({
                "position": "absolute",
                "top": minboxHeight,
                "left": box.eq(minboxIndex).position().left
            });
            boxArr[minboxIndex] += box.eq(index).height();
        }
    });
}



//屏蔽右键菜单
/*
 document.oncontextmenu = function (event){
 if(window.event){
 event = window.event;
 }try{
 var the = event.srcElement;
 if (!((the.tagName == "INPUT" && the.type.toLowerCase() == "text") || the.tagName == "TEXTAREA")){
 return false;
 }
 return true;
 }catch (e){
 return false;
 }
 }
 */