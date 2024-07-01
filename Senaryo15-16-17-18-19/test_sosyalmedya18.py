from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest
from pathlib import Path
from datetime import date
import openpyxl




@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.get("https://tobeto.com/giris")  # Giriş sayfasına gidin
    folderPath=str(date.today())
    Path(folderPath).mkdir(exist_ok=True)
    yield driver
    driver.quit()

def login(driver, email, password):
  
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")))
    usernameInput = driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")))
    passwordInput =driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    usernameInput.send_keys(email)
    passwordInput.send_keys(password)
        
    loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/div[4]/form/button[1]")
    
    loginBtn.click()

    # platform sayfasına gelebeklene kadar 
    WebDriverWait(driver,5).until(EC.url_to_be("https://tobeto.com/platform"))

def wait_for_element(driver, by, value, timeout=10):
     return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by,value)))

def media(driver):

    driver.get("https://tobeto.com/profilim")

    #Adım 2:profil düzenle sayfasına gel

    wait_for_element(driver, By.XPATH," /html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div/span").click()

#    medya hesaplarıma git
    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[1]/div/a[8]/span[2]").click()
        






#SOSYAL MEDYA HESABI EKLE
@pytest.mark.parametrize("platform,hesap",[("instagram","nisanrbas" ),("LinkedIn","1245." )])
def test_socialmedia_add(driver,platform,hesap):
    # Kullanıcı giriş bilgilerini doldurun ve medya hesaplarıma git
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
    media(driver)


#seç ve hesapları gir

    medya_input=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[2]/input")
    
    medya_input.click()
    sleep(2)
    medya_input.send_keys(platform)
    sleep(1)
    medya_input.send_keys(Keys.ENTER)
    sleep(2)

    medya_input2=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/form/div/div[2]/input")
    medya_input2.click()
    sleep(2)
    medya_input2.send_keys(hesap)
    sleep(3)

    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/form/button").click()


    sleep(1)

    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_socialmedia_add.png"
    driver.save_screenshot(screenshot_path)
    assert "Sosyal medya adresiniz başarıyla eklendi" in driver.page_source



#Sosyal medya alanların boş veya geçersiz bilgisinin boş bırakılmasını test et

@pytest.mark.parametrize("platform,hesap",[("instagram","" ),("aa","Nisa" )])
def test_socialmedia_emptychoice(driver,platform,hesap):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
    
    media(driver)

    #hesap türü seç

    medya_input=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[2]/input")
    
    medya_input.click()
    sleep(2)
    medya_input.send_keys(platform)
    sleep(1)
    medya_input.send_keys(Keys.ENTER)
    sleep(2)
    #hesap bilgisi gir
    medya_input2=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/form/div/div[2]/input")
    medya_input2.click()
    sleep(2)
    medya_input2.send_keys(hesap)

    sleep(2)
    

    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/form/button").click()
    # if platform=="instagram":
    #     message="Doldurulması zorunlu alan*" 

    sleep(1)
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_socialmedia_emptychoice.png"
    driver.save_screenshot(screenshot_path)
    assert "Doldurulması zorunlu alan*" in driver.page_source

#EN FAZLA ÜÇ HESAP EKLENİR TESTİ =MEVCUT İKİ HESAP VAR 1 HESAP DAHA EKLE
@pytest.mark.parametrize("platform,hesap",[("instagram","abc" )])
def  test_socialmedia_addlimit(driver,platform,hesap):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
    #medya hesaplarıma git
    media(driver)
    #hesap ekle
    medya_input=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[2]/input")
    medya_input.click()
    medya_input.send_keys(platform)
    medya_input.send_keys(Keys.ENTER)
    medya_input2=wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/form/div/div[2]/input")
    medya_input2.click()
    sleep(2)
    medya_input2.send_keys(hesap)
    sleep(3)

 
    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div/form/button").click()
    sleep(2)

    try:
      WebDriverWait(driver,10).until(EC.invisibility_of_element(( By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div[1]/form/button")))

      assert True,"alan başarılı şekikde kayboşdu"
       
    except noElement:  
        assert False


   
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_socialmedia_addlimit.png"
    driver.save_screenshot(screenshot_path)
    assert "En fazla 3 adet medya seçimi yapılabilir." in driver.page_source
    # assert not button

#HESAP GÜNCELLEME TESTİ

def test_socialmedia_update(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
    #medya hesaplarıma git
    media(driver)
    #düzenlemek için kalem işaretliye tıkla
    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div[1]/div/btn[2]").click()
    #sosyal medya güncelle penceresinden sosyal medya hesap türlerine tıkla
    wait_for_element(driver, By.XPATH," /html/body/div[3]/div/div/div[2]/div/form/div/div[1]/select").click()
    #yeni tür seç

    wait_for_element(driver, By.XPATH," /html/body/div[3]/div/div/div[2]/div/form/div/div[1]/select/option[4]").click()
    sleep(3)
    #güncelleye tıkla
    sleep(2)
    wait_for_element(driver, By.XPATH,"/html/body/div[3]/div/div/div[2]/button[1]").click()

    sleep(2)
   
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_socialmedia_update.png"
    driver.save_screenshot(screenshot_path)

    assert "Sosyal medya adresiniz başarıyla güncellendi." in driver.page_source
    
#HESAP SİLME TESTİ=3 HESABIDA SİL
def test_socialmedia_delete(driver):
    # Kullanıcı giriş bilgilerini doldurun
    login(driver,"nisanr.bas@gmail.com","Nisa123.")
    #medya hesaplarıma git
    media(driver)
    #silmek için kalem işaretliye tıkla
    wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div[1]/div/btn[1]").click()
    sleep(3)

    wait_for_element(driver, By.XPATH," /html/body/div[3]/div/div/div/div/div/div[2]/button[2]").click()
    sleep(2)
    
    folderPath = str(date.today())
    screenshot_path = f"{folderPath}/test_socialmedia_delete.png"
    driver.save_screenshot(screenshot_path)
    assert "Sosyal medya adresiniz başarıyla kaldırıldı." in driver.page_source
    sleep(2)


  
    # #sosyal medya güncelle penceresinden sosyal medya hesap türlerine tıkla
    # wait_for_element(driver, By.XPATH,"/html/body/div/div/main/section/div/div/div[2]/div[2]/div/btn[1]").click()
    # #yeni tür seç

    # wait_for_element(driver, By.XPATH," /html/body/div[3]/div/div/div[2]/div/form/div/div[1]/select/option[3]").click()
    # sleep(2)
    # #güncelleye tıkla
    # sleep(2)
    # wait_for_element(driver, By.XPATH,"/html/body/div[3]/div/div/div[2]/button[1]").click()

    # sleep(2)
    # assert "Sosyal medya adresiniz başarıyla güncellendi." in driver.page_source
    


   





    