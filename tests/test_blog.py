import pytest

from pages.blog.blog import blog

@pytest.mark.smoke
def test_blog(page):
    obj_blog=blog(page)
    obj_blog.blogSubMenus()