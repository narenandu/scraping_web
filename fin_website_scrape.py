
import bs4
import pandas as pd
import requests


url = "https://oasm.dfsa.dk/uk/searchannouncementresult.aspx?headline=&name=&RealAnnouncerCVR=&CVRnumber=&announcmentsId=-1&informationTypeId=23&announcementTypeId=-1&languageId=-1&nationality=-1&pubDateFrom=2007:11:25:00:00&pubDateTo=2019:12:25:14:38&regDateFrom=1999:01:01:00:00&regDateTo=2050:01:01:00:00&index=3&sindex={}&historic=1&postponed=0"


df = pd.DataFrame(columns=["date", "time", "company_announcement", "company", "type"])

def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")

def get_pages():

    count = 0

    for i in range(1,4300,10):

        soup = get_page_contents(url.format(i))
        rows = soup.findAll('tr', class_='detail')

        for row in rows:
            temp = []
            for col in row.find_all("td"):
                temp.append(col.text)
            df.loc[count] = temp
            count += 1

get_pages()          
        
print(df)
df.to_csv("fin_output_results.csv")

