# from celery.schedules import crontab
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# options = Options()
# options.add_argument('--no-sandbox')
# options.add_argument('--window-size=1920,1080')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# service = webdriver.ChromeService(executable_path='/usr/local/bin/chromedriver-linux64/chromedriver')

command: celery --app=web_scrappers worker -l INFO