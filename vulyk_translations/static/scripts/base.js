$(function () {
    var template = Handlebars.compile($('#judgeme_template').html()),
        output = $("#out"),
        answer_is_given = false;

    function serialize_form() {
        return{
            score: $('#score-slider').prop('disabled') ? null : $('#score-slider').val(),
            inappropriate: $('#inappropriate').prop('checked'),
            garbled: $('#garbled').prop('checked')
        };
    }


    $(document.body).on("vulyk.next", function (e, data) {
        answer_is_given = false;
        $(".mark-errors strong").removeClass("text-danger");
        output.html(template(data.result.task.data));
        $('[data-toggle="tooltip"]').tooltip();

        $('#inappropriate, #garbled').change(function () {
            if ($('#inappropriate').prop('checked') || $('#garbled').prop('checked')) {
                $('#score-slider').prop('disabled', true);
            } else {
                $('#score-slider').prop('disabled', false);
            }
        });

        $("#score-slider").change(function () {
            answer_is_given = true;
        });

        // Hotkey for inappropriate checkbox
        key("i", function () { $("#inappropriate").click(); });

        // Hotkeys for detailed feedback checkboxes
        key("g", function () { $("#garbled").click(); });
    }).on("vulyk.save", function (e, callback) {
        if (answer_is_given || $('#inappropriate').prop('checked') || $('#garbled').prop('checked')) {
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
