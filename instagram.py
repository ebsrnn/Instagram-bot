from selenium import webdriver
from login import username,password
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instegram():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.browser=webdriver.Chrome()


    def sıngIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        usernameInput=self.browser.find_element(By.XPATH ,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput=self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
    
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(35)

        self.browser.find_element(By.CSS_SELECTOR,"div[role=button]").click()
        time.sleep(3)

        

    def Getfollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        

        time.sleep(4)
        followersLink=self.browser.find_element(By.CSS_SELECTOR,".x78zum5.x1q0g3np.xieb3on").find_element(By.TAG_NAME,"a").click()

        time.sleep(4)
        users=self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        
        followersList=[]


        for user in users:
            followername=user.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade").text
            followersList.append(user)

        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in followersList:
                file.writr(item+"\n")

    def allFollowers(self):
   
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        

        time.sleep(4)
        followersLink=self.browser.find_element(By.CSS_SELECTOR,".x78zum5.x1q0g3np.xieb3on").find_element(By.TAG_NAME,"a").click()


        time.sleep(4)
        fallowerlist=self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog]")
        usersCount=len(fallowerlist.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
        print(f"first part: {usersCount}")

        while True:
            fallowerlist.click()

            scroll_count=4
            for i in range(scroll_count):
                self.browser.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
                time.sleep(2)

                newCount=len(fallowerlist.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
            if usersCount !=newCount:
                usersCount=newCount
                print(f"all followers: {newCount}")
            else:
                    break





        users=self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        for user in users:
            followername=user.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade").text
            print(followername)


    def FollowersUser(self,followerName):

        self.browser.get(f"https://www.instagram.com/{followerName}/")

        time.sleep(4)
        text=self.browser.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aad6._aade")
        if text !=" following":
            self.browser.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aade").click()
            time.sleep(2)

        else:
            print("you are following now")

    def unfollowUser(self,followerName):
        self.browser.get(f"https://www.instagram.com/{followerName}")
        time.sleep(10)

        text=self.browser.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aad6._aade").text

        if text !="following":
            self.browser.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aad6._aade").click()
            time.sleep(6)
            button=self.browser.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]")
            button.click()

            time.sleep(2)


ınstgrm=Instegram(username,password)
ınstgrm.sıngIn()
# ınstgrm.Getfollowers()
# ınstgrm.allFollowers()

# list=["nasaearth",""]
# for user in list:
#     ınstgrm.FollowersUser("user")
#     time.sleep(3)
ınstgrm.unfollowUser("nasaearth")

