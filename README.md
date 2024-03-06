# Amazon Price Tracker

## Overview
Amazon Price Tracker is a Python script that monitors the price of a specified product on Amazon. If the price drops below a set threshold, it sends notifications via WhatsApp and email. This project is a handy tool for catching great deals on your favorite products.

## Features
- Web scraping with BeautifulSoup to extract product price information from Amazon.
- Integration with Twilio API for sending WhatsApp notifications.
- Utilizes SMTP for sending email notifications.

## Dependencies
- Python 3.x
- [Requests](https://docs.python-requests.org/en/latest/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Twilio Python](https://www.twilio.com/docs/libraries/python)
- [Twilio Account SID and Auth Token](https://www.twilio.com/docs/iam/api-keys)
- [SMTP (Simple Mail Transfer Protocol)](https://docs.python.org/3/library/smtplib.html)
- [Gmail Account for sending emails](https://support.google.com/mail/answer/185833?hl=en)

## Setup
1. Install the required dependencies: `pip install -r requirements.txt`
2. Update the following variables in the script:
    - `account_sid`: Your Twilio Account SID.
    - `auth_token`: Your Twilio Auth Token.
    - `my_twilio_num`: Your Twilio phone number.
    - `product_min_price`: Set the minimum price threshold.
    - `product_link`: The URL of the Amazon product.
    - `header`: User-Agent and Accept-Language for the HTTP request.

## Usage
Run the script using Python:

```bash
python main.py
```

## Contributors
- Nikhil Telase
- [Angela Yu](https://www.appbrewery.co/)

## Acknowledgments
Special thanks to Angela Yu, the instructor of [100DaysOfCode](https://www.appbrewery.co/p/100-days-of-code), for her guidance and teaching.
