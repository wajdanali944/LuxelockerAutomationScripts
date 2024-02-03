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
Gift = driver.find_element(By.CLASS_NAME, "glproGiftOptionsPageEleCheckboxCheckmark").click()
time.sleep(3)
# Add details in the Gift Window
# From
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2FromField").click()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2FromField").clear()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2FromField").send_keys("Usama")
# To
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2ToField").click()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2ToField").clear()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2ToField").send_keys("Wajdan")
# Enter Note
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2InputField").click()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2InputField").clear()
driver.find_element(By.CLASS_NAME, "glproGiftMessageV2InputField").send_keys("Hi Wajdan, Please let me know when you got the gift")
# Enter Email Address
driver.find_element(By.CLASS_NAME, "glproVideoMsgEmailField").click()
driver.find_element(By.CLASS_NAME, "glproVideoMsgEmailField").clear()
driver.find_element(By.CLASS_NAME, "glproVideoMsgEmailField").send_keys("Wajdanali933@gmail.com")
# Click on SEND Later button
driver.find_element(By.CLASS_NAME, "glproGiftCardSendLaterButton").click()
# Click on Save Gifting Options
driver.find_element(By.CLASS_NAME, "giftMessageFinalButton").click()
time.sleep(2)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# Shop_accessories = driver.find_element(By.CLASS_NAME, "field__input")
# actions = ActionChains(driver)
# actions.move_to_element(Shop_accessories).perform()


        # # Add the product to the cart
        # add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='Add to Cart']")
        # add_to_cart_button.click()
        #
        # # Wait for the cart page to load
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cart-container']")))
        #
        # # Proceed to checkout
        # checkout_button = driver.find_element(By.XPATH, "//a[@class='checkout-button']")
        # checkout_button.click()
        #
        # # Add Gift Message to Order
        # add_gift_message_checkbox = driver.find_element(By.XPATH, "//input[@name='gift_message']")
        # add_gift_message_checkbox.click()
        #
        # # Fill the form with the required details
        # name_input = driver.find_element(By.ID, "checkout_shipping_address_first_name")
        # name_input.send_keys("Your Name")
        #
        # email_input = driver.find_element(By.ID, "checkout_shipping_address_email")
        # email_input.send_keys("your.email@example.com")
        #
        # address_input = driver.find_element(By.ID, "checkout_shipping_address_address1")
        # address_input.send_keys("123 Main Street")
        #
        # city_input = driver.find_element(By.ID, "checkout_shipping_address_city")
        # city_input.send_keys("City")
        #
        # zip_input = driver.find_element(By.ID, "checkout_shipping_address_zip")
        # zip_input.send_keys("12345")
        #
        # # Add a gift message
        # gift_message_input = driver.find_element(By.ID, "checkout_note")
        # gift_message_input.send_keys("This is a gift for someone special!")
        #
        # # Proceed to payment (you may need to add additional details based on the website's checkout process)
        # continue_to_payment_button = driver.find_element(By.XPATH, "//button[text()='Continue to payment']")
        # continue_to_payment_button.click()

        # Close the browser window
driver.quit()