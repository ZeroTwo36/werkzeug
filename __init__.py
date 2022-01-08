"""
Werkzeug: Comprehensive Project Management Toolkit

Using Werkzeug, you can easily run and debug your Programs

Basic Usages:

```py
from werkzeug.serving import run_simple

run_simple(app=print,args=("Hello"))
```

Or, in advanced Programs:
```py
from werkzeug.serving import run_simple
from simplewsgi import WSGIApplication, Endpoint


@Endpoint
def main():
    return "Hello World"

app = WSGIApplication(main)

run_simple(app=app,args=("localhost",8080))
```

Debugging an App:

```py
from werkzeug.debug import Debugger,DebugFile,Settings,TimeConverter,secure_error

file = DebugFile("hello.py")
debug = Debugger()
debug.settings(Settings(
    restart_every=TimeConverter("1m"),
    on_error=secure_error
))
debug.start(file)

```
"""

__title__ = 'werkzeug'
__author__ = 'ZeroTwo36'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present ZeroTwo36'
__version__ = '2.0.0a3'

from .debug import *
from .serving import *
