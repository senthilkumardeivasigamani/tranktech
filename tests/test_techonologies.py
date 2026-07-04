import pytest

from pages.techonlogies.ai import ai
from pages.techonlogies.eCommerceDevelopment import eCommerceDevelopment
from pages.techonlogies.mobileAppDev import mobileAppDev

@pytest.mark.smoke
def test_techonologies(page):

    #eCommerceDevelopment
    obj_eCommerceDevelopment=eCommerceDevelopment(page)
    obj_eCommerceDevelopment.eCommerceDevelopmentSubMenu()

    #mobileAppDev object
    obj_mobileAppDev=mobileAppDev(page)
    obj_mobileAppDev.mobileAppDevSubMenu()

    # AI Obkects
    obj_ai=ai(page)
    obj_ai.aiSubMenu()