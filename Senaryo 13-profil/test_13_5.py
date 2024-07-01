from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
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
@pytest.mark.skip()
def test_profil(browser, dropdown=None):
    # Adım 1: Basarili giris yap.
    browser.get("https://tobeto.com/giris")
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("sevalcagdas4@gmail.com")
    password_input = browser.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("Dolunay13")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    sleep(4)
    # Adim 2: 'Profilim" alanindan profil bilgilerim butonuna tikla.
    profilalani = browser.find_element(By.XPATH, "//*[@id='__next'] / div/nav/div[1]/div/div/div[2]/button").click()
    profilbilgileri = browser.find_element(By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a").click()

   
    #Adım11: “Mahalle / Sokak” alanına bilgileri gir.
    browser.execute_script("window.scrollBy(0, 500)")   #Sayfa kaymadigindan bulamiyor
    mahalle_sokak = browser.find_element(By.NAME, "address").send_keys("CİHAN mah Kür sokSncashdashdncaschjdbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbhhhhhhhhhhhhhhhhhhhhhhhhhhhhhheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

    sleep(10)
    assert  "En fazla 200 karakter girebilirsiniz" in browser.page_source
    #Adım 12: “Hakkımda” alanına bilgileri gir.
    hakkinda = browser.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[16]/textarea")
    sleep(3)
    hakkinda.send_keys("Yazılım Test mühendisliği alanında Tobetoda eğitim alıyorum.ojskajsdkajsdjakjdkjaskdjajdkascnsjdjasdhasjdhasjdhjashdjahdjahsjdhasdhaksjdjhjwehduehwjijsmwijdiwdnwidjqijdiwjeidjwidiwedjuewhfuwehfuwehfuehfuwehduwehduehuhduheuueudhuehwuhudheudo8jeijdfiefjdiwedjjqoweidjejdiejihfefheufhufhudhwpihdjufhueifheuhfeuhfeiruhfuehwufheruhfeufhuefhuehfuefhuehfnmnmmmmmmmmmmmmmm")
    sleep(2)
    assert "En fazla 300 karakter girebilirsiniz" in browser.page_source
    
   

    
    
