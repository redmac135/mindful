let selected_types = new Set();

function filterResources(element) {
    if (element.checked) {
        selected_types.add(element.id);
    } else {
        selected_types.delete(element.id);
    }

    let cnt = 0;
    if (selected_types.size === 0) {
        $("#resource-list div").show();
        cnt = $("#resource-list div").length;
    } else {
        $("#resource-list div").hide();
        $("#resource-list div").each(function () {
            if (selected_types.has($(this).attr("id"))) {
                $(this).show();
                cnt++;
            }
        });
    }

    $("#resource-cnt").text(`${cnt} resource${cnt === 1 ? "" : "s"} found`);
}

function toggleFilters() {
    $("#sm-filters").toggle("fast");
}
