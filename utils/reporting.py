import sys
import time
import traceback

import allure


def attach_png(attachment, attachment_name="Screenshot"):
    """Attach IMAGE/PNG to report"""

    allure.attach(attachment, attachment_name, allure.attachment_type.PNG)


def screenshot(func):
    """ Decorator function which takes screenshot at Allure step.
        Decorate function with you want to produce screenshots
        Can be called only with <Page> instance
    """

    def wraps(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
            time.sleep(0.3)
            png = args[0].driver.get_screenshot_as_png()
            attach_png(png)
        except Exception:
            _type, _value, _traceback = sys.exc_info()
            raise _type(''.join(traceback.format_exception(_type, _value, _traceback)))
        return result

    return wraps
