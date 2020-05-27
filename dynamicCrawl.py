#In order to web scrape a dynamic web page that uses JavaScript to load conent:
    #Use Selenium with Chrome Web Driver (Chromium)
    #To use Selenium, must also install a web browser engine: geckodriver
    

#Strategy:
#Use Selenium web driver to call the browser
#Search for elements of interest by searching by XPath
#Return results and store in a pandas dataframe
#Export dataframe to Excel Sheet

#Import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

#Specify the URL
urlpage = 'https://programs.sigchi.org/chi/2019/search?searchKey=visualization'
#print(urlpage)
#Run Chrome webdriver from executable path of your choice
driver = webdriver.Chrome(ChromeDriverManager().install())

#Page Scroll Test
#Get web page
driver.get(urlpage)
#Execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
#Sleep for 30s
time.sleep(30)
#Driver.quit()

#Find elements by XPath

#results = driver.find_elements_by_xpath("//*[@class=' tab-content']//*[@class=' tab-pane active ng-star-inserted']//*[@class='program-body vertical selfScroll ng-star-inserted']//*[@class='scrollable-content']//*[@class='ng-star-inserted']//*[@class='card-container']//*[@class='card-data-name ng-star-inserted']")
results = driver.find_elements_by_xpath('/html/body/app-root/conference/search/ngb-tabset/div/div[1]/virtual-scroller/div[2]/content-card/div/program-card-data/h6')
print('Number of results', len(results))

#Create an empty array to store data
data = []
#Loop over results
for result in results:
    title = result.text
    #link = result.find_element_by_tag_name('a')
    #product_link = link.get_attribute("href")
    #append dict to array
    data.append({"Title" : title})
#Close driver
driver.quit()
#Save to pandas dataframe
df = pd.DataFrame(data)
print(df)

#Write to excel file
df.to_excel('CHI_2019.xlsx')
