from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://app.fitdegree.com/t/dashboard/live-schedule?f=700"
page= requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div')

with open('remote-jobs.csv', 'w', encoding='utf8', newline='') as f: 
    thewriter = writer(f)
    header = ['Class Date', 'Instructor Name', 'Class Time']
    thewriter.writerow(header)

    for list in lists: 
        class_date = list.find('div', class_="date-header").text
        instructor_name = list.find('h2', class_="instructor-name").text
        Time = list.find('div', class_="date").text
        date = [class_date, instructor_name, Time]
        thewriter.writerow(info)