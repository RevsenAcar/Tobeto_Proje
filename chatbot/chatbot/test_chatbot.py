import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

class Test_Chatbot:
    def setup_method(self, method):
        # Tarayıcıyı başlatır ve TOBETO giriş sayfasını açar
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)  # Maksimum bekleme süresi 

    def teardown_method(self, method):
        # Tarayıcıyı kapatır
        self.driver.quit()
    
    def open_chatbot(self):
        # Chatbot iframe'ine geçiş yap
        iframe = self.wait.until(EC.presence_of_element_located((By.ID, "exw-launcher-frame")))
        self.driver.switch_to.frame(iframe)
        
        # Chatbot simgesinin yüklenmesini bekle ve tıkla
        launcher_button = self.wait.until(EC.element_to_be_clickable((By.ID, "launcher")))
        launcher_button.click()
        sleep(5)  # Bekleme süresi, sayfanın yüklenmesi için
        self.driver.switch_to.default_content()
        
        iframe = self.wait.until(EC.presence_of_element_located((By.ID, "exw-conversation-frame")))
        self.driver.switch_to.frame(iframe)
        
    @pytest.mark.order(1)
    def test_chatbot_icon_control(self):
        """
        Case 1: Chatbot Simgesi ve Simgenin Açık veya Kapalı Kontrolü.
        """
        self.open_chatbot()
        
        # Chatbot simgesini kapat
        svg_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @class='exw-minimize-button header-button']")))
        svg_element.click()
        sleep(5)
        
    
 
    @pytest.mark.order(2)
    def test_chatbot_message_control(self):
        """
        Case 2: Chatbot Mesaj Bölümü Kontrolü
        """
        sleep(25)  # Sayfanın tamamen yüklenmesi için bekle
        self.open_chatbot()

        # Ad soyad giriş alanını bul ve bilgileri gir
        input_adsoyad = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.exw-inline-response-input-container input")))
        input_adsoyad.click()
        input_adsoyad.send_keys("Revşen Acar")
        input_adsoyad.send_keys(Keys.ENTER)
         # Chatbot'un sorusunu veya seçenekleri sunup sunmadığını kontrol et
        expected_question = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Sana hangi konuda yardımcı olmamı istersin?') or contains(text(), 'Tobeto Hakkında mı? İstanbul Kodluyor Hakkında mı?')]")))
        assert expected_question, "Chatbot beklenen soruyu veya seçenekleri sunmuyor."
         # 'Tobeto' seçeneğini seç
        tobeto_option = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Tobeto')]")))
        tobeto_option.click()
    
    @pytest.mark.order(3)
    def test_chatbot_end_conversation(self):
        """
        Case 3: Chatbot Mesaj Bölümünü Sonlandırma
        """
        self.open_chatbot()
        
        # Görüşmeyi sonlandır
        svg_element2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @class='exw-end-session-button header-button']")))
        svg_element2.click()
        sleep(5)
        
        # Evet butonunun yüklenmesini bekle ve tıkla
        yes_Btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='exw-conversation-frame-body']/div/div/div/div[1]/div/div[3]/div/button[1]")))
        yes_Btn.click()
        sleep(10)
        
        # Geri bildirim metin alanının yüklenmesini bekle ve mesaj gönder
        gorus_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='surveyTextArea']")))
        gorus_input.send_keys("Pair 1 teşekkür ediyor")
        sleep(10)
        
        # Gönder butonunun yüklenmesini bekle ve tıkla
        gndr_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='surveyForm']//*[@id='surveyBtn']")))
        self.driver.execute_script("arguments[0].click();", gndr_btn)
       
        # Geri bildirim onay mesajını kontrol et
        message = self.driver.find_element(By.XPATH, "//*[@id='exw-messages']/div[2]/div/div/div/h3")
        assert message.text == "Geri bildiriminiz için teşekkürler!", "Geri bildirim mesajı görünmedi"
        sleep(5)

    def test_chatbot_emoji_selection(self):
        """
        Case 4: Chatbot Emoji Seçimi
        """
        # İlk olarak test_chatbot_message_control fonksiyonunu çağır
        self.test_chatbot_message_control()
        sleep(15)
        # Emoji butonuna tıkla
        emoji_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "exw-add-emoji")))
        emoji_button.click()
        sleep(15)
        

    @pytest.mark.order(5)
    def test_chatbot_file_upload_button(self):
        """
        Case 5: Chatbot Dosya Yükleme Butonu Kontrolü
        """
        # İlk olarak test_chatbot_message_control fonksiyonunu çağır
        self.test_chatbot_message_control()
        sleep(15)
        # Dosya yükleme butonuna tıkla
        file_upload_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "exw-add-file")))
        file_upload_button.click()
        # Dosya seçiniz pop-up'ının göründüğünü kontrol et
        sleep(15)
        file_select_popup = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='exw-drag-drop-select-button']")))
        assert file_select_popup, "Dosya seçiniz pop-up'ı görünmedi."
         # Dosya seçiniz butonuna tıkla
        sleep(15)
        file_select_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='exw-drag-drop-select-button']")))
        file_select_button.click()     
          
            