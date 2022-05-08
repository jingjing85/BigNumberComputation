import unittest
from BeautifulReport import BeautifulReport
# import HTMLTestRunner
import time
if __name__ == '__main__':
    """
    generate the report 
    """
    now_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    test_dir = "./"
    dis = unittest.defaultTestLoader.discover(test_dir, pattern='test.py')

    runner = BeautifulReport(dis)
    runner.report(
        description="description",
        filename="BeautifulReport"
        # filename="HtmlReport"
    )


