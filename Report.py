import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    """
    generate the report BeautifulReport
    """
    test_dir = "./"
    dis = unittest.defaultTestLoader.discover(test_dir, pattern='test.py')

    runner = BeautifulReport(dis)
    runner.report(
        description="description",
        filename="BeautifulReport"
    )


