import requests

def getReser():
    url = "https://www.taiwanstat.com/waters/latest"

    res = requests.get(url)
    print(res.text)
    dataStr = res.text

    import json
    data = json.loads(dataStr)

    location = list()
    percentage = list()
    volumn = list()
    
    for d in data[0]:
        location.append(d)
        percentage.append(data[0][d]['percentage'])
        volumn.append(data[0][d]['volumn'])

    return location, percentage, volumn
