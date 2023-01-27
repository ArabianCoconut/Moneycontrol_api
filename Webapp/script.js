const url = [
"https://www.moneycontrol.com/news/news-all/",
"https://www.moneycontrol.com/news/business",
"https://www.moneycontrol.com/news/latest-news/"

]


// Web Api

onload = function getNews() {
    fetch(url[0])
    .then(response => response.text().title())
    .then(data => document.getElementById("test").innerHTML = data);
    console.log(data);
}