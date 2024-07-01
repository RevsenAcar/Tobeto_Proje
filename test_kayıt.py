import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # WebDriver'ı başlat
    yield driver  # Testlerin çalışmasını beklet
    # Tarayıcı penceresini tam ekran yap
    driver.quit()  # WebDriver'ı kapat

def test_kayıt(browser):
    
    #  Kayıt sayfasına git
    browser.get("https://tobeto.com/giris")
    # Kayıt butonuna tıkla
    kayit_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[3]/button[2]")
    kayit_button.click()
    # Kayıt formunun açıldığını kontrol et
    kayit_form = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div")
    assert kayit_form.is_displayed()
    #Kayıt bilgilerini doldurma
    ad_input = browser.find_element(By.NAME, "firstName")
    ad_input.send_keys("Test2")
    soyad_input = browser.find_element(By.NAME, "lastName")
    soyad_input.send_keys("Kullanıcı")
    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("test@gmail.com")
    sifre_input = browser.find_element(By.NAME, "password")
    sifre_input.send_keys("123456")
    sifre_tekrar_input = browser.find_element(By.NAME, "passwordAgain")
    sifre_tekrar_input.send_keys("123456")
    kayıtOl_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/button")))
    browser.execute_script("arguments[0].click();", kayıtOl_button)

    # Beklenen Sonuç: Kayıt ol butonuna tıkladıktan sonra kayıt oluşturmak için sözleşmeler başlıklı bir pop-up açılmalıdır.
    popup_title = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div")))

    # Kişisel rıza metni checkbox'ını işaretle
    riza_checkbox = browser.find_element(By.NAME, "contact")
    riza_checkbox.click()
    assert riza_checkbox.is_displayed()
    # Üyelik sözleşmesi ve kullanım koşulları checkbox'larını işaretle
    sozlesme_checkbox = browser.find_element(By.NAME, "membershipContrat")
    sozlesme_checkbox.click()
    # "E-posta gönderim izni" checkbox'ını işaretle
    email_izin_checkbox = browser.find_element(By.NAME, "emailConfirmation")
    email_izin_checkbox.click()
    # "Arama izni" checkbox'ını işaretle
    arama_izin_checkbox = browser.find_element(By.NAME, "phoneConfirmation")
    arama_izin_checkbox.click()
    #  Arama iznine tıklandıktan sonra açılan telefon numarası alanını doldur.
    telefon_input = browser.find_element(By.ID, "phoneNumber")
    telefon_input.send_keys("+90 9909909900")
    # # Google ReCAPTCHA iframe'i bul
    # iframe = WebDriverWait(browser, 10).until(
    #     EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
    # # "Ben robot değilim" checkbox'ını işaretle
    # robot_checkbox = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "recaptcha-anchor")))
    # robot_checkbox.click()
    # # "Devam" butonunu bul ve tıkla
    # devam_button = WebDriverWait(browser, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/button[2][text()='Devam Et']")))

    # # Ana frame'e geri dön
    # browser.switch_to.default_content()
    # Beklenen Sonuç: KAYIT BAŞARILI YAZISININ OLDUĞU SAYFA AÇILMALI
    browser.get("https://tobeto.com/e-posta-dogrulama?registerType=registerForm")
    
    # Başarı mesajını bul
    basari_mesaji = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/div/span")

    # Mesajları alırken <br> etiketleriyle ayrılmış olduğunu varsayarak, metni <br> etiketleriyle böler
    mesajlar = basari_mesaji.get_attribute("innerHTML").split("<br>")

    # Tüm mesajları birleştir
    birlesik_mesaj = " ".join(mesajlar)

    # İstenen metnin kontrol edilmesi
    assert birlesik_mesaj == "Tobeto Platform'a kaydınız başarıyla gerçekleşti. Giriş yapabilmek için e-posta adresinize iletilen doğrulama linkine tıklayarak hesabınızı aktifleştirin."




#Case 2: Kayıt Ol Sırasında İstenen Telefon Numarası Karakter Kontrolü
@pytest.mark.skip()
def test_hatali_register(browser):
    #  Kayıt sayfasına git
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kayıt butonuna tıkla
    kayit_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[3]/button[2]")
    kayit_button.click()
    # Kayıt formunun açıldığını kontrol et
    kayit_form = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div")
    assert kayit_form.is_displayed()
    #Kayıt bilgilerini doldurma
    ad_input = browser.find_element(By.NAME, "firstName")
    ad_input.send_keys("Bahar")
    soyad_input = browser.find_element(By.NAME, "lastName")
    soyad_input.send_keys("Kaya")
    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("bahar@gmail.com")
    sifre_input = browser.find_element(By.NAME, "password")
    sifre_input.send_keys("123456")
    sifre_tekrar_input = browser.find_element(By.NAME, "passwordAgain")
    sifre_tekrar_input.send_keys("123456")
    kayıtOl_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable( (By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/button")))
    browser.execute_script("arguments[0].click();", kayıtOl_button)
    # Beklenen Sonuç: Kayıt ol butonuna tıkladıktan sonra kayıt oluşturmak için sözleşmeler başlıklı bir pop-up açılmalıdır.
    popup_title = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div")))
    # Kişisel rıza metni checkbox'ını işaretle
    riza_checkbox = browser.find_element(By.NAME, "contact")
    riza_checkbox.click()
    assert riza_checkbox.is_displayed()
    # Üyelik sözleşmesi ve kullanım koşulları checkbox'larını işaretle
    sozlesme_checkbox = browser.find_element(By.NAME, "membershipContrat")
    sozlesme_checkbox.click()
    # "E-posta gönderim izni" checkbox'ını işaretle
    email_izin_checkbox = browser.find_element(By.NAME, "emailConfirmation")
    email_izin_checkbox.click()
    # "Arama izni" checkbox'ını işaretle
    arama_izin_checkbox = browser.find_element(By.NAME, "phoneConfirmation")
    arama_izin_checkbox.click()
    #  Arama iznine tıklandıktan sonra açılan telefon numarası alanını doldur.
    telefon_input = browser.find_element(By.ID, "phoneNumber")
    telefon_input.send_keys("444")
    # Google ReCAPTCHA iframe'i bul
    iframe = WebDriverWait(browser, 10).until(
       EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
    # "Ben robot değilim" checkbox'ını işaretle
    robot_checkbox = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "recaptcha-anchor")))
    robot_checkbox.click()
    # Ana frame'e geri dön
    browser.switch_to.default_content()
    
    # "Devam" butonunu bul ve tıkla
    devam_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/button[2][text()='Devam Et']")))
    browser.execute_script("arguments[0].click();", devam_button)
    
    success_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div/div/label[4]/small/p")))
    assert "En az 10 karakter girmelisiniz." in success_message.text

#Case 3 : Geçersiz E-posta Kontrolü
def test_hatalimail_register(browser):
    #  Kayıt sayfasına git
    browser.get("https://tobeto.com/giris")
    # Kayıt butonuna tıkla
    kayit_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[3]/button[2]")
    kayit_button.click()
    # Kayıt formunun açıldığını kontrol et
    kayit_form = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div")
    assert kayit_form.is_displayed()
    #Kayıt bİlgilerini doldurma
    ad_input = browser.find_element(By.NAME, "firstName")
    ad_input.send_keys("Test3")
    soyad_input = browser.find_element(By.NAME, "lastName")
    soyad_input.send_keys("Kullanıcı")
    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("t")
    errorMessage = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/form/p")
    assert errorMessage.text == "Geçersiz e-posta adresi*"
    

#Case 4 : Girdiğiniz E Posta Adresi İle Kayıtlı Üyelik Bulunmaktadır Uyarısının Alınması
#Case 5: Şifrenin Karakter Sayı Kontrolü
#Case 6: Şifre Tekrarı Kontrolü
#Case 7: Girilen Bilgilerde 2 Farklı Hatalı Kısım Olduğunda








