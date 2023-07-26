console.log("Hello, world!")

// var https = require('follow-redirects').https;
// var fs = require('fs');

const axios = require('axios');
const cheerio = require('cheerio');

const puppeteer = require('puppeteer');

(async () => {
  try {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    page.setJavaScriptEnabled(true);
    await page.goto('https://www.ticketmaster.com.br/event/aespa');
    await page.waitForSelector('#picker-bar > div > div', { timeout: 500 });

    console.log("foi 1")

    var selectors = await page.$x("//button[contains(text(),'Reject')]")

    // var selectors = await page.$x("//div[@class='next']")
    console.log(selectors)

    // await Promise.all([selectors[0].click(), page.waitForNavigation()]);
    await selectors[0].click()
    console.log("foi 2")
    await new Promise(r => setTimeout(r, 1000));


    var selectors = await page.$x("//div[@class='next']")
    console.log(selectors)
    await selectors[0].click()
    console.log("foi 3")
    await new Promise(r => setTimeout(r, 1000));


    var selectors = await page.$x("//div[@class='festival-selection']")
    console.log(selectors)
    await selectors[0].click()
    console.log("foi 4")
    await new Promise(r => setTimeout(r, 1000));


    var selectors = await page.$x("(//h3[normalize-space()='Pista Premium'])/parent::div")
    console.log(selectors)
    console.log("foi 5")
    await new Promise(r => setTimeout(r, 1000));

    
    var selectors = await selectors[0].evaluate("(//strong[contains(text(),'Meia-Entrada')])/parent::div/parent::div")
    console.log(selectors)
    console.log("foi 6")
    await new Promise(r => setTimeout(r, 1000));
    
    
    // selectors = await page.$x('//a[contains(text(), "Suporte ao Fã")]')
    // console.log(selectors)

    // await selectors[0].click()
    // await page.waitForNavigation()


    // await selectors[0].click()
    // console.log("foi 3")

    // const buttonClick = await page.$('#user_data > div > a:nth-child(3)');

    // await buttonClick.click();
    

    // await page.waitForXPath('//div[contains(text(), "Selecionar ingressos")]')

    // console.log("foi 3")

    // await page.waitForSelector('#checkout-actions > h1', { timeout: 500 })

    // await page.click('#ingresar', {timeout: 500});
    // await page.waitForNavigation();
    // await page.waitForSelector('.festival-selection', { timeout: 500 });

    await page.screenshot({ path: "/Users/marianabianca/Documents/aespa/screenshot.png", type: "png" })
    console.log('See screenshot')



    const body = await page.evaluate(() => {
      return document.querySelector('body').innerHTML;
    });
    console.log(body);

    await browser.close();
  } catch (error) {
    console.log(error);
  }
})();

// (async () => {
//   try {
//     const response = await axios.get('https://www.ticketmaster.com.br/event/aespa');
//     const $ = cheerio.load(response.data);

//     console.log($('body').html());
//   } catch (error) {
//     console.log(error);
//   }
// })();

// var options = {
//   'method': 'GET',
//   'hostname': 'www.ticketmaster.com.br',
//   'path': '/event/aespa',
//   'headers': {
//   },
//   'maxRedirects': 20
// };

// var req = https.request(options, function (res) {
//   var chunks = [];

//   res.on("data", function (chunk) {
//     chunks.push(chunk);
//   });

//   res.on("end", function (chunk) {
//     var body = Buffer.concat(chunks);
//     console.log(body.toString());
//   });

//   res.on("error", function (error) {
//     console.error(error);
//   });
// });

// req.end();