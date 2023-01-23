class Controller:
    def __init__(self):
        self.clicks = 1
        self.channel = self.clicks

    def click(self):
        self.clicks += 1
        if self.clicks > 5:
            self.clicks = 1
        self.channel = self.clicks


c = Controller()
print(c.channel)
c.click()
c.click()
c.click()
c.click()
c.click()
c.click()
print(c.channel)
c.click()
c.click()
print(c.channel)
c.click()
c.click()
print(c.channel)
