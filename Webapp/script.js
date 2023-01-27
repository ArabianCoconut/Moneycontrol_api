const url = [
"https://www.moneycontrol.com/news/",
"https://www.moneycontrol.com/news/business",
"https://www.moneycontrol.com/news/latest-news/",
"https://www.moneycontrol.com/news/india/"
]


// Web Api
 let data = fetch(url[3]).then((response) => response.text())

// filter title from html
let title = data.then((html) => {
    let parser = new DOMParser();
    let doc = parser.parseFromString(html, "text/html");
    let title = doc.querySelectorAll("h2");
     //skip empty date and limit to 24 items in array
    for(let element of title) {
        let title = {"title": element.innerText};
    
    //skip empty title and remove last 2 items
    if (title.title == "") {
        continue;
    };
    console.log(title.title);
};

});

let date = data.then((html) => {
    let parser = new DOMParser();
    let doc = parser.parseFromString(html, "text/html");
    let date = doc.querySelectorAll("li > span");
    //skip empty date and limit to 24 items
    for (const element of date) {
    const date = {"date": element.innerText};
    //skip empty date and filter words
    if (date.date == "") {
        continue;
    };
    console.log(date.date);
    };
});

let link = data.then((html) => {
    let parser = new DOMParser();
    let doc = parser.parseFromString(html, "text/html");
    let link = doc.querySelectorAll("a");
    for (const element of link) {
    const link = {"link": element.href};
    //skip empty link
    if (link.link == "") {
        continue;
    }
    // console.log(link.link);
    };
})

    
    