$(document).ready(() => {
    $("#add_column").click(function () {
        let form_idx = $('#id_schemacolumn_set-TOTAL_FORMS').val();
        console.log(form_idx, "Hello, world!");
        let $div = $('div[id^="schema_column_form"]:last');
        let num = parseInt($div.prop("id").match(/\d+/g), 10) + 1;
        let $klon = $div.clone().prop('id', 'schema_column_form' + num);
        $div.after($klon);
        $("[name=extra_field_count]").val(num);
        let new_value = parseInt(form_idx) + 1
        $('#id_schemacolumn_set-TOTAL_FORMS').prop("value", new_value);
    });
});
