from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

# Russell loves using Firefox and wants to check out the new todo app
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

#He calls up the todo app website
    def test_can_open_todo_site(self):
        self.browser.get('http://localhost:8000')
#The todo site returns
        self.assertIn('To-Do', self.browser.title)
        self.fail()
if __name__ == '__main__':
    unittest.main(warnings = 'ignore')

#He is presented with the opportunity to enter a todo

#He types 'Buy an iPhone' and hits the Enter key

#The page refreshes and he sees
# 1. Buy an iPhone
