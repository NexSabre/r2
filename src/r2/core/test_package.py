from unittest import TestCase
from unittest.mock import MagicMock

from r2.core.package import Package


class TestPackage(TestCase):
    def setUp(self) -> None:
        self.package = Package()

    def test_save(self):
        # self.package.save = MagicMock(return_value=False)
        self.assertTrue(self.package.save("test/endpoint", {"test": "test_body"}))

    def test_load(self):
        self.package._Package__read = MagicMock(return_value='{"test": "test_body"}')
        self.assertIsNotNone(self.package.load("test/endpoint"))
