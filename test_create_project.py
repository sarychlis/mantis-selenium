import unittest
from selenium.webdriver.common.by import By

import test_case


class CreateProjectTest(test_case.TestCase):

    def test_create_project(self):
        self.login()
        self.goToProjectListPage()

        self.driver.find_element(
            By.XPATH,
            '//*[@id="main-container"]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[1]/form/button'
        ).click()

        new_project_name = self.driver.find_element(By.ID, 'project-name')
        new_project_name.click()
        new_project_name.send_keys('rowi.tech')

        self.driver.find_element(By.ID, 'project-status').click()
        self.driver.find_element(By.XPATH, '//*[@id="project-status"]/option[3]').click()
        self.driver.find_element(By.ID, 'project-view-state').click()
        self.driver.find_element(By.XPATH, '//*[@id="project-view-state"]/option[1]').click()

        project_description = self.driver.find_element(By.ID, 'project-description')
        project_description.click()
        project_description.send_keys('my new test project')

        self.driver.find_element(By.XPATH, '//*[@id="manage-project-create-form"]/div/div[3]/input').click()
        self.driver.find_element(By.XPATH, '//a[contains(@href,"manage_proj_page.php")]').click()

        assert self.driver.find_element(By.LINK_TEXT, 'rowi.tech').is_enabled()


if __name__ == '__main__':
    unittest.main()
