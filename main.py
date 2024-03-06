import requests
import smtplib
from bs4 import BeautifulSoup
from twilio.rest import Client
# api details
account_sid = "ACc16699c2e3ccdf2980f17498ecafa82d"
auth_token = "b68ccfb12f8221e92e3eaed8791edce1"
my_twilio_num = "+16592667763"

# product details
product_min_price = 1500
product_link = "https://www.amazon.in/Noise-Wireless-Earbuds-Playtime-Instacharge/dp/B0C7L4MY51/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.ab6ef955-1bde-4b05-b15e-b208c97a1fdb&dib=eyJ2IjoiMSJ9.5pesQeEJkNDuVPugHB_MfnYrkjgnlHslK9ZNkL1dN-4aTIefbeRrTebH_76i0snMx4buewjVYKLxampu6UBrpC_Cn84EJ1cyuZZhFeDPmINMH5MS_tM3dsYycJqSLyDDBWdy3aeakclERjWCkgYLMyrrDQ8cKG82pnXMIFYc3MMPy20ar2C0Xu1VVs6JZlRo.V6rKfFsX1gBIkgWhhgzH3rqh3OwOIIw79Mn326AcUy8&dib_tag=se&pd_rd_r=16e51069-4215-4dca-878e-7c81f4e95e93&pd_rd_w=wZikr&pd_rd_wg=lCexM&pf_rd_p=ab6ef955-1bde-4b05-b15e-b208c97a1fdb&pf_rd_r=EQ94WJFJ038Y86MRR2NT&qid=1709027310&sr=8-2"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en,hi;q=0.9"
}
# scraping price data
response = requests.get(product_link, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
product_price = soup.find(name="span", class_="a-price-whole").getText()
# remove clutter from price
product_price_int = int(product_price.replace(",", "").replace(".", ""))
print("Product current price is :", product_price_int)

if product_price_int <= product_min_price:
    # sending WhatsApp message
    price_message = f'The price of your product is {product_price_int}\nBuy now>>> {product_link}'
    client = Client(account_sid, auth_token)

    whatsapp_message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=price_message,
        to='whatsapp:+918305230871'
    )
    print("I send a message you")

    # sending mail
    my_email = "nikhiltelase17@gmail.com"
    password = "exmnjdjmcoodvhpm"
    to_mail = "nikhiltelase@gmail.com"
    mail_message = f"Subject: Motivational Quotes \n\n{price_message}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # seure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=[to_mail],
                            msg=mail_message)
    print("I send a mail you")
else:
    print(f"Price is not less than your set price: {product_min_price}")

