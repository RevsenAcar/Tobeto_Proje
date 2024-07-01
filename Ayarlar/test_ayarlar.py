from calendar import c
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("https://tobeto.com/giris")
    driver.maximize_window()
    yield driver
    driver.quit()

class TestSifreDegisim:

    def test_bos_bırakma(self, browser):
        # Giriş yap
        browser.find_element(By.NAME, "email").send_keys("ignacio.ender@floodouts.com")
        browser.find_element(By.NAME, "password").send_keys("123456")
        logibuton = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
        logibuton.click()

        # platform sayfası
        WebDriverWait(browser, 5).until(EC.url_to_be("https://tobeto.com/platform"))
        time.sleep(25)  
        # Profilimi Oluştur modülünde Başla butonuna tıkla
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/section[3]/div/div/div[1]/div/button').click()
        time.sleep(15)  
        # Ayarlar başlığına tıkla
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[10]/span[2]').click()
        time.sleep(15)    
        # Şifre değiştir butonuna tıkla
        browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(25) 
        # Beklenen sonucu kontrol et
        assert "Doldurulması zorunlu alan*" in browser.page_source
        time.sleep(25) 


    def test_sifre_eslesme_kontrol(self, browser):
        browser.find_element(By.NAME, "email").send_keys("ignacio.ender@floodouts.com")
        browser.find_element(By.NAME, "password").send_keys("123456")
        logibuton = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
        logibuton.click()

        WebDriverWait(browser, 10).until(EC.url_to_be("https://tobeto.com/platform"))
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/section[3]/div/div/div[1]/div/button').click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[10]/span[2]')))
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[10]/span[2]').click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/input')))
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/input').send_keys("123456")
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input').send_keys("1234568")
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input').send_keys("1234569")
        browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

        try:
            error_message = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body"))
            )
            assert error_message.text == "• Girilen şifreler eşleşmiyor kontrol ediniz.."
        except Exception as e:
            browser.save_screenshot("error_screenshot.png")
            raise e



    def test_sifre_karakter_kontrol(self, browser):
        browser.find_element(By.NAME, "email").send_keys("ignacio.ender@floodouts.com")
        browser.find_element(By.NAME, "password").send_keys("123456")
        logibuton = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
        logibuton.click()
    
        WebDriverWait(browser, 10).until(EC.url_to_be("https://tobeto.com/platform"))
        time.sleep(5)
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/section[3]/div/div/div[1]/div/button').click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[10]/span[2]')))
        time.sleep(5)
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[10]/span[2]').click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/input')))
        time.sleep(5)
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/input').send_keys("123456")
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input').send_keys("123")
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input').send_keys("123")
        browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(15)
        
        browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()            
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
        assert browser.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Şifreniz en az 6 karakterden oluşmalıdır."
        time.sleep(12)
       
    @pytest.mark.skip(reason="Bu test sonucunda verilmesi gereken mesaj hatalı ve raporlandı.")
    def test_tekrarlayan_sifre_kontrol(self, browser):
        browser.find_element(By.NAME, "email").send_keys("ignacio.ender@floodouts.com")
        browser.find_element(By.NAME, "password").send_keys("123456")
        logibuton = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
        logibuton.click()

        WebDriverWait(browser, 10).until(EC.url_to_be("https://tobeto.com/platform"))
        time.sleep(5)  # 5 saniye bekle
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/section[3]/div/div/div[1]/div/button').click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[10]/span[2]')))
        time.sleep(5)  # 5 saniye bekle
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[10]/span[2]').click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/input')))
        time.sleep(5)  # 5 saniye bekle
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/input').send_keys("123456")
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input').send_keys("123456")
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input').send_keys("123456")
        browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(10)  # 10 saniye bekle


                   
        WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
        assert browser.find_element(By.CSS_SELECTOR, ".toast-body").text == "Yeni şifreniz mevcut şifrenizden farklı olmalıdır"
       
       
    
    @pytest.mark.skip(reason="Bu test, şifre değişimini önlemek için atlanacak.")
    def test_basarili_sifre_yenileme(self, browser):
        browser.find_element(By.NAME, "email").send_keys("rhyett.baron@floodouts.com")
        browser.find_element(By.NAME, "password").send_keys("1234567")
        logibuton = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
        logibuton.click()
        
        WebDriverWait(browser, 5).until(EC.url_to_be("https://tobeto.com/platform"))
        time.sleep(25)  
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/section[3]/div/div/div[1]/div/button').click()
        time.sleep(15)  
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[10]/span[2]').click()
        time.sleep(15)    
        oldPassword=browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/input').send_keys("1234567")
        newPassword= browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input').send_keys("1234567")
        newPasswordAgain= browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input').send_keys("12345678")
        browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(15) 
        assert "• Şifreniz güncellenmiştir.." in browser.page_source
   
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
        