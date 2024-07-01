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
#Açıklama : Kullanıcıların :“Kişisel Bilgilerim”, “Deneyimlerim”, “Eğitim Hayatım”, “Yetkinliklerim”,
#Sertifikalarım”, “Medya Hesaplarım”, “Yabancı Dillerim” ve “Ayarlar” başlıklarına erişebilmelerinin testi
#yapılacaktır.

def test_Kullanıcı_Profili_Oluşturma (browser):
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("alwin.ramesses@floodouts.com")
    password_input = browser.find_element(By.XPATH,   "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("123456")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    #  Profili oluştur başla butonuna tıkla
    profil_basla_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button ")))
    browser.execute_script("arguments[0].click();", profil_basla_button)
    sleep(2)
    platform_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div")))
    sleep(2)
    #Kişisel Bilgilerim,Deneyimlerim,Eğitim Hayatım,Yetkinliklerim,Sertifikalarım,
    # Üye Topluluklar,Projeler ve Ödüller,Medya Hesaplarım,Yabancı Dillerim,Ayarlar sekmesi görünmeli
    result_text = platform_title.text
    print("Result Text:", result_text)

    #Deneyimlerim başlığına tıkla
    deneyim_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2] ")))
    browser.execute_script("arguments[0].click();", deneyim_button)
    sleep(2)
    #Beklenen Sonuç: ‘Deneyimlerim’ başlığının olduğu alanının açılması.
    deneyim_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div")))
    sleep(2)
    result_text = deneyim_title.text
    print("Result Text:", result_text)

    # Eğitim Hayatım başlığına tıkla.
    egitim_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, " //*[@id='__next']/div/main/section/div/div/div[1]/div/a[3]")))
    browser.execute_script("arguments[0].click();", egitim_button)
    sleep(2)
    #Beklenen Sonuç: ‘Eğitim Hayatım’ başlığının olduğu alanının açılması.
    egitim_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div")))
    sleep(2)
    result_text = egitim_title.text
    print("Result Text:", result_text)

    #  Yetkinliklerim başlığına tıkla başlığına tıkla.
    yetkinlik_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[4] ")))
    browser.execute_script("arguments[0].click();", yetkinlik_button)
    sleep(2)
    #Beklenen Sonuç: ‘Yetkinliklerim’ başlığının olduğu alanının açılması.
    yetkinlik_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/div")))
    sleep(2)
    result_text = yetkinlik_title.text
    print("Result Text:", result_text)

    # Sertifikalarım başlığına tıkla başlığına tıkla.
    sertifika_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[5] ")))
    browser.execute_script("arguments[0].click();", sertifika_button)
    sleep(2)
    #Beklenen Sonuç: ‘Sertifikalarım’ başlığının olduğu alanının açılması.
    sertifika_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[2]/form/div[1]")))
    sleep(2)
    result_text = sertifika_title.text
    print("Result Text:", result_text)

    #  Üye Topluluklar başlığına tıkla başlığına tıkla.
    uyeTopluluk_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[6] ")))
    browser.execute_script("arguments[0].click();", uyeTopluluk_button)
    sleep(2)
    #Beklenen Sonuç: “Üye Topluluklar“ başlığının olduğu alanının açılması.
    uyeTopluluk_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div")))
    sleep(2)
    result_text = uyeTopluluk_title.text
    print("Result Text:", result_text)

    # Projeler ve Ödüller başlığına tıkla başlığına tıkla.
    proje_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[7] ")))
    browser.execute_script("arguments[0].click();", proje_button)
    sleep(2)
    #Beklenen Sonuç: “Proje ve Ödüller“ başlığının olduğu alanının açılması.
    proje_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div")))
    sleep(2)
    result_text = proje_title.text
    print("Result Text:", result_text)

    # Medya Hesaplarım başlığına tıkla başlığına tıkla.
    medya_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[8] ")))
    browser.execute_script("arguments[0].click();", medya_button)
    sleep(2)
    #Beklenen Sonuç: “Medya Hesaplarım“ başlığının olduğu alanının açılması.
    medya_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form")))
    sleep(2)
    result_text = medya_title.text
    print("Result Text:", result_text)

    #  Yabancı Dillerim başlığına tıkla başlığına tıkla.
    yabancıDil_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, " //*[@id='__next']/div/main/section/div/div/div[1]/div/a[9]")))
    browser.execute_script("arguments[0].click();", yabancıDil_button)
    sleep(2)
    #Beklenen Sonuç: “Yabancı Dillerim” başlığının olduğu alanının açılması.
    yabancıDil_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form")))
    sleep(2)
    result_text = yabancıDil_title.text
    print("Result Text:", result_text)

    # Ayarlar başlığına tıkla başlığına tıkla.
    ayarlar_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[10] ")))
    browser.execute_script("arguments[0].click();", ayarlar_button)
    sleep(2)
    #Beklenen Sonuç: ”Ayarlar” başlığının olduğu alanının açılması.
    ayarlar_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]")))
    sleep(2)
    result_text = ayarlar_title.text
    print("Result Text:", result_text)


















