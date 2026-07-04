import pytest

from pages.SocialMedia.socialmedia import socialmedia

@pytest.mark.smoke
def test_socialMedia(page):
    obj_socailMedia=socialmedia(page)
    obj_socailMedia.socialmediapageclick()