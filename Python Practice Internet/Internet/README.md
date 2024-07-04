# Python Practice Internet

Бурлаков Максим

## Installation

1. Install selenium

```bash
pip install selenium
```

2. Download chromedriver

## Usage

```python
driver_path = 'your-path-to-chromedriver'
browser = BrowserAutomation(driver_path)

# LocalStorage
url = 'webpage-url'
key = 'key'
value = 'value'

browser.open_url(url)
browser.set_local_storage(key, value)
stored_value = browser.get_local_storage(key)
browser.delete_local_storage(key)

# Cookie
url = 'webpage-url'
name = 'name'
value = 'value'

browser.open_url(url)
browser.set_cookie(name, value)
cookie_value = browser.get_cookie(name)
browser.delete_cookie(name)

browser.close()
```

## Testing

The default output shoud be:

```plaintext
Set LocalStorage: exampleKey=Hello world!
LocalStorage value: Hello world!
Set Cookie: exampleCookieValue=1234567890qwerty
Cookie value: 1234567890qwerty
```
