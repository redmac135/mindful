const moods = ['very sad', 'sad', 'neutral', 'happy', 'very happy'];
const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

function formatArray(arr) {
    arr = arr.map(word => word.toLowerCase());
    if (arr.length === 1) {
        return arr[0];
    }
    return arr.slice(0, -1).join(', ') + ' and ' + arr.slice(-1);
}

function formatDay(day) {
    var tmp = day.split('-');
    return `${months[parseInt(tmp[1]) - 1]} ${tmp[2]}, ${tmp[0]}`;
}

function getDetails(entry) {
    // fetch data from api
    var url = `/api/entries/${entry}`;
    fetch(url, {
        format: 'json'
    }).then(response =>
        response.json()
    ).then(data => {
        // fill modal with data
        var content = `On <i>${formatDay(data.date)}</i> I felt ${moods[data.feeling - 1]}.<br>I was ${formatArray(data.adjective)} because of ${formatArray(data.reason)}.`;
        $('#modal-text').html(content);
    }).catch(error => {
        $('#modal-text').html("An internal error occurred. Try again later.");
    });
    $("#modal").show();
    $('#modal-content').css('opacity', '0');
    $('#modal-content').animate({
        opacity: 1
    }, 100);
}

function hideModal() {
    $("#modal").hide();
}

$(window).click(function (event) {
    if (event.target.id === 'modal') {
        hideModal();
    }
});