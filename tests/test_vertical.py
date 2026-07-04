from types import SimpleNamespace
import pytest

from pages.vertical.customApp import customApp
from pages.vertical.fintech import fintech
from pages.vertical.healthcare import healthcare
from pages.vertical.retail import retail
from pages.vertical.trading import trading


@pytest.mark.smoke
def test_vertical(page):

    #Trading object
    obj_trade=trading(page)
    #obj_trade.mouseHover()
    obj_trade.tradingSubMenu()
    
    #Reatil and Ecommerce Object
    # obj_retail=retail(page)
    # obj_retail.retailSubMenu()

    #Healthcare Object
    obj_health=healthcare(page)
    obj_health.healthcareSubMenu()

    #Fintech Object
    obj_fintech=fintech(page)
    obj_fintech.fintechSubMenu()

    #Custom App
    obj_customApp=customApp(page)
    obj_customApp.customAppSubMenu()



@pytest.mark.smoke
def test_reatil(page):
    obj_retail=retail(page)
    obj_retail.retailSubMenu()


# def vertical_objects(page):
#     return SimpleNamespace(
#         obj_trade=trading(page),
#         obj_retail=retail(page),
#         obj_health=healthcare(page),
#         obj_fintech=fintech(page),
#         obj_customApp=customApp(page))

# @pytest.mark.smoke
# def test_trading(vertical_objects):
#     vertical_objects.trade.tradingSubMenu()

# @pytest.mark.smoke
# def test_retail(vertical_objects):
#     vertical_objects.retail.retailSubMenu()

# @pytest.mark.smoke
# def test_healthcare(vertical_objects):
#     vertical_objects.health.healthcareSubMenu()

# @pytest.mark.smoke
# def test_fintech(vertical_objects):
#     vertical_objects.fintech.fintechSubMenu()

# @pytest.mark.smoke
# def test_custom_app(vertical_objects):
#     vertical_objects.custom_app.customAppSubMenu()