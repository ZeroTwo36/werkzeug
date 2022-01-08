from threading import Thread


def thread_run_simple(app,args=(),debug=False):
    """Lightly Modified Version of run_simple. Used by serving.run_in_thread()

    Args:
        app (Union[function, ABC]): Executed automatically
        args (tuple, optional): Args passed in app(). Defaults to ().
        debug (bool, optional): Debug. Defaults to False.
    """
    print("* Restarting with Werkzeug")
    print("* Running in non-main thread")
    print("* (https://packages.zerotwo36.repl.co/lib/werkzeug/")
    print(f'* Serving app \'{app.__name__}\'...')
    print(f"* Debug Mode: '{'on' if debug else 'off'}'")
    app(args)

class ThreadPoolExecutor:
    def __init__(self):
        self.loops = []
        self.funcs = []
    
    def loop(self,func):
        def wrap(f):
            self.loops.append(Loop(f))
            self.funcs.append(func)
        return wrap
        
class Loop:
    def __init__(self,method) -> None:
        self.method = method

    def start(self,*,in_thread:bool=False):
        if in_thread:
            run_in_thread(self.method)
        else:
            run_simple(self.method)

    
def run_simple(*,app,args=(),debug=False):
    """
    Run a Minimal Application:
    Code is basicly a fancy wrapper around
    ```py
    pool = serving.ThreadPoolExecutor()
    @pool.loop
    def mainloop():
        foo('bar')

    pool.loops[0].start()
    ```

    Args:
        app (Union[function, ABC]): Executed automatically
        args (tuple, optional): Args passed in app(). Defaults to ().
        debug (bool, optional): Debug. Defaults to False.
    """
    print("* Restarting with Werkzeug")
    print("* (https://packages.zerotwo36.repl.co/lib/werkzeug/")
    print(f'* Serving app \'{app.__name__}\'...')
    print(f"* Debug Mode: '{'on' if debug else 'off'}'")
    app(args)

def placeholder(*args):
    """
    Use this if you just want to print out a note from serving.run_simple()
    """
    pass

def run_in_thread(app,args=(),debug=False):
    t = Thread(target=thread_run_simple,args=(app,args,debug))