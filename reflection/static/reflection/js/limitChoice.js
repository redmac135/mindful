$(document).ready(function () {
	$("#id_reason :input").change(function (event) {
		if ($("#id_reason :input:checked").length > 3) {
			this.checked = false;
			this.nextElementSibling.classList.add("apply-shake");
			this.nextElementSibling.addEventListener("animationend", finishAnimation)
		}
	});
	$("#id_adjective :input").change(function (event) {
		if ($("#id_adjective :input:checked").length > 3) {
			this.checked = false;
			this.nextElementSibling.classList.add("apply-shake");
			this.nextElementSibling.addEventListener("animationend", finishAnimation)
		}
	});
	function finishAnimation() {
		this.classList.remove("apply-shake")
	}
});