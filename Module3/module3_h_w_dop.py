
import webbrowser

url = "https://drive.google.com/file/d/1SUOHiI5Qicp0clk9OLIwkdySWluNbWJZ/view?usp=sharing"
browser_path = r"C:\Users\Боровской Михаил\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
webbrowser.register('yandex', None, webbrowser.BackgroundBrowser(browser_path))
webbrowser.get('yandex').open(url)




