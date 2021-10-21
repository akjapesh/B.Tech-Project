from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ff=open("text.txt","w",encoding='utf-8')
ff2=open("text2.txt","w")

with open('list_tags', 'rb') as f:
     tags = pickle.load(f)
print(len(tags),file=ff2)
print(tags,file=ff2)


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
wd=webdriver.Chrome()
URL="https://www.sec.gov/ix?doc=/Archives/edgar/data/1021635/000102163520000016/oge-20191231.htm"

wd.get(URL)
time.sleep(1)

elements = WebDriverWait(wd, 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@enabled-taxonomy="true"]')))

print(elements.__len__())
global sec0
sec_doc="SEC"
i=0
e=elements[3]

try:
    e.click()
    reset=WebDriverWait(wd,1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="taxonomy-modal-carousel-indicators"]/li[1]')))
    reset.click()
    next=WebDriverWait(wd,1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="taxonomy-modal"]/div[3]/button[2]')))
    page1_tags=WebDriverWait(wd,1).until(EC.visibility_of_any_elements_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-1"]/tbody/tr')))
    print(len(page1_tags))
    for st in page1_tags:
        tag=st.find_element_by_tag_name("th")
        label=st.find_element_by_tag_name("div")
        print(tag.get_attribute("innerHTML"),"->",label.get_attribute("innerHTML"))
    # //*[@id="taxonomy-modal-carousel-page-1"]/tbody/tr[1]/th
    # sec_tag=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-1"]/tbody/tr[1]/td/div'))).get_attribute("innerHTML")
    # sec_fact=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-1"]/tbody/tr[2]/td/div'))).get_attribute("innerHTML")
    # sec_period=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-1"]/tbody/tr[3]/td/div'))).get_attribute("innerHTML")
    # sec_type=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-1"]/tbody/tr[4]/td/div'))).get_attribute("innerHTML")
    
    # next.click()
    page2_tags=wd.find_elements_by_xpath('//*[@id="taxonomy-modal-carousel-page-2"]/div/tr')
    print(len(page2_tags))
    for st in page2_tags:
        tag=st.find_element_by_tag_name("th")
        label=st.find_element_by_tag_name("div")
        print(tag.get_attribute("innerHTML"),"->",label.get_attribute("innerHTML"))
    # sec_docu=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-2"]/div/tr[1]/td/div'))).get_attribute("innerHTML")
    # sec_label=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-2"]/div/tr[2]/td/div'))).get_attribute("innerHTML")
    # sec_terse_label=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-2"]/div/tr[3]/td/div'))).get_attribute("innerHTML")
    # next.click()
    page3_tags= wd.find_elements_by_xpath('//*[@id="taxonomy-modal-carousel-page-2"]/div/tr')
    print(len(page3_tags))
    for st in page3_tags:
        tag=st.find_element_by_tag_name("th")
        label=st.find_element_by_tag_name("div")
        print(tag.get_attribute("innerHTML"),"->",label.get_attribute("innerHTML"))
    # try:
    #     sec_name=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-3"]/div/tr[1]/td'))).get_attribute("innerHTML")
    #     sec_number=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-3"]/div/tr[2]/td'))).get_attribute("innerHTML")
    #     sec_publisher=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-3"]/div/tr[3]/td'))).get_attribute("innerHTML")
    #     sec_section=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-3"]/div/tr[4]/td'))).get_attribute("innerHTML")
    #     sec_subsection=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-3"]/div/tr[5]/td'))).get_attribute("innerHTML")
    # except KeyboardInterrupt:
    #     quit()
    # except:
    #     sec_name="No data"
    #     sec_number="No data"
    #     sec_publisher="No data"
    #     sec_section="No data"
    #     sec_subsection="No data"

        
    # next.click()
    # sec_balanace=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-4"]/div/tr/td'))).get_attribute("innerHTML")
    # if sec_doc =="SEC" and sec_tag=="dei:EntityRegistrantName":
    #     sec_doc=sec_fact
    
    
    close=WebDriverWait(wd,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[1]/div/i[6]')))
    close.click()
    # if sec_tag in tags:
    #     print(i)
    #     if "Contract / Expand" in sec_fact:
    #         print("------skip---------")
            
    #     else:
    #         print(sec_doc+" , "+sec_tag+" , "+sec_fact+" , "+sec_label+" , "+sec_section+" , "+sec_balanace,file=ff)
except KeyboardInterrupt:
    exit()
except:
    print("--------error---------")



wd.close()




