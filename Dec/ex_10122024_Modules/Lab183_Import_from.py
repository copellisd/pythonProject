from BrowserPackage.OpenBrowser import start_browser
from BrowserPackage.CloseBrowser import stop_browser

def test_case():
    start_browser()
    print("hello running TC")
    stop_browser()


test_case()
