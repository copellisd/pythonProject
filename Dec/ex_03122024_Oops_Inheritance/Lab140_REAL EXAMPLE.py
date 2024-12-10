class basetest:
    def open_browser(self):
        print("starting the browser")

    def close_browser(self):
        print("closing the browser")

class testcase1(basetest):
    def test_positive(self):
        self.open_browser()
        print("testcase 1 executed")
        self.close_browser()

    class testcase2(basetest):
        def test_2(self):
            self.open_browser()
            print("testc ase2 executed")
            self.close_browser()

    class testcase3(basetest):
        def test_3(self):
            self.open_browser()
            print("testcase3 executed")
            self.close_browser()
