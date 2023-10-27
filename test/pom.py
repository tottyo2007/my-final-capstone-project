import time

from selenium import webdriver

from src.pages.LandingPage import LandingPage
from src.pages.RegPage import RegPage
from src.pages.LoginPage import LoginPage
from src.pages.ProductPage import ProductPage
from src.pages.CartPage import CartPage
from src.pages.OrderPage import OrderPage


driver = webdriver.Firefox()
driver.get('http://shop.icraftsoft.net:8095/')
driver.maximize_window()

# Landing Page
lp = LandingPage(driver)  # object create
lp.click_login()
time.sleep(4)

# Register username and password
rg = RegPage(driver)
rg.getUsername()
time.sleep(4)
rg.getEmail()
time.sleep(4)
rg.getButton()
time.sleep(4)


        #-----login page-----
driver.get('http://shop.icraftsoft.net:8095/')
Login = LoginPage(driver)
Login.login_textbox()
time.sleep(4)
Login.click_login()
time.sleep(4)
Login.click_logout()
time.sleep(4)
Login.click_home()
Login.login_textbox2()
Login.login_again()

          #------product page-----
Prop = ProductPage(driver)
Prop.search_box()
time.sleep(4)
Prop.Quick_view_product()
time.sleep(4)
Prop.select_Product1()
time.sleep(4)
Prop.Add_to_Cart()
time.sleep(4)
Prop.Add_cart_again()
time.sleep(4)


# cart page
CartP = CartPage(driver)
time.sleep(4)
CartP.click_on_cart()
time.sleep(4)




       #order page
OP = OrderPage(driver)
OP.remove_items()
OP.Contin_shop()
time.sleep(4)
OP.click_cart_again()
time.sleep(4)
OP.click_Buy_now()
time.sleep(7)
OP.click_on_home()











#THANK YOU
OP.loG_THANKS()
OP.login_tha()

