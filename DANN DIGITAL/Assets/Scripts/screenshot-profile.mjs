import puppeteer from 'puppeteer';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, 'profile.html');

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.setViewport({ width: 800, height: 800, deviceScaleFactor: 2 });
await page.goto(`file://${htmlPath}`);
await new Promise(r => setTimeout(r, 500));
await page.screenshot({ path: path.join(__dirname, 'profile.png'), type: 'png' });
await browser.close();
console.log('Done! profile.png saved.');
