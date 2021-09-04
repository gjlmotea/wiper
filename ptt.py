import requests

from bs4 import BeautifulSoup

def getPtt():
    payload = {'from':'/bbs/Gossiping/index.html','yes':'yes'}
    rs = requests.session()
    res = rs.post('https://www.ptt.cc/ask/over18', data=payload)
    res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html')
    dom = BeautifulSoup(res.text, 'html.parser')

    text = ""
    for ele in dom.select('.r-ent'):
        text += ele.select('.date')[0].text +":" + ele.select('.author')[0].text + " " + ele.select('.title a')[0].text + "\n"
    return text
