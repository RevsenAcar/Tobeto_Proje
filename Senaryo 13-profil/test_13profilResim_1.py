import os
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    # Webdriver'ı başlat
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Test tamamlandıktan sonra tarayıcıyı kapat
    driver.quit()

def get_desktop_file_path(filename):
    # Bir dosya adını girdi olarak al ve kullanıcının masaüstündeki bu dosyaya tam yolu döndür.
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, filename)
    return file_path

def test_profil(browser):
    try:
        # Adım 1: Başarılı giriş yap
        browser.get("https://tobeto.com/giris")
        # Kullanıcı adı ve şifre girme işlemi
        email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
        email_input.send_keys("davy.acxel@floodouts.com")
        password_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
        password_input.send_keys("369369")
        login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
        login_button.click()
        
        # Platform açılmalıdır.
        platform_title = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3"))
        )
        sleep(4)
    
        # Adım 2: 'Profilim' alanından profil bilgilerim butonuna tıkla
        profilalani = browser.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")
        profilalani.click()
        profilbilgileri = browser.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")
        profilbilgileri.click()
        sleep(2)
    
        # Adım 3: Görsel yükleme butonuna tıkla
        buton = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[1]/div")
        sleep(22)
        buton.click()
        sleep(22)
    
        # Adım 4: Gözat seçeneğine tıkla ve dosya seç
        profilresmi_path = get_desktop_file_path('rev.png')
        if not os.path.exists(profilresmi_path):
            raise FileNotFoundError(f"Dosya bulunamadı: {profilresmi_path}")
        
        file_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        file_input.send_keys(profilresmi_path)
        sleep(2)
    
        # Dosya yükle butonuna tıkla
        dosyayukle_buton = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button")
        dosyayukle_buton.click()
        sleep(2)

    except Exception as e:
        print(f"Test başarısız oldu: {e}")
        browser.save_screenshot("error_screenshot.png")
        raise
    
