$(document).ready(() => {
    $("#add_column").click(function () {
        let form_idx = $('#id_schemacolumn_set-TOTAL_FORMS').val();
        let $div = $('div[id^="schema_column_form_"]:last');
        let num = parseInt(form_idx) - 1;
        let $klon = $div.clone().prop('id', 'schema_column_form_' + num + "_new");
        $klon.find("div #id_schemacolumn_set-" + num + "-DELETE").attr({
            name: "schemacolumn_set-" + form_idx + "-name",
            id: "id_schemacolumn_set-" + form_idx + "-name",
        });
        $klon.find("#id_schemacolumn_set-" + num + "-id").attr({
            name: "schemacolumn_set-" + form_idx + "-id",
            id: "id_schemacolumn_set-" + form_idx + "-id",
        });
        $klon.find("div #id_schemacolumn_set-" + num + "-name").attr({
            name: "schemacolumn_set-" + form_idx + "-name",
            id: "id_schemacolumn_set-" + form_idx + "-name",
            value: "",
        });
        $klon.find("div #id_schemacolumn_set-" + num + "-type").attr({
            name: "schemacolumn_set-" + form_idx + "-type",
            id: "id_schemacolumn_set-" + form_idx + "-type",
            value: "",
        });
        $klon.find("div #id_schemacolumn_set-" + num + "-from_field").attr({
            name: "schemacolumn_set-" + form_idx + "-from_field",
            id: "id_schemacolumn_set-" + form_idx + "-from_field",
            value: "",
        });
        $klon.find("div #id_schemacolumn_set-" + num + "-to_field").attr({
            name: "schemacolumn_set-" + form_idx + "-to_field",
            id: "id_schemacolumn_set-" + form_idx + "-to_field",
            value: "",
        });
        $klon.find("div #id_schemacolumn_set-" + num + "-order").attr({
            name: "schemacolumn_set-" + form_idx + "-order",
            id: "id_schemacolumn_set-" + form_idx + "-order",
            value: form_idx,
        });
        $div.after($klon);
        let new_value = parseInt(form_idx) + 1
        $('#id_schemacolumn_set-TOTAL_FORMS').prop("value", new_value);
    });
    // delete the schema column
    $("#schema-column").on("click", "button", function () {
        let $del_element = $(this).parent().parent().first();
        let $del_checkbox = $del_element.find("input[type=checkbox]").prop('checked', true);
        let $del_id_field = $del_element.find("input[type=hidden]")
        if ($del_element.attr("id").split("_")[4] != 'new') {
            $del_element.after($del_checkbox.prop('hidden', true));
            $del_element.after($del_id_field);
        } else {
            let total_value = parseInt($('#id_schemacolumn_set-TOTAL_FORMS').val()) - 1;
            $('#id_schemacolumn_set-TOTAL_FORMS').prop("value", total_value);

        };
        $del_element.remove();
    });
});
