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
    
        

# BAŞARILI YABANCI DİL EKLEME TESTİ
def test_language__add(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
   
    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()

    
    # Adım 3: "Yabancı dillerim" başlığına tıkla
    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[1]/div/a[9]/span[2]").click()


    dil=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/form/div/div[1]/div/div/div[1]/div[2]/input")
    dil.click()
    dil.send_keys("İngilizce")
    sleep(2)
    dil.send_keys(Keys.ENTER)

    seviye=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/form/div/div[2]/div/div/div[1]/div[2]/input")
  
    
    seviye.click()
    seviye.send_keys("Orta")
    seviye.send_keys(Keys.ENTER)

    sleep(2)

      #kaydet butonuna bas

    wait_for_element(driver, By.XPATH," /html/body/div/div/main/section/div/div/div[2]/form/button").click()

    sleep(5)

    # # Beklenen sonuç: 'Yabancı dil bilgisi eklendi' mesajının görünmesi
    
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_language_add.png"
    driver.save_screenshot(screenshot_path)

    assert "• Yabancı dil bilgisi eklendi" in driver.page_source
    
#Yabancı Dil Boş Bırakma Kontrolü 

def test_language_emptychoice(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()

    
    # Adım 3: "Yabancı dillerim" başlığına tıkla
    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[1]/div/a[9]/span[2]").click()
   

    #Dil seçimi yap seviyeyi boş bırak
    

    dil=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/form/div/div[1]/div/div/div[1]/div[2]/input")
    dil.click()
    dil.send_keys("ALMANCA")
    dil.send_keys(Keys.ENTER)

    wait_for_element(driver, By.XPATH," /html/body/div/div/main/section/div/div/div[2]/form/button").click()
    #Bekklenen uyarı

    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_language_emptychoice1.png"
    driver.save_screenshot(screenshot_path)
    assert "Doldurulması zorunlu alan*" in driver.page_source

    sleep(3)
    driver.refresh()
    sleep(2)

    #seviyeyi dolu dil seçimini boş bırak
    seviye=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/form/div/div[2]/div/div/div[1]/div[2]/input")
    seviye.click()
    seviye.send_keys("temel seviye")
    seviye.send_keys(Keys.ENTER)
    wait_for_element(driver, By.XPATH," /html/body/div/div/main/section/div/div/div[2]/form/button").click()

    sleep(2)
    
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_language_emptychoice2.png"
    driver.save_screenshot(screenshot_path)
    assert "Doldurulması zorunlu alan*" in driver.page_source
    sleep(2)



@pytest.mark.skip()
def test_language_delete(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()

    
    # Adım 3: "Yabancı dillerim" başlığına tıkla
    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[1]/div/a[9]/span[2]").click()

    #Dillerin sol kısımdaki çöp kutusuna tıkla

    wait_for_element(driver,By.XPATH, "/html/body/div/div/main/section/div/div/div[2]/div/div/div/span[2]").click()
    sleep(2)
    # wait_for_element(driver,By.CSS_SELECTOR, ".btn-yes").click()

    #EVETE TIKLA

    # wait_for_element(driver, By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[2]/button[2]").click()
    sleep(4)
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_language_delete.png"
    driver.save_screenshot(screenshot_path)
    assert "Yabancı dil kaldırıldı." in driver.page_source

    sleep(2)









    
    # seviye.click()
    # seviye.send_keys("Orta")
    # seviye.send_keys(Keys.ENTER)

    # sleep(2)
 
    # # if platform=="instagram":
    # #     message="Doldurulması zorunlu alan*" 

    # sleep(1)
    # assert "Doldurulması zorunlu alan*" in driver.page_source

