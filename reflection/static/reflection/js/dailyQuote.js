async function getQuote() {
    // check cache if api has been requested within the last x miliseconds
    const hours = 6;
    const x = hours * 60 * 60 * 1000;
    const now = Date.now();
    var quoteJson;
    const url = "https://zenquotes.io/api/random";

    if (localStorage.getItem("quote") && localStorage.getItem("quoteTime") && (now - localStorage.getItem("quoteTime")) < x) {
        quoteJson = JSON.parse(localStorage.getItem("quote"));
    } else {
        quoteJson = await fetch(url).then(
            (response) => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error("Error fetching quote");
                }
            }
        ).catch(error => {
            return [{
                "q": "In the beginning there was nothing, and nothing was nothing.",
                "a": "Unknown"
            }];
        });
        localStorage.setItem("quote", JSON.stringify(quoteJson));
        localStorage.setItem("quoteTime", now);
    }
}

// set the daily quote
$(document).ready(function () {
    getQuote().then(() => {
        const quote = JSON.parse(localStorage.getItem("quote"));
        console.log(quote[0]);
        $("#quote-text").html(`"${quote[0].q}"`);
        $("#quote-author").html(`- ${quote[0].a}`);
    });
});
