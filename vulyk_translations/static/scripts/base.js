$(function () {
    var template = Handlebars.compile($('#judgeme_template').html()),
        output = $("#out"),
        answer_is_given = false;

    function serialize_form() {
        return{
            score: $('#score-slider').val()
        };
    }


    $(document.body).on("vulyk.next", function (e, data) {
        answer_is_given = false;
        $("#current-score").text("");
        $(".mark-errors strong").removeClass("text-danger");
        output.html(template(data.result.task.data));
        $('[data-toggle="tooltip"]').tooltip();

        $("#score-slider").change(function () {
            answer_is_given = true;
            $("#current-score").text($(this).val());
        });
    }).on("vulyk.save", function (e, callback) {
        if (answer_is_given) {
            callback(serialize_form());
        }
        else {
            $("a#save-button, a#skip-button").removeClass("disabled");
            $(".mark-errors strong").addClass("text-danger");
        }
    }).on("vulyk.skip", function (e, callback) {
        callback();
    });
});
