Ikea outlet web scraper is a docker-based web application whose purpose is to independently (running in the background) search for promotions/deals in the ikea outlet section and notify the user via e-mail.

The application is composed of the following elements (containers):

- Django - The main part of the application responsible for interaction with the user. Using the browser, the user defines queries for periodic searches and can view scraping results. Django also acts as a message provider for the tasks that Celery performs

- Redis - Message broker. It stores the tasks that are sent from message provider. 

- Celery - Celery worker picks up the tasks and proccess them. Celery's tasks include performing periodic searches on the ikea website (web scraping) and sending emails with notifications about found products defined by the user in the django application.

- Selenium - Container built using selenium/standalone-chrome image. It provides a ready-to-use evironment with Selenium, ChromeDriver and the Chrome browser installed. It’s used to web scraping proccess.

To run application:
- clone https://github.com/MarcinLebiedzinski/Web_Scrappers
- use the command “docker compose up” in the root directory of the repository
- open http://localhost:8001/web_scrappers/main/ in Your browser