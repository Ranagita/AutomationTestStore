from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest


# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=option)
driver = webdriver.Chrome()
driver.get("https://automationteststore.com/")
driver.maximize_window()
driver.implicitly_wait(3)
action = ActionChains(driver)

# =======Login and Navigation
# # Registration
# @pytest.mark.registration
# def test_registration():
#     # Your personal details
#     driver.find_element(by.XPATH,"//a[.='Login or register']").click()
#     driver.find_element(by.XPATH,"//button[contains(.,'Continue')]").click()
#     driver.find_element(by.ID,"AccountFrm_firstname").send_keys("Dragon")
#     driver.find_element(by.ID,"AccountFrm_lastname").send_keys("Boy")
#     driver.find_element(by.ID,"AccountFrm_email").send_keys("dragon@boy.com")
#     driver.find_element(by.ID,"AccountFrm_telephone").send_keys("1777")
#     driver.find_element(by.ID,"AccountFrm_fax").send_keys("-")
#     # Your address
#     driver.find_element(by.ID,"AccountFrm_company").send_keys("Privateer")
#     driver.find_element(by.ID,"AccountFrm_address_1").send_keys("Lovely Lane 17")
#     driver.find_element(by.ID,"AccountFrm_address_2").send_keys("-")
#     driver.find_element(by.ID,"AccountFrm_city").send_keys("Serang")
#     country = driver.find_element(by.ID,"AccountFrm_country_id")
#     select_country = Select(country)
#     select_country.select_by_visible_text("Indonesia")
#     region = driver.find_element(by.ID,"AccountFrm_zone_id")
#     select_region = Select(region)
#     select_region.select_by_visible_text("Banten")
#     driver.find_element(by.ID,"AccountFrm_postcode").send_keys("42100")
#     # Login details
#     driver.find_element(by.ID,"AccountFrm_loginname").send_keys("Dragonboy")
#     driver.find_element(by.ID,"AccountFrm_password").send_keys("Rgita777")
#     driver.find_element(by.ID,"AccountFrm_confirm").send_keys("Rgita777")
#     # Newsletter
#     driver.find_element(by.XPATH,"//form[@id='AccountFrm']//label[1]/input[@name='newsletter']").click()
#     # Policy
#     driver.find_element(by.ID,"AccountFrm_agree").click()
#     # Continue
#     driver.find_element(by.CSS_SELECTOR,".lock-on-click").click()
#     # Continue
#     driver.find_element(by.XPATH,"//a[contains(.,'Continue')]").click()

# Login with valid credentials
def test_valid_login():
    driver.get("https://automationteststore.com/index.php?rt=account/login")
    driver.find_element(by.ID,"loginFrm_loginname").send_keys("Dragonboy")
    driver.find_element(by.ID,"loginFrm_password").send_keys("Rgita777")
    driver.find_element(by.XPATH,"//button[contains(.,'Login')]").click()
    Title = driver.title
    assert Title=="My Account"

# # =======Functionality
# Add items to cart
def test_add_to_cart():
    apparel = driver.find_element(by.XPATH,"//ul[@class='nav-pills categorymenu']//a[contains(.,'Apparel & accessories')]")
    action.move_to_element(apparel).perform()
    driver.find_element(by.XPATH,"//a[contains(.,'Shoes')]").click()
    shoes = driver.find_element(by.CSS_SELECTOR,".maintext").text
    assert shoes=="SHOES"

    driver.find_element(by.XPATH,"//div[@class='thumbnails grid row list-inline']//a[.='New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals']").click()
    item = driver.find_element(by.XPATH,"//span[@class='bgnone']").text
    assert item=="New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals"

    driver.find_element(by.XPATH,"//input[@value='749']").click() # size 5UK
    qty = driver.find_element(by.ID,"product_quantity")
    action.double_click(qty).perform()
    driver.find_element(by.ID,"product_quantity").send_keys("2")
    driver.find_element(by.CLASS_NAME,"cart").click()

    cart = driver.find_element(by.CSS_SELECTOR,".maintext").text
    price = driver.find_element(by.XPATH,"//div[@class='container-fluid cart-info product-list']//td[.='$26.00']").text
    total_price = driver.find_element(by.XPATH,"//td[6]").text
    assert cart=="SHOPPING CART"
    assert price=="$26.00"
    assert total_price=="$52.00"
    driver.find_element(by.XPATH,"//a[contains(.,'Continue Shopping')]").click()

# Remove items from cart test
def test_remove_from_cart():
    driver.find_element(by.XPATH,"//ul[@class='nav topcart pull-left']/li[@class='dropdown hover']/a[1]").click()
    driver.find_element(by.XPATH,"//i[@class='fa fa-trash-o fa-fw']").click()
    text = driver.find_element(by.CSS_SELECTOR,".contentpanel").text
    assert text=="Your shopping cart is empty!\nContinue"
    driver.find_element(by.XPATH,"//a[contains(.,'Continue')]").click()

# View items detail test
def test_view_details():
    apparel = driver.find_element(by.XPATH,"//ul[@class='nav-pills categorymenu']//a[contains(.,'Apparel & accessories')]")
    action.move_to_element(apparel).perform()
    driver.find_element(by.XPATH,"//a[contains(.,'T-shirts')]").click()
    # jersey 1
    driver.find_element(by.XPATH,"//a[.='Jersey Cotton Striped Polo Shirt']").click()
    shirt1 = driver.find_element(by.XPATH,"//span[@class='bgnone']").text
    price1 = driver.find_element(by.XPATH,"//div[@class='productfilneprice']").text
    desc1 = driver.find_element(by.XPATH,"//div[@id='description']/p[1]").text
    assert shirt1=="Jersey Cotton Striped Polo Shirt"
    assert price1=="$6.75"
    assert "Classically designed Charles Wilson polo shirts now available." in desc1
    # jersey 2
    driver.find_element(by.XPATH,"//ul[@class='breadcrumb']//a[contains(.,'T-shirts')]").click()
    driver.find_element(by.XPATH,"//a[.='Designer Men Casual Formal Double Cuffs Grandad Band Collar Shirt Elegant Tie']").click()
    shirt2 = driver.find_element(by.XPATH,"//span[@class='bgnone']").text
    price2 = driver.find_element(by.XPATH,"//div[@class='productfilneprice']").text
    desc2 = driver.find_element(by.XPATH,"//div[@id='description']").text
    assert shirt2=="Designer Men Casual Formal Double Cuffs Grandad Band Collar Shirt Elegant Tie"
    assert price2=="$32.00"
    assert "Grandad collar. Slim Fit. Highest quality - made in Turkey. Great as casual or formal shirt." in desc2

# # =======Checkout Process
# Checkout process
def test_chxout():
    driver.find_element(by.XPATH,"//a[contains(.,'Add to Cart')]").click()
    driver.find_element(by.XPATH,"//div[@class='pull-right mb20']/a[contains(.,'Checkout')]").click()
    text = driver.find_element(by.XPATH,"//span[@class='maintext']").text
    assert text=="CHECKOUT CONFIRMATION"
    element_price = driver.find_element(by.XPATH,"//div[@class='sidewidt']//span[.='$32.00']").text
    element_tax = driver.find_element(by.XPATH,"//div[@class='sidewidt']//span[.='$2.00']").text
    element_total = driver.find_element(by.XPATH,"//div[@class='sidewidt']//span[.='$34.00']").text
    price = float(element_price.replace("$",""))
    tax = float(element_tax.replace("$",""))
    total = float(element_total.replace("$",""))
    calculated = price+tax
    assert calculated==total
    # Confirm order
    driver.find_element(by.XPATH,"//button[@id='checkout_btn']").click()
    driver.find_element(by.XPATH,"//a[contains(.,'Continue')]").click()

# Logout
def test_logout():
    my_account = driver.find_element(by.XPATH,"//div[@class='menu_text']")
    action.move_to_element(my_account).perform()
    driver.find_element(by.XPATH,"//a[contains(.,'Not Dragon? Logoff')]").click()
    text = driver.find_element(by.CSS_SELECTOR,"p:nth-of-type(2)").text
    assert text=="You have been logged off your account. It is now safe to leave the computer."
    driver.find_element(by.XPATH,"//a[contains(.,'Continue')]").click()


# Login with invalid credentials
credentials = [
    ('salahudin','Rgita777'),
    ('Dragonboy','Rgita7'),
    ('salahudin','Rgita7')
]
@pytest.mark.neg
@pytest.mark.parametrize('username,pswd',credentials)
def test_invalid_login(username,pswd):
    driver.get("https://automationteststore.com/index.php?rt=account/login")
    driver.find_element(by.ID,"loginFrm_loginname").send_keys(username)
    driver.find_element(by.ID,"loginFrm_password").send_keys(pswd)
    driver.find_element(by.XPATH,"//button[contains(.,'Login')]").click()
    notif = driver.find_element(by.CSS_SELECTOR,".alert").text
    assert notif=="×\nError: Incorrect login or password provided."