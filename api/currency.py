import requests
import xml.etree.ElementTree as ET
url = "https://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=26/05/2024"

response = requests.get(url)
root = ET.fromstring(response.content)
name = root.attrib.get('Value')
USD_STR = root.find(f".//Valute[@ID='R01235']").find('Value').text
TRY_STR = root.find(f".//Valute[@ID='R01700J']").find('Value').text
EUR_STR = root.find(f".//Valute[@ID='R01239']").find('Value').text
USD = float(USD_STR.replace(',', '.'))
TRY = float(TRY_STR.replace(',', '.'))
EUR = float(EUR_STR.replace(',', '.'))
print(EUR, TRY)