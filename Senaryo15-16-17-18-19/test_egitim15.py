from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest
from pathlib import Path
from datetime import date
import openpyxl

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://tobeto.com/giris")  # Giriş sayfasına gidin
    folderPath=str(date.today())
    Path(folderPath).mkdir(exist_ok=True)
    yield driver
    driver.quit()

def login(driver, email, password):
  
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")))
    usernameInput = driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")))
    passwordInput =driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    usernameInput.send_keys(email)
    passwordInput.send_keys(password)
        
    loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
    
    loginBtn.click()

    # platform sayfasına gelebeklene kadar 
    WebDriverWait(driver,5).until(EC.url_to_be("https://tobeto.com/platform"))

def wait_for_element(driver, by, value, timeout=10):
     return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by,value)))
        




        

# Eğitim ekleme testi
def test_educationadd(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
   
    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()


    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[1]/div/a[3]/span[2]").click()

    egitim=wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div/div/div[1]/div[2]/input")
    sleep(5)
    
    egitim.send_keys("Lisans")
    egitim.send_keys(Keys.ENTER)
    sleep(2)
#   


#     sleep(5)
    # 
    
    
    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[2]/input").send_keys("Sakarya Üniversitesi")
    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[3]/input").send_keys("Sayısal")
    year=wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[4]/div[1]/div/input")
    year.send_keys("2016")
    year.send_keys(Keys.ENTER)

    sleep(3)

    endyear=wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input")
    endyear.send_keys("2020")
    endyear.send_keys(Keys.ENTER)

    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/form/button").click()
    sleep(5)

         
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_educationadd_.png"
    driver.save_screenshot(screenshot_path)
    assert "• Eğitim bilgisi eklendi." in driver.page_source

#Eğitim silme testi

def test_educationdelete(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
   
    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()


    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[1]/div/a[3]/span[2]").click()

    sleep(2)

    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/div/div[2]/div[3]/span[1]/i").click()

    sleep(2)
    wait_for_element(driver, By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[2]/button[2]").click()

    sleep(1)

    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_educationdelete_.png"
    driver.save_screenshot(screenshot_path)

    assert "Eğitim kaldırıldı." in driver.page_source


#Eklediğin eğitim durumuna göre ismi girdiğin alanın değişmemesi
@pytest.mark.skip()
def test_succesi(driver):
       # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
   
    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()


    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[1]/div/a[3]/span[2]").click()

    egitim=wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div/div/div[1]/div[2]/input")
    sleep(3)
    
    egitim.send_keys("Lise")
    egitim.send_keys(Keys.ENTER)
    sleep(3)
#   
    yazi=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/form/div/div[2]/label")
    yazi=yazi.text
    beklenen="Lise*"

         
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_certifica_successful_delete.png"
    driver.save_screenshot(screenshot_path)

    assert yazi==beklenen,f"Beklenen alan ismi:{beklenen},Ancak görülen:{yazi}"

# #    Adım 5: 'Kaydet' butonuna tıklayın



