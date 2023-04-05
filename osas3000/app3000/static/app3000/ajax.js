$(document).ready(function(){
    $(".send-button").click(function(){
        $.ajax({
            url: $("#url").val(),
            type:"post",
            data: {
                csrfmiddlewaretoken: $("#csrf").val(),
                "name":$(".input-name").val(),
                "review":$(".input-review").val(),
            },
            success: function(response){
                
            }
        });
    });
});
