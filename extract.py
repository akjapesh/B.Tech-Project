from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ff=open("triplets.txt","w",encoding='utf-8')
ff2=open("tags_name.txt","w")
ff3=open("facts_and_attributes.txt","w",encoding='utf-8')
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
time.sleep(3)

elements = WebDriverWait(wd, 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@enabled-taxonomy="true"]')))

print(elements.__len__(),file=ff)
print(elements.__len__(),file=ff3)
global sec0
sec_doc="SEC"
i=0
for e in elements:
    i+=1
    try:
        e.click()
        # reset=WebDriverWait(wd,1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="taxonomy-modal-carousel-indicators"]/li[1]')))
        # reset.click()
        # next=WebDriverWait(wd,1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="taxonomy-modal"]/div[3]/button[2]')))
        
        # page1_tags=WebDriverWait(wd,1).until(EC.visibility_of_any_elements_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-1"]/tbody/tr')))
        page1_tags=wd.find_elements_by_xpath('//*[@id="taxonomy-modal-carousel-page-1"]/tbody/tr')
        sec_tag=page1_tags[0].find_element_by_tag_name("div").get_attribute("innerHTML")
        sec_fact=page1_tags[1].find_element_by_tag_name("div").get_attribute("innerHTML")
        if sec_doc =="SEC" and sec_tag=="dei:EntityRegistrantName":
            sec_doc=sec_fact
        if "Contract / Expand" in sec_fact:
            print("------skip contract/expand---------")
            continue
        if sec_tag not in tags:
            print("------not imp---------")
            continue
        print(i)
        print(sec_doc+" , "+sec_tag+" , "+sec_fact,file=ff)
        print("{",file=ff3)
        for st in page1_tags:
            tag=st.find_element_by_tag_name("th")
            label=st.find_element_by_tag_name("div")
            print('\t " '+tag.get_attribute("innerHTML"),' " : " ',label.get_attribute("innerHTML")+' " ',file=ff3)
        
        # next.click()
        # page2_tags=WebDriverWait(wd,1).until(EC.visibility_of_any_elements_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-2"]/div/tr')))
        try:
            page2_tags=wd.find_elements_by_xpath('//*[@id="taxonomy-modal-carousel-page-2"]/div/tr')
            for st in page2_tags:
                tag=st.find_element_by_tag_name("th")
                label=st.find_element_by_tag_name("div")
                print('\t " '+tag.get_attribute("innerHTML"),' " : " ',label.get_attribute("innerHTML")+' " ',file=ff3)
        except KeyboardInterrupt:
            quit()
        except:
            print("--no page2--")
            pass

        try:
            page3_tags=wd.find_elements_by_xpath('//*[@id="taxonomy-modal-carousel-page-3"]/div/tr')
            for st in page3_tags:
                    tag=st.find_element_by_tag_name("th")
                    label=st.find_element_by_tag_name("td")
                    print('\t " '+tag.get_attribute("innerHTML"),' " : " ',label.get_attribute("innerHTML")+' " ',file=ff3)
        except KeyboardInterrupt:
            quit()
        except:
            print("--no page3--")
            pass
        # next.click()
        # try:
        #     page3_tags=WebDriverWait(wd,1).until(EC.visibility_of_any_elements_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-3"]/div/tr')))
        #     for st in page3_tags:
        #         tag=st.find_element_by_tag_name("th")
        #         label=st.find_element_by_tag_name("td")
        #         print('\t " '+tag.get_attribute("innerHTML"),' " : " ',label.get_attribute("innerHTML")+' " ',file=ff3)
        # except KeyboardInterrupt:
        #     quit()
        # except:
        #     pass

            
        # next.click()
        # sec_balanace=WebDriverWait(wd,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="taxonomy-modal-carousel-page-4"]/div/tr/td'))).get_attribute("innerHTML")
        try:
            sec_balance=wd.find_element_by_xpath('//*[@id="taxonomy-modal-carousel-page-4"]/div/tr/td').get_attribute("innerHTML")
            print('\t " sec_balanace " : " '+sec_balance+' " ',file=ff3)
        except KeyboardInterrupt:
            quit()
        except:
            print("--no page4--")
            pass
        print("}",file=ff3)
        
        
        
        close=WebDriverWait(wd,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[1]/div/i[6]')))
        close.click()
        
    except KeyboardInterrupt:
        exit()
    except:
        print("--------error---------")
    


wd.close()




