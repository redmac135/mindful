function expand(num) {
    $('#arrow' + num).addClass('rotate-90');
    $('#answer' + num).slideDown('fast');
}

function collapse(num) {
    $('#arrow' + num).removeClass('rotate-90');
    $('#answer' + num).slideUp('fast');
}

function toggleAnswer(questionNum) {
    if ($('#answer' + questionNum).is(':hidden')) {
        expand(questionNum);
    } else {
        collapse(questionNum);
    }
}

let expanded = false;
function toggleAll() {
    for (let i = 1; ; i++) {
        if ($('#answer' + i).length == 0) {
            break;
        }
        if (expanded) {
            collapse(i);
        } else {
            expand(i);
        }
    }
    expanded = !expanded;
}