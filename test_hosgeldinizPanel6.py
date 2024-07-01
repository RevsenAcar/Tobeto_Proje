import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

#Case 1: Hoşgeldiniz Paneli’ne Yönlendirme
def test_giris(browser):
        #Sitenin giriş sayfasına git
        browser.get("https://tobeto.com/giris")
        browser.maximize_window()
        # Kullanıcı adı ve şifre girme işlemi
        email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
        email_input.send_keys("sevalcagdas4@gmail.com")
        password_input = browser.find_element(By.XPATH,   "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
        password_input.send_keys("Dolunay13")
        login_button = browser.find_element(By.XPATH,      "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
        login_button.click()
        # Sayfanın yönlendirilmesini bekleyerek URL kontrolü yap
        platform_url = "https://tobeto.com/platform"
        WebDriverWait(browser, 20).until(EC.url_to_be(platform_url))


#Case 2: Hoşgeldiniz Paneli’nin Kontrolü
def test_panel(browser):
    #  Sitenin giriş sayfasına git
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
    platform_title = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # Eğitimlerim butonuna tıklamadan önce bekleme işlemi
    egitim_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "lessons-tab")))
    # Eğitimlerim butonuna tıklamadan önce ekranı kaydırma
    actions = ActionChains(browser)
    actions.move_to_element(egitim_button).perform()
    # Eğitimlerim butonuna tıklama
    egitim_button.click()
    # Eğitimlerim butonuna tıklandıktan sonra beklenen sayfanın açılması
    # “Hoşgeldin Mesajı” sekmesinin varlığı kontrol ediliyor
    hosgeldin_mesaji = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[1]")))
    assert hosgeldin_mesaji.is_displayed(), "Hoşgeldin Mesajı bulunamadı veya görünür değil."
    # “Eğitimlere nasıl katılırım?” sekmesinin varlığı kontrol ediliyor
    katilim_sekmesi = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[2]/div/div[2]/div/span[1]")))
    assert katilim_sekmesi.is_displayed(), "Eğitimlere Nasıl Katılırım? sekmesi bulunamadı veya görünür değil."
    #Herkes için kodlama sekmesi
    kodlama_sekmesi = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[3]/div/div[2]/div/span[1]")))
    assert kodlama_sekmesi.is_displayed(), "Herkes İçin Kodlama sekmesi bulunamadı veya görünür değil."
    #Hoşgeldin Buluşması sekmesi
    bulusma_sekmesi = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[4]/div/div[2]/div/span[1]")))
    assert bulusma_sekmesi.is_displayed(), "Hoşgeldin Buluşması sekmesi bulunamadı veya görünür değil."
    #Daha fazla göster butonu
    daha_fazla_goster_butonu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lessons-tab-pane']/div/div/div[2]")))
    assert daha_fazla_goster_butonu.is_displayed(), "Daha fazla göster butonu bulunamadı veya tıklanabilir değil."
    # "Duyuru ve Haberlerim" butonuna tıkla
    duyuru_ve_haberler_butonu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "notification-tab")))
    duyuru_ve_haberler_butonu.click()
   # Beklenen Sonuç: Güncel duyuru haberlerini kontrol et
   #assert len(guncel_duyurular) > 0 bu ifade güncel duyuru haberlerinin varlığını kontrol eder.
    guncel_duyurular = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='notification-tab-pane']/div")))
    assert len(guncel_duyurular) > 0, "Güncel duyuru haberleri bulunamadı."
    # Daha fazla göster butonu
    daha_fazla_goster_butonu = WebDriverWait(browser, 10).until( EC.element_to_be_clickable((By.XPATH, "// *[ @ id = 'notification-tab-pane'] / div / div[4]")))
    assert daha_fazla_goster_butonu.is_displayed(), "Daha fazla göster butonu bulunamadı veya tıklanabilir değil."
    # "Anketlerim" butonuna tıkla
    anketlerim_butonu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "mySurvey-tab")))
    anketlerim_butonu.click()
    # Beklenen Sonuç: Eğer kullanıcıya atanmış bir anket yoksa "Atanmış herhangi bir anketiniz bulunmamaktadır." sonucunu görmelidir
    atanmıs_anket = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mySurvey-tab-pane']/div/div")))
    assert atanmıs_anket.text == "Atanmış herhangi bir anketiniz bulunmamaktadır"
    time.sleep(3)



#Case 3: Sınavlarım Butonunun Kontrolü
def test_sınav(browser):
    test_giris(browser)
    time.sleep(2)
    #Sınavlarıma tıkla.
    # Class ögesini bulun ve üzerine tıklayın
    sınav_element = WebDriverWait(browser, 10).until( EC.element_to_be_clickable((By.CLASS_NAME, "exam-card  ")))
    browser.execute_script("arguments[0].click();", sınav_element)
    # Sonuç ekranının açıldığını doğrulayın
    sonuc_ekranı = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div")))
    # Sonuç ekranındaki öğeleri yazdırıyor.
    result_text = sonuc_ekranı.text
    print("Result Text:", result_text)
    # Raporu görüntüle butonuna tıkla.
    rapor_button = WebDriverWait(browser, 10).until( EC.element_to_be_clickable(  (By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/div[2]/button ")))
    browser.execute_script("arguments[0].click();", rapor_button)
    # Rapor ekranının açıldığını doğrulayın
    rapor_ekranı = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div/div")))
    # Rapor ekranındaki öğeleri yazdırıyor.
    result_text = rapor_ekranı.text
    print("Result Text:", result_text)
    time.sleep(3)
    #Kapat butonuna tıkla
    kapat_button = WebDriverWait(browser, 10).until( EC.element_to_be_clickable(  (By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[2]/button ")))
    browser.execute_script("arguments[0].click();", kapat_button)

    # Pop-up'ın kapatıldığını doğrulayın
    try:
        WebDriverWait(browser, 5).until_not(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div/div")))
        print("Pop-up kapatıldı.")
    except TimeoutException:
        print("Pop-up kapatılamadı veya kapatılması uzun sürdü.")

#Case 4: Kişisel Alan Kontrolu
def test_kisiselAlan(browser):
    test_giris(browser)
    # Sayfanın en altına in
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Scroll işlemi tamamlanması için bir süre bekle
    #  Profili oluştur başla butonuna tıkla
    profil_basla_button = WebDriverWait(browser, 10).until( EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[4]/div/div/div[1]/div/button ")))
    browser.execute_script("arguments[0].click();", profil_basla_button)
    # Beklenen Sonuç: Profil sayfasına ulaşılmalıdır
    assert "profilim/profilimi-duzenle/kisisel-bilgilerim" in browser.current_url
    time.sleep(5)
    # Önceki sayfaya geri dön
    browser.back()
    time.sleep(5)
    #  Kendini değerlendir başla butonuna tıkla
    degerlendir_basla_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable( (By.XPATH, "//*[@id='__next']/div/main/div[1]/section[4]/div/div/div[2]/div/button ")))
    browser.execute_script("arguments[0].click();", degerlendir_basla_button)
    # Beklenen Sonuç: Değerlendirmeler sayfasına ulaşılmalıdır
    assert "https://tobeto.com/degerlendirmeler" in browser.current_url
    time.sleep(5)
    # Önceki sayfaya geri dön
    browser.back()
    time.sleep(5)
    #  Öğrenmeye başla butonuna tıkla
    ogrenme_basla_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[4]/div/div/div[3]/div/button ")))
    browser.execute_script("arguments[0].click();", ogrenme_basla_button)
    # Beklenen Sonuç:Katalog sayfasına ulaşılmalıdır
    assert "https://tobeto.com/platform-katalog" in browser.current_url #casede farklı url ama doğrusu bu
    time.sleep(5)
    # Önceki sayfaya geri dön
    browser.back()
    time.sleep(5)




































