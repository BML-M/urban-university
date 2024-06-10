

import webbrowser

url = "
https://drive.google.com/file/d/12U77o_qAm_ewzR9biGmT_yOVh3ZelZqA/view?usp=drive_link"
browser_path = r"C:\Users\Боровской Михаил\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
webbrowser.register('yandex', None, webbrowser.BackgroundBrowser(browser_path))
webbrowser.get('yandex').open(url)


