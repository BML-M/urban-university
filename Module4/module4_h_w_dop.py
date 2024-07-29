
import webbrowser

url = "https://drive.google.com/file/d/1kFP-mYOISfbA0vH-xsvlgaQihjl2jgyT/view"
browser_path = r"C:\Users\Боровской Михаил\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
webbrowser.register('yandex', None, webbrowser.BackgroundBrowser(browser_path))
webbrowser.get('yandex').open(url)




