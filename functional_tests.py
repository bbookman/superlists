from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time

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


    def test_can_start_a_list_and_retrieve_it_later(self):
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.sendkeys('Buy an iPhone')
        inputbox.sendkeys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Buy an iPhone'
            for row in rows)
        )


if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
