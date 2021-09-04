import requests
from bs4 import BeautifulSoup

def getCovid():
    url = "https://nidss.cdc.gov.tw/PivotChart/ChartMap1988"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    block = soup.find("div", id="appendContainer").find("script").string

    index_s = block.find('[{')
    index_e = block.find(',"properties"')

    dataStr = block[index_s: index_e]

    import json
    data = json.loads(dataStr)

    location = list()
    people = list()

    for d in data:
        location.append(d['code'])
        people.append(d['value'])

    return location, people
