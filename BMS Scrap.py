from datetime import datetime

screenToFind = "PVR: The Forum Mall, Koramangala"
toEmailList = ["risingrohit18@gmail.com","dsumanth17@gmail.com"] 
fromEmail = "rohitphotos18@gmail.com"
passwordOfFromEmail = "password"


def notifyUser():
	openUrl()
	sendEmail(fromEmail, passwordOfFromEmail, toEmailList, screenToFind + ' Found!!', screenToFind + " is now listed. \nBook from here : "+url)

def openUrl():
	import webbrowser
	webbrowser.open(url)
	
def sendEmail(user, pwd, recipient, subject, body):
    import smtplib
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, pwd)
        print('reached here')
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


print("BMS Scrape started at "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

import requests
url = "https://in.bookmyshow.com/buytickets/rrr-bengaluru/movie-bang-ET00094579-MT/20220325#!quickbook"
request  = requests.get(url)
htmlContent = request.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(htmlContent, "html.parser")
venueList = soup.find('ul', {'id': 'venuelist'})
found = False
availableList = ""
screenToFindLower = screenToFind.lower();
for link in venueList.find_all('li'):
    screenName = link.get('data-name')
    if(screenName.lower().find(screenToFindLower)>-1):
        found = True
        break
    availableList+=screenName + "\n"

if(found==False):
    print(screenToFind + ' not found')
else:
    print(screenToFind + " found! Triggering emails to: "+', '.join(toEmailList))
    notifyUser()
print("BMS Scrape completed at "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
