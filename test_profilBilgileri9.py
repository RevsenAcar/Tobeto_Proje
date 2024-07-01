
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

#Case 1 : Profil Bilgileri Sayfasına Geçiş
def test_profil(browser):
    # Adım 1: Sitenin giriş sayfasına git
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("sevalcagdas4@gmail.com")
    password_input = browser.find_element(By.XPATH,       "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("Dolunay13")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # Profil sayfasına git
    profil_url = "https://tobeto.com/profilim"
    browser.get(profil_url)
    sleep(3)
    #Düzenle butonuna tıkla
    duzenle_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div/div/div[1]/div/div[2]/div[1]/div/span")
    duzenle_button.click()
    # Profil bilgileri sayfasına git
    kullanıcı_url = "https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim"
    browser.get(kullanıcı_url)
    sleep(5)

#Case 2: Profili Paylaş Butonunun Kontrolü
def test_profilPaylasma(browser):
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("sevalcagdas4@gmail.com")
    password_input = browser.find_element(By.XPATH,   "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("Dolunay13")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # Profil sayfasına git
    profil_url = "https://tobeto.com/profilim"
    browser.get(profil_url)
    sleep(3)
    # Paylaş butonuna tıkla
    paylas_button = browser.find_element(By.XPATH, "//*[@id='dropdown-basic']")
    paylas_button.click()
    #Profilimi paylaş penceresi açılmalı.
    profil_ekranı = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div/div/div[1]/div/div[2]/div[1]/div/div/div")))
    # Profilimi paylaş ekranı açılmalı.Profil linki yazısı görünmeli.
    result_text = profil_ekranı.text
    print("Result Text:", result_text)
    sleep(3)
    #  Açılan pencerede, “Profilimi paylaş” yazısının yanında bulunan açma-kapama tuşuna bas.
    #Beklenen Sonuç: Kullanıcı bu tuşa bastığı zaman, buton sağa kaymalı ve mor bir tik işareti çıkmalıdır.
    #Tekrar bastığında ise buton sola kaymalı gri renkli bir çarpı işareti çıkmalıdır.
    acKapa_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='__next']/div/main/div/div/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]")))
    browser.execute_script("arguments[0].click();", acKapa_button)
    sleep(2)
    #Link kopyalama butonuna bas.
    linkcopy_button=browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div/div/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/i")
    linkcopy_button.click()
    #Kopyalandığı doğrulanmalı

#Case 3: Sertifikalarım Bölümünün Kontrolü
def test_sertifilakalrım(browser):
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("sevalcagdas4@gmail.com")
    password_input = browser.find_element(By.XPATH,    "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("Dolunay13")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # Profil sayfasına git
    profil_url = "https://tobeto.com/profilim"
    browser.get(profil_url)
    sleep(3)
    #  Sayfayı aşağı  kaydır
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.5);")
    sleep(2)
    #Sertifika tıkla
    sertifika_element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div/div/div[2]/div/div[5]/div/div[2]/div/div")))
    browser.execute_script("arguments[0].click();", sertifika_element)
    sleep(3)
#Case 4: Medya Hesaplarım Bölümünün Kontrolü
def test_medyaHesapları(browser):
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("sevalcagdas4@gmail.com")
    password_input = browser.find_element(By.XPATH,   "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("Dolunay13")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # Profil sayfasına git
    profil_url = "https://tobeto.com/profilim"
    browser.get(profil_url)
    sleep(3)
    #Medya hesap tıkla.
    medya_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div/div/div[1]/div/div[2]/div[2]/div/span")))
    browser.execute_script("arguments[0].click();", medya_button)
    sleep(3)#Tıklanan hesabın sayfasına geçiş yapıyor.
#Case 5: “Tobeto İşte Başarı Modelim” Bölümünün Kontrolü
def test_basarıModeli(browser):
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
    # Profil sayfasına git
    profil_url = "https://tobeto.com/profilim"
    browser.get(profil_url)
    sleep(3)
    #  Sayfayı aşağı  kaydır
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.5);")
    sleep(2)
    # “Tobeto İşte Başarı Modelim” kısmındaki “Başla” butonuna tıkla.
    basla_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div/div/div[3]/div/div[5]/div/div[2]/div/a")))
    browser.execute_script("arguments[0].click();", basla_button)
    sleep(2)
    # Sonuç ekranının açıldığını doğrulayın
    sonuc_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div/div/h6")))
    # Sonuç ekranındaki öğeleri yazdırıyor.Başlık "Tobeto İşte Başarı Modeli"
    result_text = sonuc_ekranı.text
    print("Result Text:", result_text)
    

#Case5 :2.Beklenen sonuç :Değerlendirmenin profilde gözüktüğünü doğrula
def test_basarıModeli2(browser):
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("sevalcagdas4@gmail.com")
    password_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("Dolunay13")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # Profil sayfasına git
    profil_url = "https://tobeto.com/profilim"
    browser.get(profil_url)
    sleep(3)
    #  Sayfayı aşağı  kaydır
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.5);")
    sleep(2)
#Değerlendirme ekranının göründüğünü doğrula
    degerlendirme_ekranı = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div/div/div[3]/div/div[5]/div/div[2]")))
#Değerlendirme ekranındaki yazıları göster.
    result_text = degerlendirme_ekranı.text
    print("Result Text:", result_text)

#Case 6: “Aktivite Haritam” Bölümünün Kontrolü
#SAYFADA BULAMADIM




























