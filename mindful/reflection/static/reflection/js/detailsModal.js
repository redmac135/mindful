const moods = ["very sad", "sad", "neutral", "happy", "very happy"];
const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
];

let url;

function formatArray(arr) {
    arr = arr.map((word) => word.toLowerCase());
    if (arr.length === 1) {
        return arr[0];
    }
    return arr.slice(0, -1).join(", ") + " and " + arr.slice(-1);
}

function formatDay(day) {
    let tmp = day.split("-");
    return `${months[parseInt(tmp[1]) - 1]} ${tmp[2]}, ${tmp[0]}`;
}

function getDetails(entry) {
    // fetch data from api
    url = `/api/entries/${entry}`;
    fetch(url, {
        format: "json",
    })
        .then((response) => response.json())
        .then((data) => {
            // fill modal with data
            let content = `On <i>${formatDay(data.date)}</i> I felt ${
                moods[data.feeling - 1]
            }.<br>I was ${formatArray(data.adjective)} because of ${formatArray(
                data.reason
            )}.<br><input type="submit" onclick="showDeleteConfirmation()" value="Delete" class="btn-pink mt-3 -mb-1">`;
            $("#modal-text").html(content);
        })
        .catch((error) => {
            $("#modal-text").html(
                "An internal error occurred. Try again later."
            );
        });
    $("#modal-del").hide();
    $("#modal").show();
    $("#modal-content").css("opacity", "0");
    $("#modal-content").animate(
        {
            opacity: 1,
        },
        100
    );
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = jQuery.trim(cookie);
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function showDeleteConfirmation() {
    $("#modal-content").addClass("rounded-b-none");
    $("#modal-del").slideDown("fast");
}

function confirmDelete() {
    deleteEntry();
    hideModal();
}

function cancelDelete() {
    $("#modal-content").removeClass("rounded-b-none");
    $("#modal-del").slideUp("fast");
}

function deleteEntry() {
    //console.log("DELETEEE");
    fetch(url, {
        method: "delete",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
        },
    });
}

function hideModal() {
    $("#modal").hide();
}

$(window).click(function (event) {
    if (event.target.id === "modal") {
        hideModal();
    }
});
