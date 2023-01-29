const html_parser = "html.parser";
const title_text = "Title:";
const link_text = "Link:";
const date_text = "Date:";
const news_type = "News Type:";

const urls = [
  "https://www.moneycontrol.com/news",
  "https://www.moneycontrol.com/news/business",
  "https://www.moneycontrol.com/news/latest-news/"
];

async function getNews() {
  const url = urls[0];
  const response = await fetch(url);
  const data = await response.text();
  const parser = new DOMParser();
  const htmlDoc = parser.parseFromString(data, "text/html");
  const related_des_class = htmlDoc.querySelectorAll("h3.related_des");
  const related_date_class = htmlDoc.querySelectorAll("p.related_date.hide-mob");
  for (let i = 0; i < related_des_class.length; i++) {
    const title = related_des_class[i].querySelector("a").getAttribute("title");
    const link = related_des_class[i].querySelector("a").getAttribute("href");
    const date = related_date_class[i].textContent;
    const json_data = {
      [news_type]: "News",
      [title_text]: title,
      [link_text]: link,
      [date_text]: date
    };
    return document.getElementById("demo_out").innerHTML = JSON.stringify(json_data, null, 2);
  }
};

async function getBusinessNews() {
    const url = urls[1];
    const response = await fetch(url);
    const data = await response.text();
    const parser = new DOMParser();
    const htmlDoc = parser.parseFromString(data, "text/html");
    for (let i = 1; i < 24; i++) {
    const newList = "newslist-" + i;
    const newsList = htmlDoc.querySelector(
    `li.clearfix[id="${newList}"]`
    );
    const newsListHeading2 = htmlDoc.querySelector("h1.fleft");
    if (newsList) {
    const titleClass = newsList.querySelector("h2 > a");
    const title = titleClass.getAttribute("title");
    const link = titleClass.getAttribute("href");
    const dateClass = newsList.querySelector("span");
    const date = dateClass.textContent;
    const jsonData = {
    [news_type]: newsListHeading2.textContent,
    [title_text]: title,
    [link_text]: link,
    [date_text]: date
    };
    return document.getElementById("demo_out").innerHTML = JSON.stringify(jsonData, null, 2);
    } else {
    console.log(`li element with class 'clearfix' and id '${newList}' not found.`);
    return null;
    }
}
};
    

async function getLatestNews() {
    const response = await fetch(urls[2]);
    const html = await response.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, "text/html");
    const relatedDesClass = doc.querySelectorAll("h3.related_des");
    const relatedDateClass = doc.querySelectorAll("p.related_date.hide-mob");

    for (let i = 0; i < relatedDesClass.length; i++) {
        const h3Tag = relatedDesClass[i];
        const pTag = relatedDateClass[i];
        const title = h3Tag.querySelector("a").getAttribute("title");
        const link = h3Tag.querySelector("a").getAttribute("href");
        const date = pTag.textContent;
        const news = {
            [news_type]: "Latest News",
            [title_text]: title,
            [link_text]: link,
            [date_text]: date
        };
    return document.getElementById("demo_out").innerHTML = JSON.stringify(news, null, 2);
    }
};


function select(){
    const news = document.getElementById("api").value;
    if(news == "NApi"){
        getNews();
    }else if(news == "BApi"){
        getBusinessNews();
    }else if(news == "LApi"){
        getLatestNews();
    }
    else{
        document.getElementById("demo_out").innerHTML = "Please Select Any One Api";
    }
};

function clearDemoOut(){
    let element = document.getElementById("demo_out");
    element.innerHTML = " ";
}

async function copyDemoOut() {
    const copyText = document.getElementById("demo_out");
    try {
      await navigator.clipboard.writeText(copyText.value);
      copyText.innerHTML = "Copied text!";
    } catch (error) {
      console.error("Failed to copy text: ", error);
    }
  }
  
  

