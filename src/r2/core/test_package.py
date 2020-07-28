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

    def test_save_arg_endpoint(self):
        self.assertTrue(self._save_example_with_args())

    def test_load_arg_endpoint(self):
        self._save_example_with_args()
        self.assertIsNotNone(self.package.load("test/endpoint?first=asdfgh&second=qwerty"))

    def _save_example_with_args(self):
        return self.package.save("test/endpoint?first=asdfgh&second=qwerty", {"test22": "test_body"})

    def _save_example_with_args_diff(self):
        pass

    def test__make_args_dict_from_endpoint(self):
        args = self.package._make_args_dict_from_endpoint("test/endpoint?first=asdfgh&second=qwerty")

        self.assertIs(len(args), 2, "Should return 2 elements in the dictionary")
        self.assertTrue(isinstance(args, dict), "Return should be a dictionary instance")

    def test__undress_endpoint(self):
        path, filename, args = self.package._undress_endpoint("test/endpoint?first=asdfgh&second=qwerty")
        self.assertIsNotNone(path)
        self.assertEqual(filename, "endpoint")
        self.assertTrue(isinstance(args, dict))

    def tearDown(self) -> None:
        test_endpoint_location = os.path.join(*(Installation.DOWNLOAD_DIR, "default", "test", "endpoint"))
        if os.path.exists(test_endpoint_location):
            os.remove(test_endpoint_location)
        if os.path.isdir(os.path.join(*(Installation.DOWNLOAD_DIR, "default", "test"))):
            os.rmdir(os.path.join(*(Installation.DOWNLOAD_DIR, "default", "test")))
