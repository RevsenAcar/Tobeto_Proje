from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import pytest
from pathlib import Path 
from datetime import date
from constants import globalConstants


class Test_Scenario_14:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(globalConstants.URL)
        self.folderPath = str(date.today()) 
        Path(self.folderPath).mkdir(exist_ok=True)

        #giriş yap
        emailInput = self.driver.find_element(By.NAME, "email")
        passwordInput = self.driver.find_element(By.NAME, "password")
        emailInput.send_keys("davy.acxel@floodouts.com")
        passwordInput.send_keys("369369")
        loginButon = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
        loginButon.click()
        #profilim alanına tıkla
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[2]/a"))
        myProfile = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[2]/a")
        myProfile.click()
        #düzenle ikonuna tıkla
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div/div/div[1]/div/div[2]/div[1]/div/span"))
        profileEditIcon = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div/div/div[1]/div/div[2]/div[1]/div/span")
        profileEditIcon.click()

    def teardown_method(self):
        self.driver.quit() 

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))

    #Başarılı Deneyim Eklenmesi 
   
    def test_add_successful_experience(self):
        
        personalInformation = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[1]/span[2]")
        assert personalInformation.text == "Kişisel Bilgilerim"
        
        # "Deneyimlerim" başlığına tıkla
        myExperience = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")
        myExperience.click()
        # "Kurum Adı” alanını gir.
        self.waitForElementVisible((By.NAME,"corporationName"))
        corporationNameInput = self.driver.find_element(By.NAME,"corporationName")
        corporationNameInput.send_keys("TOBETO")
        # "Pozisyon" alanını gir.
        positionInput = self.driver.find_element(By.NAME,"position")
        positionInput.send_keys("YAZILIM TEST")
        # "Deneyim Türü" alanından seçim yap.
        experienceTypeListBox = self.driver.find_element(By.CLASS_NAME,"select__control")
        experienceTypeListBox.click()
        self.waitForElementVisible((By.ID,"react-select-5-option-2"))
        optionProfessionalWork = self.driver.find_element(By.ID,"react-select-5-option-2")
        optionProfessionalWork.click()
        # "Sektör" alanını gir.
        sectorInput = self.driver.find_element(By.NAME,"sector")
        sectorInput.send_keys("YAZILIM")
        # "Şehir" alanına tıkla ve listeden şehri seç.
        cityListBox = self.driver.find_element(By.NAME,"country")
        cityListBox.click()
        optionIstanbul = self.driver.find_element(By.XPATH,"//option[. = 'İstanbul']")
        optionIstanbul.click()
        # "İş Başlangıcı" alanına tarih gir ya da takvim üzerinden tarih seç
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[1]/div/input"))
        workStartInput = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[1]/div/input")
        workStartInput.click()
        workStartInput.send_keys("03.01.2020")
        # "İş Bitiş" alanına tarih gir ya da takvim üzerinden tarih seç.
        workFinishInput = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input")
        workFinishInput.send_keys("11.02.2024")
        # "İş Açıklaması" alanını doldur.
        self.driver.execute_script("window.scrollTo(0,500)")
        self.waitForElementVisible((By.XPATH,"//textarea[@name='description']"))
        jobDescription = self.driver.find_element(By.XPATH,"//textarea[@name='description']")
        jobDescription.click()
        jobDescription.send_keys("TOBETO")
        # Kaydet butonuna tıklayın.
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button"))
        saveButon = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")
        saveButon.click()
        # Sağ üstte deneyimin başarıyla eklendiğini belirten ‘Deneyim eklendi’ şeklinde bir bildiri görülmeli ve kaydedilen deneyim sayfanın alt 
        # kısmında listelenmelidir.
        self.waitForElementVisible((By.XPATH,"//div[@id='__next']/div/div/div/div[2]"))
        infoBox = self.driver.find_element(By.XPATH,"//div[@id='__next']/div/div/div/div[2]")
        assert infoBox.text == "• Deneyim eklendi."
        self.driver.save_screenshot(f"{self.folderPath}/test_add_successful_experience.png")
        experienceArea = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[1]/div[1]/span")
        assert experienceArea.is_displayed()


    #İş Açıklaması Karakter Kontrolü

    def test_job_description_character_check(self):

        # "Deneyimlerim" başlığına tıkla
        myExperience = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")
        myExperience.click()
        # "Kurum Adı” alanını gir.
        self.waitForElementVisible((By.NAME,"corporationName"))
        corporationNameInput = self.driver.find_element(By.NAME,"corporationName")
        corporationNameInput.send_keys("TOBETO")
        # "Pozisyon" alanını gir.
        positionInput = self.driver.find_element(By.NAME,"position")
        positionInput.send_keys("YAZILIM TEST")
        # "Deneyim Türü" alanından seçim yap.
        experienceTypeListBox = self.driver.find_element(By.CLASS_NAME,"select__control")
        experienceTypeListBox.click()
        self.waitForElementVisible((By.ID,"react-select-5-option-2"))
        optionProfessionalWork = self.driver.find_element(By.ID,"react-select-5-option-2")
        optionProfessionalWork.click()
        # "Sektör" alanını gir.
        sectorInput = self.driver.find_element(By.NAME,"sector")
        sectorInput.send_keys("YAZILIM")
         # "Şehir" alanına tıkla ve listeden şehri seç.
        cityListBox = self.driver.find_element(By.NAME,"country")
        cityListBox.click()
        optionIstanbul = self.driver.find_element(By.XPATH,"//option[. = 'İstanbul']")
        optionIstanbul.click()
        # "İş Başlangıcı" alanına tarih gir ya da takvim üzerinden tarih seç
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[1]/div/input"))
        workStartInput = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[1]/div/input")
        workStartInput.click()
        workStartInput.send_keys("03.01.2020")
        # "İş Bitiş" alanına tarih gir ya da takvim üzerinden tarih seç.
        workFinishInput = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input")
        workFinishInput.send_keys("11.02.2024")
        # "İş Açıklaması" alanını 300 karakterden fazla gir.
        self.driver.execute_script("window.scrollTo(0,500)")
        jobDescription = self.driver.find_element(By.XPATH,"//textarea[@name='description']")
        jobDescription.click()
        jobDescription.send_keys(globalConstants.loremIpsum)
        # Kaydet butonuna tıklayın.
        saveButon = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")
        saveButon.click()
        # "En fazla 300 karakter girebilirsiniz" uyarısı görünmelidir.
        self.driver.save_screenshot(f"{self.folderPath}/test_job_description_character_check.png")
        warningMessage = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/span")
        assert warningMessage.text == "En fazla 300 karakter girebilirsiniz"

    # Kurum Adı,Pozisyon,Sektör Alanlarının "En Az" Karakter Kontrolü 
    
    def test_minimum_character_checks(self):

        # "Deneyimlerim" başlığına tıkla
        myExperience = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")
        myExperience.click()
        # Kurum Adı alanını 5 karakterden az gir.
        self.waitForElementVisible((By.NAME,"corporationName"))
        corporationNameInput = self.driver.find_element(By.NAME,"corporationName")
        corporationNameInput.send_keys("TOBE")
        # Pozisyon alanını 5 karakterden az gir.
        positionInput = self.driver.find_element(By.NAME,"position")
        positionInput.send_keys("YAZI")
        # Sektör alanını 5 karakterden az gir.
        sectorInput = self.driver.find_element(By.NAME,"sector")
        sectorInput.send_keys("YAZI")
        # Kaydet butonuna tıklayın.
        self.driver.execute_script("window.scrollTo(0,400)")
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button"),10)
        saveButon = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")
        sleep(3)
        saveButon.click()
        # "En az 5 karakter girmelisiniz" uyarısı görünmelidir.
        self.driver.save_screenshot(f"{self.folderPath}/test_minimum_character_checks.png")
        warningMessage2 = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span")
        assert warningMessage2.text == "En az 5 karakter girmelisiniz"

        # POZİSYON ALANINDA UYARI GÖRÜNMÜYOR, HATA VAR...

    # Kurum Adı,Pozisyon,Sektör Alanlarının "En Fazla" Karakter Kontrolü 
    
    def test_maximum_character_checks(self):

        # "Deneyimlerim" başlığına tıkla
        myExperience = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")
        myExperience.click()
        # Kurum Adı alanını 50 karakterden fazla gir.
        self.waitForElementVisible((By.NAME,"corporationName"))
        corporationNameInput = self.driver.find_element(By.NAME,"corporationName")
        corporationNameInput.send_keys("TOBEjcsnscajsjcnajcsnasjcnajsnasjnckasjcnajkcnajkcnj")
        # Pozisyon alanını 50 karakterden fazla gir.
        positionInput = self.driver.find_element(By.NAME,"position")
        positionInput.send_keys("YAzısdncjancjksnkcsdkckjcnjksdcnjksdcnkjsdckhdsbchsdcbnsd")
        # Sektör alanını 50 karakterden fazla gir.
        sectorInput = self.driver.find_element(By.NAME,"sector")
        sectorInput.send_keys("dcnjxnsascxdscjdsncjksdcnkjdscnjksdncjkdnjkdscnjkdscnjskdcnds")
        # Kaydet butonuna tıklayın.
        self.driver.execute_script("window.scrollTo(0,500)")
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button"),20)
        saveButon = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")
        sleep(2)
        saveButon.click()
        # "En fazla 50 karakter girebilirsiniz" uyarısı görünmelidir.
        self.driver.save_screenshot(f"{self.folderPath}/test_maximum_character_checks.png")
        warningMessage3 = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span")
        assert warningMessage3.text == "En fazla 50 karakter girebilirsiniz"


    # Kurum Adı,Pozisyon,Sektör Boş Bırakılması Kontrolü
    
    def test_leave_empty_check(self):

        # "Deneyimlerim" başlığına tıkla
        myExperience = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")
        myExperience.click()
        # Kurum Adı alanını boş bırak.
        # Pozisyon alanını boş bırak.
        # Sektör alanını boş bırak.
        # Kaydet butonuna tıkla.
        self.driver.execute_script("window.scrollTo(0,500)")
        self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button"),20)
        sleep(3)
        saveButon = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")
        sleep(2)
        saveButon.click()
        # "Doldurulması zorunlu alan*" uyarısı görünmelidir.
        self.driver.save_screenshot(f"{self.folderPath}/test_leave_empty_check.png")
        warningMessage4 = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span")
        assert warningMessage4.text == "Doldurulması zorunlu alan*"



        

        
        




        



        


            






        
        

    





