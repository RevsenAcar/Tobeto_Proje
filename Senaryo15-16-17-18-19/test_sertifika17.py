from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest
import os
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


def get_desktop_file_path(filename):
    """
    Belirtilen dosya adını kullanarak masaüstündeki dosyanın tam yolunu döndürür.

    Args:
        filename (str): Dosya adı (örneğin, 'sertifika.png').

    Returns:
        str: Masaüstündeki dosyanın tam yolu.
    """
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, filename)
    return file_path

def sertifiklarım(driver):

    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()

    #Adım 3:Sertifikalarım sayfasına gel ve 

    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[1]/div/a[5]/span[2]").click()
  



        

#SERTİFİKA EKLE
def test_certifica_successful_add(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
    sertifiklarım(driver)

    #ekleyeceğin sertifika bilgilerini gir
    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div[2]/form/div[1]/div[1]/input").send_keys("sertifika")
    tarih=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div[2]/form/div[1]/div[2]/div/div/input")
    tarih.send_keys("2020")
    tarih.send_keys(Keys.ENTER)

    #Adım 4:Dosya yüklemek için gözata tıkla

    button=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div[2]/form/div[1]/div[3]/div/div/div/div[2]/div/div[2]/div[1]/button")
    button.click()
    sleep(6)
      # Adım 6: Bilgisayardan geçerli bir sertifika dosyasını seçin
    certificate_path = get_desktop_file_path('sertifika.png')
    file_input = wait_for_element(driver, By.XPATH, "//input[@type='file']")
    file_input.send_keys(certificate_path)

    sleep(4)
    #sertifikayı ekle
    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div[2]/form/div[2]/button").click()

    
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_certifica_successful_add.png"
    driver.save_screenshot(screenshot_path)
    sleep(2)
    #sertifika ekleme mesajı gözüktümü
    assert "Sertifikanız eklendi" in driver.page_source
    
   # Beklenen sonuç: Yüklenen dosyanın 'Sertifikalarım' kısmında liste olarak görünmesi



  
  
    
#sertifika kaldırma
def test_certifica_successful_delete(driver):
    # Kullanıcı giriş bilgilerini doldurun

    login(driver,"nisanr.bas@gmail.com","Nisa123.")
    sertifiklarım(driver)
    #silmek istediğini seç bu alan değişebilir.
    button =wait_for_element(driver, By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div[2]/div/div/div/table/tbody/tr/td[4]/span[2]")
    driver.execute_script("arguments[0].click();", button)


    #silmek istediğine eminmisin ekranı
    wait_for_element(driver, By.XPATH,"/html/body/div[3]/div/div")

    #Evet seçeneğine tıkla

    wait_for_element(driver, By.XPATH," /html/body/div[3]/div/div/div/div/div/div[2]/button[2]").click()

    sleep(1)


    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_certifica_successful_delete.png"
    driver.save_screenshot(screenshot_path)

    assert "Dosya kaldırma işlemi başarıl" in driver.page_source