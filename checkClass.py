import requests 
from bs4 import BeautifulSoup 

targetURL = "http://buy.sinyi.com.tw/list/"

def findTypeClass(pageFind):
    getList = []
    for page in range(1, pageFind):
        itemURL = targetURL + str(page) +".html" #http://buy.sinyi.com.tw/list/i.html 
        result = requests.get(itemURL)
        soup = BeautifulSoup(result.text,'html.parser')
        items = len(soup.findAll('div', class_= 'search_result_item'))
        for item in soup.select('.search_result_item'):
            houseType = []
            houseType.append(item.select('.detail_line1 span:nth-of-type(2)')[0].text.strip())
            getList.append(houseType)
    
    splitList = []
    returnList = []
    
    for result in getList:
        for types in result:
            splitList.append(types.split('、'))
    for eachList in splitList:
        for eachType in eachList:
            returnList.append(eachType)
    return set(returnList)

def findFunctionClass(pageFind):
    getList = []
    for page in range(1, pageFind):
        itemURL = targetURL + str(page) +".html"
        result = requests.get(itemURL)
        soup = BeautifulSoup(result.text,'html.parser')
        items = len(soup.findAll('div', class_= 'search_result_item'))
        for item in soup.select('.search_result_item'):
            houseFunction = []
            if len(item.select('.detail_tagGroup')) > 0:
                for eachFunction in range(0,len(item.select('div.detail_tagGroup > div.detail_tag'))):
                    houseFunction.append(item.select('div.detail_tagGroup > div.detail_tag')[eachFunction].text)
            getList.append(houseFunction)
    
    returnList = []
    for eachList in getList:
        for eachFunction in eachList:
            returnList.append(eachFunction)
    return set(returnList)

if __name__ == "__main__":
    pages = 3
    print("屋型包含： ", findTypeClass(pages))
    print("房屋機能： ", findFunctionClass(pages))