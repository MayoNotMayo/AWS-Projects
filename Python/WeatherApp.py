#CURRENTLY BROKEN, IN PROGRESS
"""
Builds a weather notification 
app using bs4 to pull data out of HTML 
and win10toast to send desktop notifications
"""
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#create object ToastNotifier class
n = ToastNotifier()

#define the function for getting data from url
def getdata(url):
    r = requests.get(url)
    return r.text

#passes the URL into getdata
htmldata = getdata("https://weather.com/ja-JP/weather/today/l/6ea069bb92c2b096313a804af4d67d5cce9e2422934cdb6d421792f434fb381d")
#convert the data into htmldata and print
soup = BeautifulSoup(htmldata, 'html.parser')
#print(soup.prettify())

#search the html to find the details
current_temp = soup.find_all("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
chances_rain = soup.find_all("div", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = (str(current_temp))
temp_rain = str(chances_rain)

result = "The current temperature in Tsubetsu is " + temp[128:-9] + "\n" +temp_rain[131:-14] 

n.show_toast("live Weather update", 
             result, duration = 10)