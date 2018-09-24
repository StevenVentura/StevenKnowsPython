import TestBase
def run_all_tests():
    print("okay")
    testcases = []
    for i in range(0, 10):
        testcases.append(TestBase.test_base(i))

    for testcase in testcases:
        testcase.run_test()
    


run_all_tests()


