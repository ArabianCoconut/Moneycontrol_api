const { type } = require('os');
const { stringify } = require('querystring');

// web scrapper using node.js
async function getWebData() {
    const puppeteer = require('puppeteer');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://www.moneycontrol.com/news/india/');

    for(let i = 1; i <= 24; i++) {
    // console.log(i);
    let li_count= '//*[@id="newslist-'+i+'"]';
    const [element] = await page.$x(li_count);
    let elementTxt = await (await element.getProperty('innerText')).jsonValue();
    elementTxt = String(elementTxt).split('\n')
    elementTxt = elementTxt.filter((item) => item != '' && item != '\n');
    elementTxt = elementTxt.slice(0, 3);
    console.log(elementTxt);
}
    browser.close();
}
getWebData();