###        _________________________________
###        <AUTOMATE WHATSAPP WITH AUTOREPLY >
###        ---------------------------------
###                      \   ^__^
###                        \  (oo)\_______
###                          (__)\       )\/\
###                              ||----w |
###                              ||     ||


########### OPEN TERMINAL OR CMD AND TYPE: "pip install selenium" ##########

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

########### #ADD YOUR CHROMEDRIVER.EXE LOCATION ##########

chromedr = r"C:\Users\KIIT\Documents\programming\chromedriver.exe" 
driver = webdriver.Chrome(chromedr)
driver.get("https://web.whatsapp.com/")
time.sleep(8)

########## REPLACE "Routine" WITH GROUP OR PERSON NAME FROM YOUR WHATSAPP ##########

names = "Routine" 
for name in names:
     
    person = driver.find_element_by_xpath('//span[@title= "{}"]'.format(names))
    person.click()
    while(True):
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            ############### OPEN YOUR WHATSAPP IN WEB AND INSPECT FOR LAST MESSAGE AND COPY SELECTABLE PATH AND PASTE IN CSS SELLECTOR################

        msg_got = driver.find_elements_by_css_selector("span._3Whw5.selectable-text.invisible-space.copyable-text")
        msg =[message.text for message in msg_got]
        msgin = "/class"
        x = datetime.datetime.now()
        y = x.strftime("%A")
        if msg[-1].lower() == msgin.lower():
                if y.lower() == "monday":
            
############################## INSPECT THE TYPING BOX AND COPY SELECTOR FROM WHATSAPP WEB AND PASTE IN CSS SELLECTOR####################

                    reply = driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")
                    reply.clear()
                    reply.send_keys("ADD YOUR MONDAY TIMETABE HERE")
                    reply.send_keys(Keys.RETURN)
                elif y.lower() == "tuesday":
                    reply = driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")
                    reply.clear()
                    reply.send_keys("ADD YOUR TUESDAY TIMETABE HERE")
                    reply.send_keys(Keys.RETURN)
                elif y.lower() == "wednesday":
                    reply = driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")
                    reply.clear()
                    reply.send_keys("ADD YOUR WEDNESDAY TIMETABE HERE")
                    reply.send_keys(Keys.RETURN)
                elif y.lower() == "thursday":
                    reply = driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")
                    reply.clear()
                    reply.send_keys("ADD YOUR THRUSDAY TIMETABE HERE")
                    reply.send_keys(Keys.RETURN)
                elif y.lower() == "friday":
                    reply = driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")
                    reply.clear()
                    reply.send_keys("ADD YOUR FRIDAY TIMETABE HERE")
                    reply.send_keys(Keys.RETURN)
                elif y.lower() == "saturday":
                    reply = driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")
                    reply.clear()
                    reply.send_keys("ADD YOUR SATURDAY TIMETABE HERE")
                    reply.send_keys(Keys.RETURN)
                elif y.lower() == "sunday":
                    reply = driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")
                    reply.clear()
                    reply.send_keys("ADD YOUR SUNDAY TIMETABE HERE")
                    reply.send_keys(Keys.RETURN)
                else :
                    print ("done")
