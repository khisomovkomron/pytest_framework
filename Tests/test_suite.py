# import unittest
# # from Tests.api_tests.test_storage_service import TestCategories
# from Tests.api_tests.test_storage_service import TestSPrice
# from Tests.api_tests.test_api import TestApi
#
# # Get all tests from the test classes
# # tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCategories)
# tc2 = unittest.TestLoader().loadTestsFromModule(TestSPrice)
# # tc3 = unittest.TestLoader().loadTestsFromModule(TestApi)
#
# # Create a test suite combining all test classes
# smokeTest = unittest.TestSuite([tc2])
#
# unittest.TextTestRunner(verbosity=2).run(smokeTest)

import pytest
import os

report_path = os.path.abspath("..") + "/Reports"
report_arg = f"--alluredir={report_path}"


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call():
    api_pytest_args = [
        # 'api_tests/test_storage.py',
        "api_tests/test_users.py",
        "--env=user_serv_tmp",
        "-s",
        "-v",
        report_arg,
        "-m filter_users_by_role",
    ]

    # ui_pytest_args = [
    #     'ui_tests/test_login.py',
    #     '-s',
    #     '-v',
    #     report_arg
    #     # '-m marks'
    # ]
    #
    pytest.main(api_pytest_args)
    # pytest.main(ui_pytest_args)


if __name__ == "__main__":
    pytest_runtest_call()
