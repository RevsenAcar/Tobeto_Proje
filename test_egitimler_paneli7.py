
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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


def test_egitimlerim(browser):

        #  Sitenin giriş sayfasına git
        browser.get("https://tobeto.com/giris")
        browser.maximize_window()
        # Kullanıcı adı ve şifre girme işlemi
        email_input = browser.find_element(By.XPATH,
                                           "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
        email_input.send_keys("sevalcagdas4@gmail.com")
        password_input = browser.find_element(By.XPATH,
                                              "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
        password_input.send_keys("Dolunay13")
        login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
        login_button.click()
        # Platform açılmalıdır.
        platform_title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
        # Eğitimlerim butonuna tıklamadan önce bekleme işlemi
        egitim_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "lessons-tab")))
        # Eğitimlerim butonuna tıklamadan önce ekranı kaydırma
        actions = ActionChains(browser)
        actions.move_to_element(egitim_button).perform()
        # Eğitimlerim butonuna tıklama
        egitim_button.click()
        #  Eğitimleri kontrol et
        egitim_sayisi = len(browser.find_elements(By.XPATH, "//div[contains(@class, 'egitim')]"))
        assert egitim_sayisi <= 4, "Kullanıcıya en fazla 4 eğitim gösterilmelidir."
        # Daha Fazla Göster butonuna tıkla. Kullanıcı kendisine tanımlanan bütün eğitimleri görüntüleyebilmelidir.
        daha_fazla_goster_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='lessons-tab-pane']/div/div/div[2] ")))
        browser.execute_script("arguments[0].click();", daha_fazla_goster_button)
        # Ders ekranının açıldığını doğrula
        ders_ekranı = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/div/div/div/span")))
        # Ders ekranındaki öğeleri yazdırıyor.Sayfa başlığında Eğitimlerim yazmalı.
        result_text = ders_ekranı.text
        print("Result Text:", result_text)
        sleep(5)

@pytest.mark.skip()
#Case 2: Kullanıcıya Atanan Eğitim İçeriklerinin Kontrolü(!!!her girmede favoriye ekleyip çıkardığı için mesaj  uyuşmaybiliyor.Favoriye eklediğine emin ol)
def test_egitimetıkla(browser):
    test_egitimlerim(browser)
    #  Sayfayı aşağı  kaydır
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.2);")

    #Eğitime  gittıkla
    egitim_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/button")))
    browser.execute_script("arguments[0].click();", egitim_button)
    sleep(3)

    ders_ekranı = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='wrapper-content']")))
    sleep(5)
    #Sayfa açıldıysa Dr. Ecmel Ayral'dan Hoşgeldin Mesajı görünmeli.
    result_text = ders_ekranı.text
    print("Result Text:", result_text)

    sleep(5)

    #Favorilere ekle butonuna tıkla
    favori_button= WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='dynamicContent']/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[4]/div/span")))
    browser.execute_script("arguments[0].click();", favori_button)
    sleep(3)

    #Renk değişikliğini test et
    # Butonun sınıfını kontrol ederek favori ekleme işleminin başarılı olduğunu doğrulayın
    WebDriverWait(browser, 10).until( EC.element_to_be_clickable((By.XPATH, "//*[@class='remove-favorite']")))

    # Favorilere ekleme başarılı uyarısını kontrol edin
    success_message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='wrapper-content']/div[2]/div/div")))
    assert success_message.text == "Favorilere ekleme işlemin başarıyla gerçekleşti."
    sleep(3)

    #Kalp butonuna tıkla
    kalp_icon = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "like-button")))
    browser.execute_script("arguments[0].click();", kalp_icon)
    sleep(2)

    # İçerik butonuna tıkla
    icerik_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='rc-tabs-0-tab-content']/div/span")))
    browser.execute_script("arguments[0].click();", icerik_button)
    sleep(2)

    #İcerik sayfasının görünürlüğünü kontrol et
    icerik_ekranı = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='rc-tabs-0-panel-content']/div/div/div[1]")))
    sleep(5)

    # Sayfa açıldıysa Dr. Ecmel Ayral'dan Hoşgeldin Mesajı görünmeli.
    result_text = icerik_ekranı.text
    print("Result Text:", result_text)
    sleep(2)

    # Hakkında butonuna tıkla
    hakkımda_button =WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='rc-tabs-0-tab-about']/div/span")))
    browser.execute_script("arguments[0].click();", hakkımda_button)
    sleep(2)

    # Hakkında sayfasının görünürlüğünü kontrol et
    hakkında_ekranı = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='dynamicContent']/div/div[2]/div")))
    sleep(5)

    # Sayfa açıldıysa
    result_text = hakkında_ekranı.text
    print("Result Text:", result_text)
    sleep(2)

    browser.back()

    # Detay butonuna tıkla
    detay_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='activity-unit-detail']/div/div[2]/div/div/div[2]/button")))
    browser.execute_script("arguments[0].click();", detay_button)
    sleep(2)

    # Detay sayfasının görünürlüğünü kontrol et
    detay_ekranı = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div[3]/div/div/div/div/div[1]/div/div")))
    sleep(5)

    # Sayfa açıldıysa
    result_text = detay_ekranı.text
    print("Result Text:", result_text)
    sleep(3)

    #Eğitime git butonuna tıkla
    egittimeGit_button = WebDriverWait(browser, 10).until( EC.visibility_of_element_located( (By.XPATH, "//*[@id='activity-unit-detail']/div/div[2]/div/div/div[2]/button")))
    browser.execute_script("arguments[0].click();", egittimeGit_button)
    sleep(2)

    # Detay sayfası kapanmalı
    ders_ekranı = WebDriverWait(browser, 20).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='wrapper-content']")))
    sleep(5)
    # Sayfa açıldıysa Dr. Ecmel Ayral'dan Hoşgeldin Mesajı görünmeli.
    result_text = ders_ekranı.text
    print("Result Text:", result_text)
    sleep(3)

    #Detay butonuna tıkla
    detay_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located( (By.XPATH, "//*[@id='activity-unit-detail']/div/div[2]/div/div/div[2]/button")))
    browser.execute_script("arguments[0].click();", detay_button)
    sleep(2)

    # Detay sayfasının görünürlüğünü kontrol et
    detay_ekranı = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div[3]/div/div/div/div/div[1]/div/div")))
    sleep(5)

    # Çarpı işaretine bas
    carpı_button = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div[3]/div/div/div/a")))
    browser.execute_script("arguments[0].click();", carpı_button)
    sleep(2)

    # Detay sayfası kapanmalı
    ders_ekranı = WebDriverWait(browser, 20).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='wrapper-content']")))
    sleep(5)
    # Sayfa açıldıysa Dr. Ecmel Ayral'dan Hoşgeldin Mesajı görünmeli.
    result_text = ders_ekranı.text
    print("Result Text:", result_text)
    sleep(3)

#Case 3: Eğitimin Tamamlanması 
def test_egitimTamamlama(browser):
    test_egitimlerim(browser)
    # Eğitime tıkla
    egitim_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[13]/div/div[2]/button")))
    browser.execute_script("arguments[0].click();", egitim_button)
    sleep(3)
    #Ders ekranının açıldığını doğrula
    ders_ekranı = WebDriverWait(browser, 20).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='dynamicContent']/div")))
    sleep(5)

    result_text = ders_ekranı.text
    print("Result Text:", result_text)
    sleep(5)

    # Dersin oynatma düğmesini bulun ve tıklayın
    oynatma_düğmesi = ders_ekranı.find_element(By.XPATH,  "//*[@id='my-player']/button")
    oynatma_düğmesi.click()

    sleep(5)

#Case 4: Eğitimlerim Sayfası’nda Arama Yapılması
def test_egitimArama(browser):
    test_egitimlerim(browser)
    #Arama kutusu bul
    arama_kutusu = browser.find_element(By.ID, "search")
    # Arama kutusuna veriyi gönder
    arama_kutusu.send_keys("Dr. Ecmel ")
    #Arama sonucu görüntülendiğini doğrula
    egitim_ekranı = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div")))
    sleep(3)
    #Ecmel Ayral ders kutucuğundaki içerikler yazılmalı.
    result_text = egitim_ekranı.text
    print("Result Text:", result_text)
    sleep(3)

def test_egitimArama2(browser):
    test_egitimlerim(browser)

    # Kurum Seçiniz kutusunu bulun ve tıklayın
    kurum_seciniz_kutusu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-select-2-input']")))
    kurum_seciniz_kutusu.click()

    # Karakterleri girin
    kurum_seciniz_kutusu.send_keys("İst")

    sleep(5)

def test_egitimArama3(browser):
    test_egitimlerim(browser)
    # En sağda bulunan sıralama kutusuna tıkla.

    # Sıralama kutusunu bulun ve tıklayın
    siralama_kutusu = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='react-select-3-input']")))
    siralama_kutusu.click()
    sleep(3)

    # Belirli bir sıralama türünü seçmek için XPath ifadesini oluşturun ve tıklayın
    siralama_turu_secimi = WebDriverWait(browser, 10).until( EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[3]/div/div")))
    siralama_turu_secimi.click()
    sleep(3)











