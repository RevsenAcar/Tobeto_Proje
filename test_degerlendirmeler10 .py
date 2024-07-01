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
    yield driver
    # Test tamamlandıktan sonra tarayıcıyı kapat
    driver.quit()

#Case 1 : “Tobeto İşte Başarı Modeli” Kontrolü
#Testi çözmeyen mail
def test_basarıModeliÇöz(browser):
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("alwin.ramesses@floodouts.com")
    password_input = browser.find_element(By.XPATH,  "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("123456")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    #Değerlendirmeler tıkla.
    değerlendirmeler_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/ul/li[3]/a")
    değerlendirmeler_button.click()
    sleep(3)
    #Değerlendirmelerim sayfasını doğrula
    degerlendirmelerim_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main")))
    #Başla butonuna tıkla
    basla_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a")
    basla_button.click()
    #  Kullanıcı değerlendirmeye başla butonunun olduğu bilgilendirme sayfasına ulaşmalısayfaya ulaşmalıdır.
    sınav_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div")))
    sleep(2)


#Case 2 : Sınavı çözme Kontrolü
def test_sınavEkranı(browser):
    test_basarıModeliÇöz(browser)
    # Değerlendirmeye başla butonuna tıkla.
    degerlendirmeye_basla_button = browser.find_element(By.XPATH,   "//*[@id='__next']/div/main/section/div/div/div/div[3]/a")
    browser.execute_script("arguments[0].click();", degerlendirmeye_basla_button)
    sleep(3)
    # sınav ekranı
    sınav_ekranı = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div")))
    result_text = sınav_ekranı.text
    print("Result Text:", result_text)

#Testi çözen mail ile test edildi
def test_raporGoruntule(browser):
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("christoper.wylder@floodouts.com")
    password_input = browser.find_element(By.XPATH,  "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("123456")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # Değerlendirmeler tıkla.
    değerlendirmeler_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/ul/li[3]/a")
    değerlendirmeler_button.click()
    sleep(3)
    # Değerlendirmelerim sayfasını doğrula
    degerlendirmelerim_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main")))
    # Rapor görüntüle butonuna tıkla
    rapor_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a")
    rapor_button.click()
    #  Rapor sayfası
    rapor_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section")))
    sleep(2)
    result_text = rapor_ekranı.text
    print("Result Text:", result_text)


#Case 3 : Çoktan Seçmeli Testlerin Rapor Görüntülenmesi
#Sınava girmeyen mail ile test edildi
def test_çoktanSeçmeliRapor(browser):
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("alwin.ramesses@floodouts.com")
    password_input = browser.find_element(By.XPATH,    "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("123456")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # Değerlendirmeler tıkla.
    değerlendirmeler_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/ul/li[3]/a")
    değerlendirmeler_button.click()
    sleep(3)
    # Değerlendirmelerim sayfasını doğrula
    degerlendirmelerim_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section[2]")))
    # Girilecek bir sınav seç. Input: Front End  Seçilen sınav metninin içerisinde bulunan başla butonuna tıkla.
    frontEnd_basla_button = browser.find_element(By.XPATH,   "//*[@id='__next']/div/main/section[2]/div/div/div[4]/div/div[1]/button")
    browser.execute_script("arguments[0].click();", frontEnd_basla_button)
    sleep(2)
#Sınavı tamamlayan mail ile test edildi
def test_çoktanSeçmeliRapor2(browser):
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("christoper.wylder@floodouts.com")
    password_input = browser.find_element(By.XPATH,    "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("123456")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # Değerlendirmeler tıkla.
    değerlendirmeler_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/ul/li[3]/a")
    değerlendirmeler_button.click()
    sleep(3)
    # Değerlendirmelerim sayfasını doğrula
    degerlendirmelerim_ekranı = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main")))
    sleep(3)
    # Gireln front end sınavının raporunu görüntüle tıkla
    goruntule_button = browser.find_element(By.XPATH,  "//*[@id='__next']/div/main/section[2]/div/div/div[4]/div/div[1]/button")
    browser.execute_script("arguments[0].click();", goruntule_button)
    sleep(2)
    # Rapor sayfasını doğrula
    rapor_ekranı = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div")))
    sleep(3)
    result_text = rapor_ekranı.text
    print("Result Text:", result_text)
    sleep(3)






















