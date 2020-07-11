from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:\\Users\\Kajal\\PycharmProjects\\SeleniumTest1\\drivers\\chromedriver.exe')
action = ActionChains(driver)
time.sleep(1)

main=driver.get('http://www.amazon.in')
time.sleep(1)

driver.maximize_window()

firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
action.move_to_element(firstLevelMenu).perform()
time.sleep(1)

secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_id('ap_email')
signinelement.send_keys("username")
time.sleep(3)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys("password")
time.sleep(1)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(1)

search1 = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search1.send_keys("wireless earchods")
time.sleep(1)

sr = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
sr.click()
time.sleep(4)

it1=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[4]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span')
driver.execute_script("arguments[0].scrollIntoView();", it1)
driver.execute_script("(arguments[0]).click();", it1)
time.sleep(5)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
w1=driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
w1.click()
time.sleep(3)

wish=driver.find_element_by_xpath('//*[@id="WLHUC_viewlist"]/span/span')
wish.click()
time.sleep(5)


remove=driver.find_element_by_xpath('//*[@id="itemAction_I18ALF5BUNTEUT"]/div/div/div/span/a')
remove.click()
time.sleep(3)


firstLevelMenu1 = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/div/span')
action.move_to_element(firstLevelMenu1).perform()
time.sleep(2)

signout=driver.find_element_by_xpath('//*[@id="nav-item-signout"]/span')
signout.click()
time.sleep(3)

