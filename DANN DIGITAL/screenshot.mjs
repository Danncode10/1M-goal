import puppeteer from 'puppeteer';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, 'cover.html');

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.setViewport({ width: 1640, height: 624, deviceScaleFactor: 1 });
await page.goto(`file://${htmlPath}`);
await new Promise(r => setTimeout(r, 500));
await page.screenshot({ path: path.join(__dirname, 'cover.png'), type: 'png' });
await browser.close();
console.log('Done! cover.png saved.');
