#Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#data
amount = '2' # amount in the cart
size_dress = "M" # S / M / L
colour_dress = "Orange" # Blue / Orange / Black / Yellow


#setUp
PATH = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
driver.implicitly_wait(20)

#search "dress"
search_dress = driver.find_element(By.NAME, "search_query")
search_dress.click()
search_dress.send_keys("dress")
search_dress.send_keys(Keys.ENTER)

#list sorting #in stock
sort = \
driver.find_element(By.ID, 'selectProductSort')
select_sort = Select(sort)
select_sort.select_by_visible_text("In stock")
time.sleep(5)

#picks first product from the list
driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()

#quantity
quantity = driver.find_element(By. ID, "quantity_wanted")
quantity.click()
quantity.send_keys(Keys.BACKSPACE)
quantity.send_keys(amount)

#size of the dress
size = Select(driver.find_element(By.ID, "group_1"))
size.select_by_visible_text(size_dress)

#colour of the dress
driver.find_element(By. XPATH, "//a[@name='" + colour_dress + "']").click()

#add to cart
driver.find_element(By. ID, "add_to_cart").click()
driver.find_element(By. XPATH, "//a[@class='btn btn-default button button-medium']").click()
time.sleep(5)

#verify amount in the cart
basket = (driver.find_element(By. XPATH, "//input[@class='cart_quantity_input form-control grey']").get_attribute("value"))
if basket == amount:
    pass
    print('OK :)')
else:
    print('Somethings wrong! :c ')
    exit()

#empty your cart
driver.find_element(By.ID, "5_25_0_0").click()

time.sleep(2)
driver.quit()
