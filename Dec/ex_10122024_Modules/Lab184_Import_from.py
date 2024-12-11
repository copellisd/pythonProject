from BrowserPackage.OpenBrowser import start_browser
from BrowserPackage.CloseBrowser import stop_browser
class testcase:
    def test_case(self):
       start_browser()
       print("hello running TC")
       stop_browser()


test=testcase()
test.test_case()
