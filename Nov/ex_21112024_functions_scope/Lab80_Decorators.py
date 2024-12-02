def add_before_ui_after_ui(func):

    def wrapper():
        print("before  test ui")
        print("start  browser")
        func()
        print("after test ui")
        print("quit browser")

    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print("--->i am in ui")