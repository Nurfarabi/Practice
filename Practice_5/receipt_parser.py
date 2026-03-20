import re 
import json 

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

prices = re.findall("\d[\d ]*,\d{2}", text)

products = re.findall("\d+\.\s*\n(.+)", text)

clean_prices = [p.replace(" ", "").replace(",", ".") for p in prices]
prices_float = [float(p) for p in clean_prices]

total_match = re.search("ИТОГО:\s*([\d\s]+,\d{2})", text)
total = total_match.group(1) if total_match else None

datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}", text)
datetime = datetime_match.group() if datetime_match else None

payment = re.search(r"(Банковская карта|Наличные)", text)
payment_method = payment.group() if payment else None

data = {
    "Products" : products,
    "Prices" : prices_float,
    "Datetime" : datetime,
    "Payment Method" : payment_method
}

print(json.dumps(data, indent=4, ensure_ascii=False))