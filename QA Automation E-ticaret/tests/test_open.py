from pages.login_page import LoginPage
import time
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest
@pytest.mark.smoke
@pytest.mark.regression
def test_open_saucedemo(driver):
    login = LoginPage(driver)
    
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_button()

    inventory = InventoryPage(driver)
    assert "inventory.html" in login.get_current_url()
    assert inventory.get_products_title() == "Products"

    inventory.add_backpack_button()
    inventory.go_to_cart()
    print(driver.current_url)

    
    print("sepete ürün eklendi.")

    assert inventory.get_cart_badge_count() == "1"

    cart = CartPage(driver)

    assert cart.get_cart_title() =="Your Cart"

    

    cart.go_to_checkout()
    print(driver.current_url)
    print(driver.page_source)

    checkout = CheckoutPage(driver)

    assert checkout.get_checkout_title() == "Checkout: Your Information"

    checkout.enter_first_name("Alper")
    assert checkout.get_first_name_value() == "Alper"

    
    checkout.enter_last_name("Türk")
    
    assert checkout.get_last_name_value() == "Türk"

    
    checkout.enter_postal_code("3400")
    assert checkout.get_postal_code_value() == "3400"
    
    checkout.click_continue()
    

    checkout.click_finish_button()

    assert checkout.get_checkout_title() =="Checkout: Complete!"
    print(driver.current_url)
    print("Bütün işlemler doğru ürün siparişi alınmıştır.")


    