class oldbrowser:
    def start_browser(self):
        print("IE Browser is starting")

    def stop_browsser(self):
        print("IE browser is stopping")

class chrome(oldbrowser):

    def start_browser(self):
        super().start_browser()
        print("better chrome browser is starting")

    def stop_browsser(self):
        print("better chrome browser is stopping")


c=chrome()

c.start_browser()
c.stop_browsser()