$(document).ready(() => {
    $("#add_column").click(function () {
        // get the last DIV which ID starts with ^= "klon"
        var $div = $('div[id^="schema_column_form"]:last');
        // Read the Number from that DIV's ID (i.e: 3 from "klon3")
        // And increment that number by 1
        var num = parseInt($div.prop("id").match(/\d+/g), 10) + 1;
        // Clone it and assign the new ID (i.e: from num 4 to ID "klon4")
        var $klon = $div.clone().prop('id', 'schema_column_form' + num);
        // Finally insert $klon wherever you want
        $div.after($klon);
        $("[name=extra_field_count]").val(num);
    });
});
