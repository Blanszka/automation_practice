#BIBLIOTEKI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#DANE
ilosc = '2' # ilość jaką dodajemy do koszyka
rozmiar = "M" # S / M / L
kolor = "Orange" # Blue / Orange / Black / Yellow


#setUp
PATH = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
driver.implicitly_wait(20)

#wyszukanie sukienki
wyszukaj = driver.find_element(By.NAME, "search_query")
wyszukaj.click()
wyszukaj.send_keys("dress")
wyszukaj.send_keys(Keys.ENTER)

#sortowanie listy
sortowanie = \
driver.find_element(By.ID, 'selectProductSort')
select_sort = Select(sortowanie)
select_sort.select_by_visible_text("In stock")
time.sleep(5)

#wybiera pirwszy produkt ze strony
driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()

#ilosc produktu
quantity = driver.find_element(By. ID, "quantity_wanted")
quantity.click()
quantity.send_keys(Keys.BACKSPACE)
quantity.send_keys(ilosc)

#rozmiar produktu
size = Select(driver.find_element(By.ID, "group_1"))
size.select_by_visible_text(rozmiar)

#kolor produktu
driver.find_element(By. XPATH, "//a[@name='" + kolor + "']").click()

#dodaj do koszyka
driver.find_element(By. ID, "add_to_cart").click()
driver.find_element(By. XPATH, "//a[@class='btn btn-default button button-medium']").click()
time.sleep(5)

#zweryfikuj czy w koszyku zgadza się ilość produktów
koszyk = (driver.find_element(By. XPATH, "//input[@class='cart_quantity_input form-control grey']").get_attribute("value"))
if koszyk == ilosc:
    pass
    print('OK :)')
else:
    print('Błąd! :c ')
    exit()

#wyczyść koszyk
driver.find_element(By.ID, "5_25_0_0").click()

time.sleep(5)
driver.quit()
