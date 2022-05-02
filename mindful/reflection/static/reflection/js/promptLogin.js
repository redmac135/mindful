function promptLoginModal() {
    $("#login-modal").show();
}

function hideLoginModal() {
    $("#login-modal").hide();
}

$(window).click(function (event) {
    if (event.target.id === "modal-content") {
        hideLoginModal();
    }
});