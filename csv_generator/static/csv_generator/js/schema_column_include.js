$(document).ready(() => {
    $("#add_column").click(function () {
        var $div = $('div[id^="schema_column_form"]:last');
        var num = parseInt($div.prop("id").match(/\d+/g), 10) + 1;
        var $klon = $div.clone().prop('id', 'schema_column_form' + num);
        $div.after($klon);
        $("[name=extra_field_count]").val(num);
    });
});
