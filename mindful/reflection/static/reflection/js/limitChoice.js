function checkChild(element, form_type) {
    let child = $(element).children("input")[0];
    child.checked = !child.checked;
    if (child.checked) {
		if ($(`input[name=${form_type}]:checked`).length > 3) {
			$(child).prop("checked", false);
            $(element).addClass("animate-shake");
            $(element).on("animationend", finishAnimation);
        } else {
			$(element).removeClass("shadow-md");
			$(element).addClass("scale-95");
			$(element).addClass("bg-clr-accent-1");
		}
    } else {
		$(element).addClass("shadow-md");
		$(element).removeClass("scale-95");
		$(element).removeClass("bg-clr-accent-1");
	}
}

function finishAnimation() {
    $(this).removeClass("animate-shake");
}
