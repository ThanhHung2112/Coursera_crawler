from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service

from time import sleep
import random
import pandas as pd

class Course_craw():
    def __init__(self):
        
        self.df = pd.read_csv("data/Coursera.csv")
        self.df["Specialized"] = None
        # Options
        service = Service(executable_path='Libs/chromedriver.exe')
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-extensions")
        # options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--window-size=1920x1080")

        self.browser = Chrome(service=service, options=options)

    def Start_craw(self):
        
        print("Starting")
        percent_step = len(self.df) // 10

        for i in range(351, len(self.df)):

            self.browser.get(self.df["Course URL"][i]) 

            try: 
                element = self.browser.find_element(By.XPATH,"/html/body/div[2]/div/main/section[1]/div/div/div/div[1]/nav/ol/li[3]/a")
            
                self.df["Specialized"][i] = element.text
                # print(element.text)
                sleep(random.randint(1,3))

                if (i + 1) % percent_step == 0:
                    percentage = round((i + 1) / len(self.df) * 100)
                    print(f"Processing: {percentage}%")                   

            except:()

        print("================================")
        print("Save results")

        self.df.to_csv("data/Coursera_2.csv", index=False)
        return
    
Course_craw().Start_craw()  

