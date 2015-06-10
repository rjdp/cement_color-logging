from cement.core.foundation import CementApp
from cement.core import backend
from cement.utils.misc import init_defaults


# defaults = init_defaults('myapp', 'log.colorlog')
# defaults['log.colorlog']['file'] = 'my.log'

class MyApp(CementApp):

    class Meta:
        label = 'myapp'
        # config_defaults = defaults
        extensions = ['colorlog']
        log_handler = 'colorlog'
with MyApp() as app:
    app.run()
    app.log.debug('This is my debug meassage')
    app.log.info('This is my info message')
    app.log.warn('This is my warning message')
    app.log.error('This is my error message')

