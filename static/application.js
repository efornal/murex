$(function() {

    // $("#select_provider").change(function(){
    //     $.ajax({
    //         type: "POST",
    //         url: "/es/toners/filtrar",
    //         data: {'provider': 1, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
    //            dataType: "json",
    //         success: function(response) {
    //             if ( response.exists ) {
    //                 alert("ok");
    //             } else {
    //                 alert("ok mm");
    //            }
    //         },
    //         error: function(rs, e) {
    //             alert("error");
    //         }
    //     }); 
    // });

    // $("#select_state").change(function(){
    //     $.ajax({
    //         type: "POST",
    //         url: "/es/toners/filtrar",
    //         data: {'state': 1, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
    //         dataType: "json",
    //         success: function(response) {
    //             if ( response.exists ) {
    //                 alert("ok");
    //             } else {
    //                 alert("ok mm");
    //            }
    //         },
    //         error: function(rs, e) {
    //             alert("error");
    //         }
    //     }); 
    // });
    $(function(){
        $("#select_state").change(function(){
            this.form.submit();
        });
    });

    $(function(){
        $("#select_provider").change(function(){
            this.form.submit();
        });
    });

});
