import test_case
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class DeleteProjectTest(test_case.TestCase):

    def test_delete_project(self):
        self.login()
        self.goToProjectListPage()

        self.driver.find_element(By.LINK_TEXT, 'rowi.tech').click()

        delete_project = self.driver.find_element(By.XPATH, '//*[@id="project-delete-form"]/fieldset/input[3]')
        delete_project.click()

        delete_project_btn = self.driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[3]/div/div/div[2]/form/input[4]')
        delete_project_btn.click()

        try:
            self.driver.find_element(By.LINK_TEXT, 'rowi.tech')
            assert False
        except NoSuchElementException:
            assert True


