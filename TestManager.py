import TestBase
class test_manager():
    def __init__(self):
        pass

    def run_all_tests_preliminary_test(self):
        print("okay")
        testcases = []
        for i in range(0, 10):
            testcases.append(TestBase.test_base(i))

        for testcase in testcases:
            testcase.run_test()
    def run_all_tests_passed_from_ui(self,uilist):
        print("typu")
        pass

x = test_manager()



