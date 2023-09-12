# Yandex Go Android Price Scraper

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

> **Disclaimer**: This project is for educational purposes only. Please respect GDPR regulations, in particular, [Article 8 of the Charter of Fundamental Rights of the European Union](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:12012P/TXT&from=EN).

---

## Overview

This Python, Appium, and ADB project is designed to scrape pricing data from the Yandex Go Android ridesharing application. It allows you to extract ride prices for various cities and routes. Simply provide the addresses in the configuration files, and the bot will take care of the rest.

The project strictly adheres to SOLID principles and utilizes the Page Object Model (POM) design pattern.

---

## Configuration

To set up and configure the scraper, follow these steps:

1. **Google Sheets Integration**: Edit `/config/gsheetserviceacc/ServiceAccountToken.json` to integrate with Google Sheets.

2. **Route Configuration**: Edit `/config/routes/*.json` to define proper route origin-destination pairs as input to the app.

3. **Appium Configuration**: Edit `/config/sys/driver.json` to configure Appium desired capabilities, host:port settings, Android package name, Google Sheet ID, Google Sheet name, and the path to an internal local database for tracking the process's last state.

---

## Usage

You can run this scraper on an Android virtual device or a real Android device with USB debugging enabled.

### Execute the Scraper

Use `main.py` as the entry point for the data scraper bot. Pass a command-line argument to select a city route configuration.

```bash
python3 main.py <arg -t=TBLISI / -b=BATUMI / -k=KUTAISI>
```

### Continuous Execution

If you want to run the Python script infinitely with the same command-line arguments, use `infinite.py`.

---

## Installation

1. Clone this repository to your local machine.
2. Install the specific APK version of the Yandex Go Android application to your Android OS device from the `/apk` folder.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to contribute to the project, report issues, or suggest improvements. Happy scraping! :rocket:
