from time import sleep, time
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

#Case 1 : İşte Başarı Modeli Testine Erişim
def test_basarıModeliTesteErisim(browser):
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
    # Hoşgeldiniz panelinde scroll'u aşağı kaydır, kendini değerlendir bölümünde bulunan başla butonuna tıkla.
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.5);")
    #  Kendini değerlendir başla butonuna tıkla
    degerlendir_basla_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[2]/div/button ")))
    browser.execute_script("arguments[0].click();", degerlendir_basla_button)
    sleep(2)
    # Beklenen Sonuç: Değerlendirmeler sayfasına ulaşılmalıdır
    degerlendirmeler_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div")))
    sleep(3)
    #Başla butonuna tıkla
    basla_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a")))
    browser.execute_script("arguments[0].click();", basla_button)
    sleep(2)
    #Değerlendirme ekranının açıldığını doğrula
    degerlendirme_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div")))
    #Tobeto İşte Başarı Modeli açıklama sayfası açılmalı.
    result_text = degerlendirme_ekranı.text
    print("Result Text:", result_text)
    sleep(2)
    #Beklenen Sonuç : Test sonucunda kullanıcıya ait "Analiz Raporu" görüntülenmelidir.
    #SINAV TAMAMLANINCA RAPOR GÖRÜNTÜLE BUTONU ÇIKIYOR İKİSİNİ AYNI YERDE TEST EDEMEDİM

#Case 2 : Analiz Raprou Görüntüleme
def test_analizRaporGoruntule(browser):
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
    # Hoşgeldiniz panelinde scroll'u aşağı kaydır, kendini değerlendir bölümünde bulunan başla butonuna tıkla.
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.5);")
    #  Kendini değerlendir başla butonuna tıkla
    degerlendir_basla_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[2]/div/button ")))
    browser.execute_script("arguments[0].click();", degerlendir_basla_button)
    sleep(2)
    # Beklenen Sonuç: Değerlendirmeler sayfasına ulaşılmalıdır
    degerlendirmeler_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div")))
    sleep(3)
    #Rapor görüntüle butonuna tıkla
    rapor_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a")))
    browser.execute_script("arguments[0].click();", rapor_button)
    sleep(2)
    #Rapor ekranında olduğunu doğrula
    rapor_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div/div")))
    #Tobeto ”İşte Başarı Modeli”Analiz Raporum başlığı görüntülenmeli
    result_text = rapor_ekranı.text
    print("Result Text:", result_text)
    sleep(2)

#Beklenen Sonuç : Kullanıcı 8 yetkinlik üzerinden test sonucunu görüntüleyebilmelidir. Her yetkinliğe
#ayrı bir renk atanmış olmalıdır. Sınav sonucu her yetkinlik için 5 puan üzerinden değerlendirilmeli ve
#renkli kutunun içerisinde bu değerlendirmeye ait puan yazmalıdır. Kullanıcı ayrıca test sonucunu grafik
#ile görüntüleyebilmelidir. Grafik üzerinde her değerlendirmenin rengi nokta ile işaretlenmeli ve
#noktanın üzerine gelindiğinde o değerlendirmeye ait puan görüntülenmelidir.(NOKTALARIN ÜZERİNE GELEMEDİM)

#Case 3 : Yetkinlik Detaylarına Ait Alt Başlıkların Açılır Pencerede Görüntülenmesi
def test_yetkinlik_pencesi(browser):
    test_analizRaporGoruntule(browser)

    #Her yetkinliğin altında bulunan, "Bu yetkinlik nedir ve neden önemli”, "Geliştirmek için ne yapmalı" ve "Bu Alanda önerilen eğitimler" alt başlıkları görüntülemek için açılır kapanır
    #pencere butonlarına tıkla.

    #  Sayfayı aşağı  kaydır
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.2);")
    sleep(2)

    #Bu yetkinlik nedir ve neden önemli? butonu tıkla
    yetkinlik_button =browser.find_element(By.XPATH, "//*[@id='heading8']/button")
    yetkinlik_button.click()
    sleep(2)

    #Yetkinlik penceresinin açıldığını doğrula
    yetkinlik_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='collapse8']/div")))
    # Yetkinlik penceri açıldığındaki yazılar gözükmeli
    result_text = yetkinlik_ekranı.text
    print("Result Text:", result_text)
    sleep(2)

def test_gelistirme_pencesi(browser):
    test_analizRaporGoruntule(browser)
    #  Sayfayı aşağı  kaydır
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.2);")
    sleep(2)

    # Geliştirmek için ne yapmalı? butonu tıkla
    gelistirme_button = browser.find_element(By.XPATH, "//*[@id='heading28']/button")
    gelistirme_button.click()
    sleep(2)

    # Geliştirme penceresinin açıldığını doğrula
    gelistirme_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='collapse28']/div")))

    result_text = gelistirme_ekranı.text
    print("Result Text:", result_text)
    sleep(2)

    #BU ADIMDA TEKRAR BUTONA BASINCA PENCERE KAPANIYOR (TEST)
    # Geliştirmek için ne yapmalı? butonu tıkla
    gelistirme_button = browser.find_element(By.XPATH, "//*[@id='heading28']/button")
    gelistirme_button.click()
    sleep(2)

def test_onerilenEgitimler_pencesi(browser):
    test_analizRaporGoruntule(browser)
    #  Sayfayı aşağı  kaydır
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.2);")
    sleep(2)

    # Bu alanda önerilen eğitimler butonu tıkla
    oneri_button = browser.find_element(By.XPATH, "//*[@id='hheading8']/button")
    oneri_button.click()
    sleep(2)

    # Öneri eğitimler penceresinin açıldığını doğrula
    oneri_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='ccollapse8']/div")))

    #Önerilen eğitim alanları boş o yüzden yazı çıkmıyor
    result_text = oneri_ekranı.text
    print("Result Text:", result_text)
    sleep(2)






































