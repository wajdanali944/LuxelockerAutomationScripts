import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
# Navigate to the website
driver.get("https://www.firebellytea.com/")
# Wait for the frame to appear
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[10]/iframe")))
# Wait for the element and click on the close popup icon
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiSvgIcon-root"))).click()
# Switch back to original window
driver.switch_to.default_content()
time.sleep(2)
# Scroll and checking the height of the page
height = driver.execute_script("return document.body.scrollHeight")
print(height)
actions = ActionChains(driver)
actions.scroll_by_amount(delta_x=0, delta_y=5200).perform()
time.sleep(2)
# Click on the product and go the product details page
Cinnamon = driver.find_element(By.XPATH, "(//a[normalize-space()='Cinnamon & Spice Cookie'])[1]")
# add_to_cart = driver.find_element(By.XPATH, "(//div[@class='add_to_cart desktop-view'][normalize-space()='ADD TO CART'])[33]")
# plus_button = driver.find_element(By.XPATH, "//div[@aria-label='6 / 20']//i[@class='fa-solid fa-plus']")
actions.move_to_element(Cinnamon).click().perform()
# actions.move_to_element(taster).move_to_element(add_to_cart).move_to_element(plus_button).click().perform()
time.sleep(5)
# Click on 1 Time Purchase option
one_time_purchase = driver.find_element(By.XPATH, "//button[normalize-space()='1 Time Purchase']")
time.sleep(1)
Gift = driver.find_element(By.CLASS_NAME, "glproGiftOptionsPageEleCheckboxCheckmark").click()
time.sleep(6)
# Add details in the Gift Window
# From
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2FromField").click()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2FromField").clear()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2FromField").send_keys("Usama")
time.sleep(1)
# To
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2ToField").click()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2ToField").clear()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2ToField").send_keys("Wajdan")
# Enter Note
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2InputField").click()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2InputField").clear()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2InputField").send_keys("Hi Wajdan, Please let me know when you got the gift")
# Enter Email Address
time.sleep(1)
driver.find_element(By.CLASS_NAME, "glproVideoMsgEmailField").click()
driver.find_element(By.CLASS_NAME, "glproVideoMsgEmailField").clear()
driver.find_element(By.CLASS_NAME, "glproVideoMsgEmailField").send_keys("Wajdanali933@gmail.com")
time.sleep(1)
# Click on SEND Later button
driver.find_element(By.CLASS_NAME, "glproGiftCardSendLaterButton").click()
# Click on Save Gifting Options
time.sleep(1)
driver.find_element(By.CLASS_NAME, "giftMessageFinalButton").click()
time.sleep(1)
# Click on add to cart button
driver.find_element(By.XPATH, "//button[@name='add']").click()
time.sleep(4)
# Click on Checkout button
driver.find_element(By.XPATH, "(//span[normalize-space()='Checkout'])[1]").click()
time.sleep(3)
# Add Details on Checkout page
# Enter Email
driver.find_element(By.NAME, "email").click()
driver.find_element(By.NAME, "email").clear()
driver.find_element(By.NAME, "email").send_keys("Wajdanali933@gmail.com")
# Country will be default US
# Enter First Name
driver.find_element(By.ID, "TextField9").click()
driver.find_element(By.ID, "TextField9").clear()
driver.find_element(By.ID, "TextField9").send_keys("John")
# Enter Last Name
driver.find_element(By.ID, "TextField10").click()
driver.find_element(By.ID, "TextField10").clear()
driver.find_element(By.ID, "TextField10").send_keys("Smith")
# Enter Company Name
driver.find_element(By.ID, "TextField11").click()
driver.find_element(By.ID, "TextField11").clear()
driver.find_element(By.ID, "TextField11").send_keys("Phaedra Solutions")
# Enter Address
driver.find_element(By.ID, "shipping-address1").click()
driver.find_element(By.ID, "shipping-address1").clear()
driver.find_element(By.ID, "shipping-address1").send_keys("XYZ")
# Enter City
driver.find_element(By.ID, "TextField12").click()
driver.find_element(By.ID, "TextField12").clear()
driver.find_element(By.ID, "TextField12").send_keys("New York")
time.sleep(1)
# Select State
driver.find_element(By.ID, "Select2").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//option[@value='AK'])[1]").click()
time.sleep(2)
# Enter Zipcode
driver.find_element(By.ID, "TextField13").click()
driver.find_element(By.ID, "TextField13").clear()
driver.find_element(By.ID, "TextField13").send_keys("54000")
time.sleep(1)
# Enter Zipcode
driver.find_element(By.ID, "TextField14").click()
driver.find_element(By.ID, "TextField14").clear()
driver.find_element(By.ID, "TextField14").send_keys("03166587552")
time.sleep(1)
# Enter Credit Card Number
driver.find_element(By.ID, "number").click()
driver.find_element(By.ID, "number").clear()
driver.find_element(By.ID, "number").send_keys("424242424242")
time.sleep(1)
# Enter Expiration Date
driver.find_element(By.ID, "expiry").click()
driver.find_element(By.ID, "expiry").clear()
driver.find_element(By.ID, "expiry").send_keys("02/40")
time.sleep(1)
# Enter Security Code
driver.find_element(By.ID, "verification_value").click()
driver.find_element(By.ID, "verification_value").clear()
driver.find_element(By.ID, "verification_value").send_keys("358")
time.sleep(1)
# Enter Card Name
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("John Smith")
time.sleep(1)
# Clicks on remember me option for later checkout
driver.find_element(By.ID, "RememberMe-RememberMeCheckbox").click()



# Close the browser window
driver.quit()