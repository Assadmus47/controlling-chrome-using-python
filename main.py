from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def main ():
    driver = webdriver.Chrome()
     
    # Open Google's home page
    driver.get("https://www.google.com")

    search_box = driver.find_element("name", "q")
    search_box.send_keys("Marvel")
    search_box.send_keys(Keys.RETURN)
    #search_button = driver.find_element("name", "btnK")
    
    
    time.sleep(60)
    
    # Close the browser after the user input
    driver.quit()
if __name__ == "__main__":
    main()
    