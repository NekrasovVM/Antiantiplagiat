import time
from selenium.webdriver import Keys, ActionChains
from  selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class DialogManager:
    def __init__(self, browser):
        self.browser = browser

        self.message_counter = 1
        self.last_thinking = None
        self.last_answer = None

    def send_message(self, m):

        ui.WebDriverWait(self.browser, 15).until(ec.element_to_be_clickable((By.ID, 'chat-input')))

        # time.sleep(3)

        chat_input = self.browser.find_element(By.ID, 'chat-input')
        chat_input.send_keys(m.replace("\n", "\\n").replace("'", "\\'"))
        # self.browser.execute_script("arguments[0].value = '" + m.replace("\n", "\\n").replace("'", "\\'")
        #                             + "'", chat_input)

        time.sleep(0.5)

        ActionChains(self.browser).key_down(Keys.SPACE).perform()

        time.sleep(0.1)

        ActionChains(self.browser).key_down(Keys.ENTER).perform()

        time.sleep(0.1)

    def get_answer(self):

        time.sleep(0.2)

        # wait for thinking
        i = 0
        while True:
            i += 1
            time.sleep(3)
            cur_thinking_list = self.browser.find_elements(By.XPATH, '//div[@class=" svelte-1c06zsf"]')

            if len(cur_thinking_list) != 0:
                if cur_thinking_list[-1] != self.last_thinking:
                    self.last_thinking = cur_thinking_list[-1]
                    break

        element = cur_thinking_list[-1]
        old_element_text = element.text

        while True:
            time.sleep(4)
            element_text = element.text

            if len(element_text) == len(old_element_text):
                break
            else:
                old_element_text = element_text

        # wait for answer
        while True:
            time.sleep(6)
            cur_answer_list = self.browser.find_elements(
                By.XPATH, '//div[@class=" svelte-1c06zsf"]')

            if len(cur_answer_list) != 0:
                if cur_answer_list[-1] != self.last_answer:
                    self.last_answer = cur_answer_list[-1]
                    break

        element = self.last_answer
        old_element_text = element.text

        while True:
            time.sleep(6)
            element_text = element.text

            if len(element_text) == len(old_element_text):
                break
            else:
                old_element_text = element_text

        # result = "\n".join(element.text.split("\n")[:-1])
        result = element.text

        return result