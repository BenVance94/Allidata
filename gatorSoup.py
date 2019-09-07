from bs4 import BeautifulSoup
import pandas as pd
import requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class gatorSoup:

    def __init__(self, media_url):
        self.url = media_url

    def chomp(self):
        r = requests.get(self.url, verify=False)
        mediaText=[]
        if r.status_code == 200:
            print(str(self.url) + " --- 200 --- SUCCESS")
            try:
                soup = BeautifulSoup(r.content, 'html.parser')
                myBool = True
                i=0
                while myBool == True:
                    try:
                        paragraphs = soup.find_all("a")[i].text
                        paragraphs = paragraphs.replace("\n", "")
                        paragraphs = paragraphs.strip()
                        #Removing any instances under 25 characters
                        if len(str(paragraphs)) > 25:
                            mediaText.append(paragraphs)
                        i = i + 1
                    except IndexError:
                        myBool = False
            except:
                print("Error w/ status code 200 --- CHECK gatorSoup!")
                mediaText = ["Null"]
                pass
        else:
            print(str(self.url) + " --- " + str(r.status_code) + " --- FAIL")
            mediaText = ["Null"]
        print(str(self.url)+" provided --- "+str(len(mediaText))+" descriptions")
        df = pd.DataFrame(list(set(mediaText)), columns=['mediaText'])
        df['mediaUrl'] = self.url
        df['responseStatusCode'] = r.status_code
        return df
