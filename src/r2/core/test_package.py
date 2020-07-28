import os
from unittest import TestCase

from r2.core.package import Package
from r2.install import Installation


class TestPackage(TestCase):
    def setUp(self) -> None:
        self.package = Package()

    def test_save(self):
        self.assertTrue(self._save_example())

    def test_load(self):
        self._save_example()
        self.assertIsNotNone(self.package.load("test/endpoint"))

    def _save_example(self):
        return self.package.save("test/endpoint", {"test": "test_body"})

    def tearDown(self) -> None:
        test_endpoint_location = os.path.join(*(Installation.DOWNLOAD_DIR, "default", "test", "endpoint"))
        if os.path.exists(test_endpoint_location):
            os.remove(test_endpoint_location)
            os.rmdir(os.path.join(*(Installation.DOWNLOAD_DIR, "default", "test")))
