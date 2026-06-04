from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverTypesFactory:

    def __init__(self, browser: str = "chrome", headless: bool = False):
        self.browser  = browser.lower()
        self.headless = headless
        self.driver   = None

    def get_chrome_options(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        return options

    def method1(self):
        print("Method 1 using selenium manager (built-in)")
        self.driver = webdriver.Chrome()
        return self.driver

    def method2(self):
        print(f"Method 2 Using webdriver-manager for {self.browser}")

        if self.browser == "chrome":
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
        elif self.browser == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service)
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")

        return self.driver

    def method3(self, driver_path: str):

        print(f"[Method 3] using manual driver path: {driver_path}")
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        return self.driver

    def method4(self):
        print(f"Method 4 Options & Service | browser={self.browser} | headless={self.headless}")

        if self.browser == "chrome":
            options  = self.get_chrome_options()
            service  = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
        elif self.browser == "firefox":
            options  = webdriver.FirefoxOptions()
            if self.headless:
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
            service  = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
            print("driver closed")


#Method 1 , download the driver manager version same as of local browser [automatically]
factory = DriverTypesFactory()
driver  = factory.method1()
driver.get("https://google.com")
factory.quit()

#Method 2 — using Chrome browser
factory = DriverTypesFactory(browser="chrome")
driver  = factory.method2()
driver.get("https://google.com")
factory.quit()

#Method 2 — using firefox browser
factory = DriverTypesFactory(browser="firefox")
driver  = factory.method2()
driver.get("https://google.com")
factory.quit()

#Method 3 , setting path manually
factory = DriverTypesFactory()
#dummy
driver  = factory.method3("C:/drivers/chromedriver.exe")
driver.get("https://google.com")
factory.quit()

#Method 4 Local with visible UI
factory = DriverTypesFactory(browser="chrome", headless=False)
driver  = factory.method4()
driver.get("https://google.com")
factory.quit()

# Method 4 Headless for Docker or Jenkins
factory = DriverTypesFactory(browser="chrome", headless=True)
driver  = factory.method4()
driver.get("https://google.com")
factory.quit()

# Add method overloading
class ComplexNumber:

    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self, other):
        real_part = self.real + other.real
        img_part = self.img + other.img
        return ComplexNumber(real_part,img_part)

    def __str__(self):
        return f"{self.real}i + {self.img}j"


c1 = ComplexNumber(4,5)
c2 = ComplexNumber(6,7)
result = c1 + c2