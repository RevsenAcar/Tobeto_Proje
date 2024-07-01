from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    # Webdriver'ı başlat
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Test tamamlandıktan sonra tarayıcıyı kapat
    driver.quit()

def test_profil(browser, dropdown=None):
    # Adım 1: Basarili giris yap.
    browser.get("https://tobeto.com/giris")
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("davy.acxel@floodouts.com")
    password_input = browser.find_element(By.XPATH,
                                          "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("369369")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    sleep(4)
    # Adim 2: 'Profilim" alanindan profil bilgilerim butonuna tikla.
    profilalani = browser.find_element(By.XPATH, "//*[@id='__next'] / div/nav/div[1]/div/div/div[2]/button").click()
    profilbilgileri = browser.find_element(By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a").click()

    # Adım 3: “Adınız” alanına adını gir
    browser.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input").clear()
    sleep(1)
    adiniz = browser.find_element(By.NAME, "name").send_keys("PANDA")
    sleep(1)
    # Adım 4: “Soyadınız” alanına soyadını gir.
    browser.find_element(By.NAME,"surname").clear()
    sleep(1)
    soyadiniz = browser.find_element(By.NAME, "surname").send_keys("PAIR")
    sleep(1)
    # Adım5: Telefon numarası kısmından ülke kodu alanından inputu seç.
    ulke_kodu = browser.find_element(By.NAME, "phoneNumberCountry").click()
    alan_kodu = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/div/div/select/option[223]').click()

    # Adım6: “Telefon Numaranız” alanına numara gir.
    browser.find_element(By.XPATH, '//*[@id="phoneNumber"]').clear()
    telefon_numaraniz = browser.find_element(By.XPATH, '//*[@id="phoneNumber"]').send_keys(+905556652655)
    sleep(1)
    # Adım7: “Doğum Tarihiniz” alanına inputu gir ya da takvim işaretine tıkla takvimden seç.
    dogum_tarihiniz= browser.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/input").send_keys(12121990)
    sleep(1)
    # Adım8: “T.C. Kimlik No” ve ‘Ülke’ alanını gir.
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    identifier_input = browser.find_element(By.NAME, 'identifier')
    identifier_input.clear()               #EN AZ 11 KARAKTER GIREBILIRSINIZ DIYOR AMA 11DEN FAZLA GIRMEYE IZIN VERMIYOR
    eleven_digit_number = ''
    identifier_input.send_keys(eleven_digit_number)
    entered_value = identifier_input.get_attribute('value')
    sleep(10)
    browser.execute_script("window.scrollBy(0, 500)")

    buton = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button").click()

    sleep(10)

    assert "Satın alınan eğitimlerin faturası için doldurulması zorunlu alan." in browser.page_source
    # HATA METNI DEGISMIS
