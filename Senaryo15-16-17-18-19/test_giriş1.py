from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium .webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date



class Test_TobetoLogin:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tobeto.com/giris")
        self.folder=str(date.today())
        Path(self.folder).mkdir(exist_ok=True)
        
    @pytest.mark.parametrize("username,password",[("nisanr.bas@gmail.com","Nisa123." )])
    #  başarılı giriş   
    def test_login(self,username,password):
        
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")))
        usernameInput = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")))
        passwordInput = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
    
        loginBtn.click()
        
        
        
        # platform sayfasına gelene kadar bekle
        WebDriverWait(self.driver,5).until(ec.url_to_be("https://tobeto.com/platform"))
        target_url="https://tobeto.com/platform"
        basarili_message = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div/div[2]")
        

        currunt_url=self.driver.current_url
        self.driver.save_screenshot(f"{self.folder}/test_login.png")
        assert currunt_url==target_url,f"Ana sayfaya ulaşılmıştır"
        assert basarili_message.text=="• Giriş başarılı."
        

    # ikissi boşken başarısız
    def test_login_fullempty(self):
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input"))
        usernameInput = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input"))
        passwordInput = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
        usernameInput.send_keys("")

        passwordInput.send_keys("")
        loginBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
        loginBtn.click()
        errorMessage2=self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/p")
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/p")
        self.driver.save_screenshot(f"{self.folder}/test_login_fullempty.png")
        assert errorMessage.text,errorMessage2 == ("Doldurulması zorunlu alan*","Doldurulması zorunlu alan*")
        # şifre boşken
    def test_login_empty_password(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")))
        usernameInput = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")))
        passwordInput = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
        usernameInput.send_keys("nisanr.bas")
        passwordInput.send_keys("")
        loginBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
        loginBtn.click()
        errorMessage2=self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/p")
        self.driver.save_screenshot(f"{self.folder}/test_login_empty_password.png")
        
        assert errorMessage2.text=="Doldurulması zorunlu alan*"
    #    eposta boşken
    def test_login_empty_email(self):

        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input"))
        usernameInput = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input"))
        passwordInput = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")

        usermameInput=("")
        passwordInput.send_keys("123456")
        loginBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/p")
        self.driver.save_screenshot(f"{self.folder}/test_login_fullempty.png")
        assert errorMessage.text=="Doldurulması zorunlu alan*"
    #  gecersiz eposta veya şifre
    @pytest.mark.parametrize("username,password",[("nisanr.bas@gmail.com","123" ),("nisanr.bas@","Nisa123." ),("nisa","1111")])
     
    def test_login_invalid(self,username,password):

   
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input"))
        usernameInput = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input"))
        passwordInput = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
        loginBtn.click()
        sleep(3)
        errorMessage4=self.driver.find_element(By.CSS_SELECTOR,".toast-body")  
        self.driver.save_screenshot(f"{self.folder}/test_login_invalid.png")
        assert errorMessage4.text=="• Başarısız..."

