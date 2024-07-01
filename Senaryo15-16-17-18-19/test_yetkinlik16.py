

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
        




        

# BAŞARILI YETKİNLİK EKLEME TESTİ
def test_successful_skill_add(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
   
    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()

    
    # Adım 3: 'Yetkinliklerim başlığına'

    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[1]/div/a[4]/span[2]").click()
    

    # Adım 4: 'Yetkinliklerim alanına gel ve sql yaz'
    liste_input=wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/input")
   
    liste_input.send_keys("SQL")
    liste_input.send_keys(Keys.ENTER)
#    Adım 5: 'Kaydet' butonuna tıklayın

    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/button").click()
    sleep(2)
    # # Beklenen sonuç: 'Yetenek eklendi' mesajının görünmesi
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/ test_successful_skill_add.png"
    driver.save_screenshot(screenshot_path)
    assert "Yetenek eklendi" in driver.page_source
#BOŞ YETKİNLİK  EKLEME TESTİ
    
def test_empty_skill_add(driver):

    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
   
    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()

    
    # Adım 3: 'Yetkinliklerim başlığına'

    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[1]/div/a[4]/span[2]").click()

    
    # Adım 4: Yetenek ekleme alanını boş bırakın

    # Adım 5: 'Kaydet' butonuna tıklayın
    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/button").click()  
    sleep(1)
    # Beklenen sonuç: 'Herhangi bir yetenek seçemediniz!' mesajının görünmesi

    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_empty_skill_add.png"
    driver.save_screenshot(screenshot_path)
    assert "Herhangi bir yetenek seçmediniz!" in driver.page_source
    #YETKİNLİK SİLME
def test_skill_delete(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver, "nisanr.bas@gmail.com", "Nisa123.")

    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()

    
    # Adım 3: 'Yetkinliklerim başlığına'

    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[1]/div/a[4]/span[2]").click()


   

    # Adım 4: Silmek istediğiniz yeteneğin yanındaki çöp kutusu ikonuna tıklayın
    delete_icon = wait_for_element(driver, By.XPATH, "/html/body/div/div/main/section/div/div/div[2]/div[2]/div[1]/div/button")  # Ikon seçici gerektiği şekilde güncellenmelidir
    delete_icon.click()

    # Adım 5: Açılan pop-up'da 'Evet' butonuna tıklayın
    wait_for_element(driver, By.XPATH, "//button[text()='Evet']").click()
    sleep(2)

    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_skill_delete.png"
    driver.save_screenshot(screenshot_path)
    # # Beklenen sonuç: 'Yetenek kaldırıldı.' mesajının görünmesi
    assert "Yetenek kaldırıldı." in driver.page_source