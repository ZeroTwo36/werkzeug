import os
from .utils import *
import contextlib

class Settings:
    def __init__(self,*,restart_every=None,on_error=raise_error) -> None:
        self.every = restart_every
        self.errorhandler = on_error

class DebugFile:
    def __init__(self,__import_name):
        self.name = __import_name
        self.data = DataReader(self.name)

def secure_error(error,stream):
    stream.write(str(error))

def TimeConverter(time):
    pos = ["s","m","h","d"]
    time_dict = {"s":1,"m":60,"h":3600,"d":3600*24}
    unit = time[-1]
    
    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

class Debugger:
    def __init__(self) -> None:
        self._prep()

    def _prep(self):
        self.config = Settings()

    def settings(self,__new__:Settings):
        self.config = __new__

    def start(self,file:DebugFile,*,stream=sys.stdout):
        try:
            with contextlib.redirect_stdout(stream):
                eval(file.data.content)
        except:
            try:     
                with contextlib.redirect_stdout(stream):
                    exec(file.data.content)
            except Exception as error:
                self.config.errorhandler(error,stream=stream)