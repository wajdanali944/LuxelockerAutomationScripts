# def test_verifying_rows_per_page_with_total_rows(self):
#     home_page = HomePage(self.driver)
#     home_page.enter_email_address("admin@luxelocker.com")
#     home_page.enter_password("123456789aA!")
#     home_page.click_on_login_button()
#     self.driver.implicitly_wait(10)
#     self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
#     self.driver.implicitly_wait(15)
#     self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div")
#     dropdown_count = self.driver.find_elements(By.XPATH,
#                                                    "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div")
#     totalfacilities = len(self.driver.find_elements(By.XPATH,
#                                                         "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[1]/div/table/tbody/tr"))
#     totalpaginationcount = self.driver.find_element(By.XPATH,
#                                                         "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[2]/div[1]/div[2]/span")
#     text = totalpaginationcount.text
#     splitval = text.split()
#     if str(totalfacilities) >= splitval[2]:
#         print('Rows are 20')
#     else:
#         self.driver.find_element(By.XPATH,
#                                   "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div").click()
#         totalfacilities = self.driver.find_elements(By.XPATH, "//li[normalize-space()='50']")
#         totalfacilities[0].click()
#
#         rows_count = len(self.driver.find_elements(By.XPATH, "//html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr"))
#
#         dropdown_count = self.driver.find_elements(By.XPATH,
#                                                    "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div")
#         # totalfacilities = len(self.driver.find_elements(By.XPATH,
#         #                                                 "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[1]/div/table/tbody/tr"))
#         if rows_count >= int(splitval[2]):
#             print('Rows are under 50')
#         else:
#             self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div").click()
#             dropdown_count = self.driver.find_elements(By.XPATH,
#                                                        "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div")
#             totalfacilities = len(self.driver.find_elements(By.XPATH,
#                                                             "//li[normalize-space()='100']"))
#
#
#             totalpaginationcount = self.driver.find_element(By.XPATH,
#                                                             "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[2]/div[1]/div[2]/span")
#             if str(totalfacilities) >= splitval[2]:
#                 print('Rows are under 100')
#             else:
#                 print("Rows are more than 100")