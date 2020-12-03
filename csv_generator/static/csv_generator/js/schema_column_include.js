$(document).ready(() => {
    $("#add_column").click(function () {
        let form_idx = $('#id_schemacolumn_set-TOTAL_FORMS').val();
        let $div = $('div[id^="schema_column_form_"]:last');
        let num = parseInt($div.prop("id").match(/\d+/g), 10) + 1;
        let $klon = $div.clone().prop('id', 'schema_column_form_' + num);
        $klon.find("div #id_schemacolumn_set-0-name").prop("name", "schemacolumn_set-" + num + "-name")
        $klon.find("div #id_schemacolumn_set-0-name").prop("value", "")
        $klon.find("div #id_schemacolumn_set-0-type").prop("name", "schemacolumn_set-" + num + "-type")
        $klon.find("div #id_schemacolumn_set-0-from_field").prop("name", "schemacolumn_set-" + num + "-from_field")
        $klon.find("div #id_schemacolumn_set-0-from_field").prop("value", "")
        $klon.find("div #id_schemacolumn_set-0-to_field").prop("name", "schemacolumn_set-" + num + "-to_field")
        $klon.find("div #id_schemacolumn_set-0-to_field").prop("value", "")
        $klon.find("div #id_schemacolumn_set-0-order").prop("name", "schemacolumn_set-" + num + "-order")
        $klon.find("div #id_schemacolumn_set-0-order").prop("value", "")
        $div.after($klon);
        $("[name=extra_field_count]").val(num);
        let new_value = parseInt(form_idx) + 1
        $('#id_schemacolumn_set-TOTAL_FORMS').prop("value", new_value);
    });
});
