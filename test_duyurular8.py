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

#Case 1  Duyuru ve Haberlerim Kısmına Erişim Kontrolü
def test_duyurular(browser):
    # Sitenin giriş sayfasına git
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("sevalcagdas4@gmail.com")
    password_input = browser.find_element(By.XPATH,  "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("Dolunay13")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    #  Sayfayı aşağı  kaydır
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.5);")
    # "Duyuru ve Haberlerim" butonuna tıkla
    duyuru_ve_haberler_butonu = WebDriverWait(browser, 10).until( EC.element_to_be_clickable((By.ID, "notification-tab")))
    browser.execute_script("arguments[0].click();", duyuru_ve_haberler_butonu)
    sleep(3)
    #Güncel duyurular görünmeli
    guncel_duyurular = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='notification-tab-pane']/div")))
    assert len(guncel_duyurular) > 0, "Güncel duyuru haberleri bulunamadı."
    sleep(2)

#Case 2: Duyuru ve Haberlerim Kısmı Filtreleme İşlemlerinin Kontrolü
def test_duyuruFiltreleme(browser):
    #  Sitenin giriş sayfasına git
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("sevalcagdas4@gmail.com")
    password_input = browser.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("Dolunay13")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    # "Duyuru ve Haberlerim" butonuna tıkla
    duyuru_ve_haberler_butonu = WebDriverWait(browser, 10).until(  EC.element_to_be_clickable((By.ID, "notification-tab")))
    browser.execute_script("arguments[0].click();", duyuru_ve_haberler_butonu)
    #Güncel duyurular görünmeli
    guncel_duyurular = WebDriverWait(browser, 10).until( EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='notification-tab-pane']/div")))
    assert len(guncel_duyurular) > 0, "Güncel duyuru haberleri bulunamadı."
    # Daha fazla göster butonunu tıkla
    daha_fazla_goster_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='notification-tab-pane']/div/div[4]")))
    browser.execute_script("arguments[0].click();", daha_fazla_goster_button)
    # Yeni sayfanın yüklenmesini bekleyin
    duyurusayfası=WebDriverWait(browser, 20).until(EC.url_contains("https://tobeto.com/duyurular"))
    sleep(5)
    # Arama motoru kısmına, bulmak istediğin duyuru ve haberin adını yaz.
    # Arama kutusunu bul
    arama_kutusu = browser.find_element(By.ID, "search")
    # Arama kutusuna veriyi gönder
    arama_kutusu.send_keys("Mindset Anketi")
    # Enter tuşuna basmak için ActionChains kullanarak Enter tuşunu gönder
    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER).perform()
    sleep(3)
    #Filtreleme kısmında bulunan "Tür" seçeneği kısmından duyuru veya haber checbox'ını seç.
    # "Tür" menüsünü bul
    tur_dropdown = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[2]/button")
    # Tür menüyü aç
    tur_dropdown.click()
    # "Duyuru" veya "Haber" seçeneğini seç
    duyuru_option = browser.find_element(By.ID, "typeNews")
    duyuru_option.click()
    sleep(3)










