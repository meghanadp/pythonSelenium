import pytest


@pytest.mark.usefixtures("init_driver") # using the fixtures already created in conftest.py
class BaseTest:
    pass  # this class don't have body
