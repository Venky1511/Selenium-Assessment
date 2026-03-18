import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

# #Q1
# driver.get('https://www.facebook.com/')
# wait_obj=WebDriverWait(driver, 20)
# driver.find_element('xpath','//input[@name="email"]').send_keys('srinjoykundu@gmail.com')
# driver.find_element('xpath','//input[@name="pass"]').send_keys('151123')
# driver.find_element('xpath','//span[text()="Log in"]').click()
# try:
#     wait_obj.until(EC.visibility_of_element_located(('xpath','//span[@id="_R_6lal8pl5bb6ismj5ilipam_"]')))
#     print("Verification Successful")
# except:
#     print("Verification Failed")

# #Q2
# wait=WebDriverWait(driver,10)
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys('puma')
# time.sleep(2)
# driver.find_element('xpath','(//li[@class="desktop-suggestion null"])[1]').click()
# time.sleep(4)
# product = wait.until(EC.presence_of_element_located(
#     ('xpath', '(//li[@class="product-base"])[1]')
# ))
# product.click()
# time.sleep(2)
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
# shoe_size = wait.until(EC.element_to_be_clickable(
#     ('xpath','//p[text()="8"]')
# ))
# time.sleep(5)
# add_to_bag = wait.until(EC.element_to_be_clickable(
#     ('xpath', '//div[text()="ADD TO BAG"]')
# ))
# time.sleep(2)
# shoe_size.click()
# add_to_bag.click()
# print("Product added to cart successfully!")



# #Q3
# driver.get('https://www.icici.bank.in/')
# time.sleep(3)
# driver.find_element('xpath','//a[@class="hero-cards--item"]').click()
# time.sleep(3)
# driver.find_element('xpath','(//a[contains(text(),"APPLY*")])[2]').click()
# time.sleep(2)
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
# time.sleep(2)
# driver.find_element('id','name').send_keys('Srinjoy Kundu')
# driver.find_element('id','pan').send_keys('ABCDE1345R')
# driver.find_element('id','pincode').send_keys('751024')
# driver.find_element('id','mobile_number').send_keys('7439900212')
# driver.find_element('xpath','//button[text()="Send OTP"]').click()
# time.sleep(3)
# driver.find_element('xpath','//input[@name="checkbox"]').click()
# time.sleep(2)
# driver.find_element('xpath','//button[text()="Apply Now"]').click()
# time.sleep(5)
# try:
#     msg=driver.find_element('xpath','//*[contains(text(),"Invalid")]')
#     print('Message prompted: ',msg)
# except:
#     print('No Error')



#Q4
# driver.get('https://www.netmeds.com/')
# ac=ActionChains(driver)
# medicine=driver.find_element('xpath','//a[text()=" Medicine "]')
# ac.move_to_element(medicine).perform()
# time.sleep(2)
# driver.find_element('xpath','(//a[contains(text(),"Order Online")])[1]').click()
# time.sleep(2)
# driver.find_element('xpath','//button[text()=" Upload Prescription "]').click()

#Q5
# wait = WebDriverWait(driver, 10)
# driver.get('https://www.netmeds.com/')
# time.sleep(2)
# driver.find_element('xpath','//div[@class="position-relative profile-name"]').click()
# time.sleep(2)
# driver.find_element('xpath','//input[@name="mobile-number"]').send_keys('7439908282')
# time.sleep(2)
# driver.find_element('xpath','//button[text()=" Get OTP "]').click()
# time.sleep(10)
# try:
#     wait.until(EC.visibility_of_element_located(('xpath','//div[text()=" SRINJOY .. "]')))
#     print("Login Successful")
# except:
#     print("Login Failed")
# Q6
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@ aria-label="Enter From station. Input is Mandatory."]').send_keys("BBS")
# time.sleep(1)
# driver.find_element('xpath','//li[@ id="p-highlighted-option"]').click()
#
# driver.find_element('xpath','//input[@ aria-label="Enter To station. Input is Mandatory."]').send_keys("HYB")
# time.sleep(1)
# driver.find_element('xpath','//li[@ id="p-highlighted-option"]').click()
#
# driver.find_element('xpath','//input[@ class="ng-tns-c69-9 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]').click()
# driver.find_element('xpath','(//td[@ class="ng-tns-c69-9 ng-star-inserted"])[20]').click()
# time.sleep(1)
#
# driver.find_element('xpath','//div[@ class="ng-tns-c76-10 ui-dropdown ui-widget ui-state-default ui-corner-all"]').click()
# time.sleep(1)
# driver.find_element('xpath','//li[@ aria-label="AC First Class (1A) "]').click()
#
# driver.find_element('xpath','//div[@ class="ng-tns-c76-11 ui-dropdown ui-widget ui-state-default ui-corner-all"]').click()
# time.sleep(1)
# driver.find_element('xpath','//li[@ aria-label="TATKAL"]').click()
#
# driver.find_element('xpath','//button[contains(text()," Search Trains ")]').click()


#Q7
# ac=ActionChains(driver)
# driver.get("https://www.purplle.com/")
# driver.maximize_window()
# time.sleep(3)
# brands = driver.find_element('xpath','(//a[@href="/brand"])[1]')
# ac.move_to_element(brands).perform()
# time.sleep(2)
# driver.find_element('xpath','//a[contains(text(),"Lakme")]').click()
# time.sleep(3)
# first_product = driver.find_element('xpath','(//a[contains(@href,"/product")])[1]')
# ac.scroll_to_element(first_product).perform()
# time.sleep(2)
# first_product.click()
# time.sleep(3)
# driver.find_element('xpath','//input[@name="pincode"]').send_keys("560001")
# time.sleep(2)
# driver.find_element('xpath','//button[contains(text(),"Check")]').click()
# time.sleep(2)
# print("Pincode availability checked")




#Q8
# from ddt.read_excel import excel_data
# data = excel_data()
# driver.get('https://lifeinsurance.adityabirlacapital.com/')
# driver.implicitly_wait(10)
# driver.find_element('xpath','(//a[text()="Her Insurance"])[2]').click()
# time.sleep(2)
# driver.find_element('id','firstName').send_keys(data['fname'])
# driver.find_element('id','lastName').send_keys(data['lname'])
# driver.find_element('id','email').send_keys(data['email'])
# driver.find_element('id','phonenumber').send_keys(data['ph'])

#Q9
# driver.get('https://www.apollopharmacy.in/')
# time.sleep(5)
# driver.find_element('xpath','//a[text()="Find Doctors"]').click()
# time.sleep(3)
# driver.find_element('xpath','(//a[@class="Jl_ "])[1]').click()
# time.sleep(2)
# driver.find_element('xpath','(//span[contains(text(),"Visit Doctor")])[1]').click()
# time.sleep(2)
# driver.find_element('xpath','(//div[@class="slots_date__Dy0W_ "])[5]').click()
# time.sleep(2)
# driver.find_element('xpath','(//div[@class="slots_slot__YYaL_ "])[2]').click()
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Continue"]').click()


# #Q10
# driver.get('https://porter.in/')
# time.sleep(3)
# driver.find_element('xpath','//p[text()="City:"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[text()="kolkata"]').click()
# time.sleep(2)
# driver.find_element('xpath','(//div[text()="Packers & Movers"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath','//input[@placeholder="Sending from"]').send_keys('Tollygaunj')
# time.sleep(2)
# driver.find_element('xpath','(//div[contains(text(),"Tollygunge")])[1]').click()
# time.sleep(2)
# driver.find_element('xpath','//input[@placeholder="Sending to"]').send_keys('Airport')
# time.sleep(2)
# driver.find_element('xpath','(//div[contains(text(),"Airport")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath','//input[@placeholder="Enter Contact Details"]').send_keys("7439905432")
# time.sleep(2)
# driver.find_element('xpath','//input[@value="19/03/2026"]').click()
# time.sleep(2)
# driver.find_element('xpath','//p[text()="19"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[text()="Check Price"]').click()
















