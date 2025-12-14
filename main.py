from ChunkMaker import ChunkMaker
from DialogManager import DialogManager

import time
import os

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import ui
from selenium.common import WebDriverException

# def custom_wait_clickable_and_click(selector, action='click', action_param=None, attempts=5):
#     count = 0
#     while count < attempts:
#         try:
#             time.sleep(0.1)
#             # This will throw an exception if it times out, which is what we want.
#             # We only want to start trying to click it once we've confirmed that
#             # selenium thinks it's visible and clickable.
#             elem = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.XPATH, selector)))#             if action == 'click':
#                 elem.click()
#             else:
#                 elem.send_keys(action_param)
#             return elem
#
#         except WebDriverException as e:
#             if 'is not clickable at point' in str(e):
#                 print('Retrying clicking on button.')
#                 count = count + 1
#             else:
#                 raise e

print("Start")

with open("output.txt", 'w', encoding="utf-8") as f:

    directory = r".\Inputs"

    for filename in [filename for filename in os.listdir(directory) if filename.endswith('.txt')]:

        print(filename)

        browser = webdriver.Firefox()
        browser.get("https://chat.qwen.ai/")

        ui.WebDriverWait(browser, 15).until(ec.element_to_be_clickable((by.By.XPATH, '//*[.="Log in"]')))
        browser.find_element(by='xpath', value='//*[.="Log in"]').click()

        login = "gromnekot@gmail.com"
        password = "X6$AwCo%.omu3Z^"

        ui.WebDriverWait(browser, 15).until(ec.element_to_be_clickable((by.By.NAME, 'email')))
        browser.find_element(By.NAME, 'email').send_keys(login)
        browser.find_element(By.XPATH, '//*/input[contains(@placeholder,"Password")]').send_keys(password)
        browser.find_element(By.XPATH,
                             '//*/button[@class="qwen-chat-btn qwenchat-auth-pc-submit-button brandprimary round large"]').click()

        message = ("Переформулируй текст другими словами таким образом, чтобы увеличить его уникальность, но при этом "
                   "обязательно сохранить весь исходный смысл. Объём текста не должен значительно уменьшиться. Избегай "
                   "перефразированных заимствований по коллекции Интернет в русском сегменте. "
                   "Не нужно описывать свои действия, делать примечания и выводы. Избегай списков, если их нет в "
                   "исходном тексте."
                   )

        dialog_manager = DialogManager(browser)

        i = 0

        dialog_manager.send_message(message)
        answer = dialog_manager.get_answer()

        chunkMaker = ChunkMaker(os.path.join(directory, filename))
        message = chunkMaker.get_chunk()
        print(i)
        i += 1
        print(message)

        # working cycle
        while message != '':
            dialog_manager.send_message(message)
            answer = dialog_manager.get_answer()

            f.write(answer)

            message = chunkMaker.get_chunk()
            print(i)
            i += 1
            print(message)

        browser.close()

print("End")