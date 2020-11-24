import pymysql
import requests
import urllib
from bs4 import BeautifulSoup, UnicodeDammit
def characterGet(start_url):
    global threads
    global count
    try:
        url = 'http://xh.5156edu.com/wx/jin.html'
        res = requests.get(url)
        res.encoding = 'gbk'
        print(res.status_code)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all('a', {"class": "fontbox2"})
        character = []
        pinyin = []
        for link in links:
            character.append(link.get_text())
            pinyin.append(link.get_text()[1:])
        save(character, pinyin)
    except Exception as err:
        print(err)
def save(character, pinyin):

    db = pymysql.connect("localhost", "root", "707615", "mysql")
    cursor = db.cursor()
    len_character = len(character)
    I = 0
    while (I < len_character):
        sql = "insert into pachong values(' " + character[I][0] + " ',' " + pinyin[I].replace(",", " ") + " ',CURRENT_TIMESTAMP);"
        I += 1
        if (I == 39):
            break
        cursor.execute(sql)
    db.commit()
    cursor.close()
characterGet("http://xh.5156edu.com/wx/jin.html")