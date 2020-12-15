$(document).ready(() => {
    // add the schema column
    $("#add_column").click(function () {
        let form_idx = $('#id_schemacolumn_set-TOTAL_FORMS').val();
        let $div = $('div[id="empty_formset"]');
        let $klon = $div.clone().html().replace(/__prefix__/g, form_idx);
        let new_value = parseInt(form_idx) + 1;
        $('#id_schemacolumn_set-TOTAL_FORMS').prop("value", new_value);
        $('#endform').before($klon);
        $("#schema-column").find("input[id$='-order']:last").prop('value', new_value);
   });

    // delete the schema column
    $("#schema-column").on("click", "button", function () {
        let $del_element = $(this).parent().parent().first();
        let $del_checkbox = $del_element.find("input[type=checkbox]").prop('checked', true);
        let $del_id_field = $del_element.find("input[type=hidden]")
        $del_element.after($del_checkbox.prop('hidden', true));
        $del_element.after($del_id_field);
        $del_element.remove();
    });

    // add 'from' & 'to' fields
    $("#schema-column").on("change", "select", function () {
        if ($(this).children("option:selected").val() == 'Integer') {
            $(this).parent().next().show();
            $(this).parent().next().next().show();
        } else {
            $(this).parent().next().hide();
            $(this).parent().next().next().hide();
        }
    });
});

