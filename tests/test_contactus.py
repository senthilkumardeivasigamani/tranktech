import pytest

from pages.contactus.contactus import contactus

@pytest.mark.smoke
def test_contatcus(page):
    obj_contact=contactus(page)
    obj_contact.contactUsFill()