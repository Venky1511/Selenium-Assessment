# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time, os

driver = webdriver.Chrome()

#########################################################################################################
#1
# Write a script to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Books
# Add first book to cart
# Click Shopping Cart
# Verify the product is present in the cart.
# Answer
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(3)
#
# driver.find_element(By.LINK_TEXT,"Books").click()
# time.sleep(3)
#
# driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
# time.sleep(3)
#
# driver.find_element(By.LINK_TEXT,"Shopping cart").click()
# time.sleep(3)
#
# product = driver.find_element(By.XPATH,"//table[@class='cart']//a").text
# print("Product in cart:", product)

#########################################################################################################
#2(issue)
# Write a Selenium script to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Electronics
# Use XPath contains() to locate the Cell Phones category
# Click it.
#Answer
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(3)
#
# driver.find_element(By.LINK_TEXT,"Electronics").click()
# time.sleep(3)
#
# driver.find_element(By.XPATH,"//a[contains(text(),'Cell phones')]").click()
# time.sleep(3)
#
# print("Navigated to Cell Phones")

#########################################################################################################
#3
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/dynamic_loading/1
# Click Start
# Wait until the Hello World text appears
# Print the text.
#Answer
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# time.sleep(3)
#
# driver.find_element(By.XPATH,"//button").click()
# time.sleep(5)
#
# text = driver.find_element(By.ID,"finish").text
# print("Text:", text)

#########################################################################################################
#4
# Write a script to:
# Open https://the-internet.herokuapp.com/dynamic_controls
# Click Remove
# Wait until Add button becomes clickable
# Click Add
#Answer
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# time.sleep(3)
#
# driver.find_element(By.XPATH,"//button[text()='Remove']").click()
# time.sleep(5)
#
# driver.find_element(By.XPATH,"//button[text()='Add']").click()
# time.sleep(3)
#
# print("Add button clicked")

#########################################################################################################
#5
# Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Select "Group 2, option 1" from the Select Value dropdown
# Verify the selected value.
#Answer
# driver.get("https://demoqa.com/select-menu")
# time.sleep(3)
#
# driver.find_element(By.ID,"withOptGroup").click()
# time.sleep(2)
#
# driver.find_element(By.XPATH,"//div[text()='Group 2, option 1']").click()
# time.sleep(2)
#
# value = driver.find_element(By.XPATH,"//div[contains(@class,'singleValue')]").text
# print("Selected value:", value)

#########################################################################################################
#6
# Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Scroll to Standard multi select
# Select Volvo, Saab, and Opel
# Print all selected options.

# driver.get("https://demoqa.com/select-menu")
# time.sleep(3)
#
# driver.execute_script("window.scrollBy(0,600)")
# time.sleep(2)
#
# multi = Select(driver.find_element(By.ID,"cars"))
#
# multi.select_by_visible_text("Volvo")
# multi.select_by_visible_text("Saab")
# multi.select_by_visible_text("Opel")
# time.sleep(2)
#
# print("Selected cars:")
# for option in multi.all_selected_options:
#     print(option.text)

#########################################################################################################
#7(issue)
# Write a Selenium script to:
# Open https://demoqa.com/menu/
# Hover over Main Item 2
# Hover over SUB SUB LIST
# Click Sub Sub Item 1
#
# driver.get("https://demoqa.com/menu/")
# time.sleep(3)
#
# actions = ActionChains(driver)
#
# main2 = driver.find_element(By.XPATH,"//a[text()='Main Item 2']")
# subsub = driver.find_element(By.XPATH,"//a[text()='SUB SUB LIST']")
# item1 = driver.find_element(By.XPATH,"//a[text()='Sub Sub Item 1']")
#
# actions.move_to_element(main2).perform()
# time.sleep(2)
#
# actions.move_to_element(subsub).perform()
# time.sleep(2)
#
# item1.click()
# time.sleep(2)
#
# print("Sub Sub Item 1 clicked")

#########################################################################################################
#8
# Write a Selenium script to:
# Open https://demoqa.com/droppable
# Drag Drag me element
# Drop it on Drop here
# Verify text changes to Dropped!
#
# driver.get("https://demoqa.com/droppable")
# time.sleep(3)
#
# drag = driver.find_element(By.ID,"draggable")
# drop = driver.find_element(By.ID,"droppable")
#
# ActionChains(driver).drag_and_drop(drag,drop).perform()
# time.sleep(2)
#
# print(driver.find_element(By.ID,"droppable").text)

#########################################################################################################
#9
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/javascript_alerts
# Click JS Confirm
# Accept the alert
# Verify result text shows You clicked: Ok
#
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(3)
#
# driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
# time.sleep(2)
#
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(2)
#
# result = driver.find_element(By.ID,"result").text
# print(result)

#########################################################################################################
#10(issue)
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/upload
# Upload a file from local system
# Click Upload
# Verify uploaded file name.
#
# driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(3)
#
# file_path = "C:/Users/YourUserName/Downloads/test.txt"   # change file path
#
# driver.find_element(By.ID,"file-upload").send_keys(file_path)
# time.sleep(2)
#
# driver.find_element(By.ID,"file-submit").click()
# time.sleep(3)
#
# print("Uploaded file:", driver.find_element(By.ID,"uploaded-files").text)

#########################################################################################################
#11(issue)
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/download
# Download any file
# Verify the file is downloaded in the Downloads folder using Python.
#
# driver.get("https://the-internet.herokuapp.com/download")
# time.sleep(3)
#
# driver.find_element(By.XPATH,"(//a)[1]").click()
# time.sleep(5)
#
# downloads = os.path.join(os.path.expanduser("~"),"Downloads")
#
# files = os.listdir(downloads)
#
# print("Files in Downloads folder:", files)

#########################################################################################################
#12
# Write a script to:
# Open https://demowebshop.tricentis.com
# Add any two products from Books
# Navigate to Shopping Cart
# Verify total number of products added is 2.
#
# driver.get("https://demowebshop.tricentis.com/books")
# time.sleep(3)
#
# buttons = driver.find_elements(By.XPATH,"//input[@value='Add to cart']")
#
# buttons[0].click()
# time.sleep(2)
#
# buttons[1].click()
# time.sleep(2)
#
# driver.find_element(By.LINK_TEXT,"Shopping cart").click()
# time.sleep(3)
#
# rows = driver.find_elements(By.XPATH,"//table[@class='cart']//tr")
#
# print("Total products added:", len(rows)-1)

#########################################################################################################
#13(issue)
# Write a Selenium script that:
# Open https://demowebshop.tricentis.com
# Navigate to Books
# Add all books priced below $20 to cart
#
# driver.get("https://demowebshop.tricentis.com/books")
# time.sleep(3)
#
# prices = driver.find_elements(By.XPATH,"//span[@class='price actual-price']")
# buttons = driver.find_elements(By.XPATH,"//input[@value='Add to cart']")
#
# for i in range(len(prices)):
#     price = float(prices[i].text.replace("$",""))
#     if price < 20:
#         buttons[i].click()
#         time.sleep(1)
#
# print("Books below $20 added")
#
# #########################################################################################################
#
# driver.quit()
#################################################################################################################
#14
# Write the steps to read the data from excel
#Answer
#1 Install required library (xlrd).
#2 Import the library in your Python script.
#3 Provide the Excel  Absolute file path where the test data is stored.
#4 Open the workbook using the library.
#5 Select the required sheet from the workbook.
#6 Read rows and columns from the sheet.
#7 Store the values in variables and use them as input in Selenium scripts (for example username, password, etc.).
#8 Use the data inside Selenium commands like send_keys() for form filling.
##########################################################################################################3
#15
# Write the syntax for the xpath to locate the elements using
# 	*	attributes : //tagname[@attribute='value']
# 	*	text : //tagname[text()='value']
# 	*	group indexing : (//tagname[@attribute='value'])[index]
# 	*	contains  : //tagname[contains(@attribute,'value')]
#
#
# #########################################################################################################
#
# 1. Which locator is generally the fastest in Selenium?
#ANS : id locator is generally the fastest in Selenium
# 2. Which wait is recommended for handling dynamic elements in Selenium?
#Ans: Explicit Wait is recommended for handling dynamic elements in Selenium
# 3. Which Selenium class is used to handle dropdown listboxes?
#Ans : Select class is used to handle dropdown listboxes

