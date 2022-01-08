import os
import contextlib
import threading
import sys
from typing import Iterable

def get_dir(__path):
    if os.path.exists(__path):
        return os.listdir(__path)
    else:
        return ("Error","Didn't find {}".format(__path))

class IterTool:
    def __init__(self,iterable:Iterable=()):
        self.iter = iterable
        self.TotalIterable = TotalIterable

    def fetch_iterable(self):
        return self.TotalIterable(self.iter)

    def kill(self):
        self.iter = None
    
    def as_string(self):
        return concat(self.TotalIterable(self.iter).as_list())
    
    def xinit(self,**kwargs):
        for i in list(kwargs.keys()):
            self.__setattr__(i,kwargs.get(i))


class TotalIterable:
    def __init__(self,data,cls=list) -> None:
        """
        Iterable with conversion functions
        """
        self.data = cls(data)

    def as_list(self):
        return list(self.data)

    def render(self,model):
        """Extends a werkzeug.wrappers.Model().iter()

        Args:
            model (Model): Model without iter set
        """
        if model.initialized:
            model.kill('iter')

        model.init_iterable(self.data)

    def as_tuple(self):
        return tuple(self.data)



class Console:
    def __init__(self,*,output=sys.stdout):
        self.output = output

    @classmethod
    def write(self,*data,file=None):
        """Writes Data to a stream, default sys.stdout .
        Difference to print(): If an error Occures, it gets written to a file
        Using werkzeug.debug.secure_error().

        Args:
            file (PathLike, optional): Errors will be parsed there. Defaults to None.

        ```python
        from werkzeug.utils import catch_error,save_error

        catch_error(lambda:print("Hello World")).then(save_error,('traceback.wkzg.err'))

        ```
        """
        self.output.write("".join(data))

class ReturnedFunction:
    def __init__(self,res) -> None:
        self.res = res()

    def then(self,function,*optn):
        return function(optn)

class CaughtError:
    def __init__(self,exception):
        self.error = exception

    def then(self,function,*optn):
        function((self.error,optn))

    def __repr__(self) -> str:
        return '%e: %e' % (self.error.__name__,self.error)

def catch_error(func):
    try:
        return ReturnedFunction(func())
    except Exception as error:
        return CaughtError(error)

class ApplicationSecureDocker:
    def __init__(self,app) -> None:
        self.application = app

    def _RE(self):
        """Restore the Application
        """
        return self.application

class BaseCopy:
    def __init__(self,obj):
        self.obj = obj

    def backup(self):
        return self.obj

    def overwrite(self,__new):
        self.obj = __new

class ExpandableCopy(BaseCopy):
    def __init__(self, obj):
        super().__init__(obj)

    def __subclass_of__(self,cls):
        return isinstance(self.obj,cls)

    def expand(self,*args):
        __temp__ = self.obj
        self.obj = [__temp__]
        for a in args:
            self.obj.append(a)

class FileStorage:
    def __init__(self,content):
        """Holds the Data of a File

        Args:
            content (str): Data
        """
        self._C = content

    def _hold(self):
        return ExpandableCopy(self._C)

    def save(self,fp=...,_BufferStyle=...):
        with open(fp,'w') as f:
            f.write(self._C)

    def wait_for(self,event,check):
        self._OLD = self._hold()
        if event == 'FILE_UPDATE':
            if check(self._OLD):
                return True
            return False

    def _wait_for_changes(self):
        while True:
            if self._OLD != self._C:
                ...

class FileName(FileStorage):
    def __init__(self,filename):
        super().__init__(open(filename).read())
        self.fn = filename

    


def secure_application(_A,securit=ApplicationSecureDocker):
    """Secures an Application in a Container that allows restoration of the App

    Args:
        _A (FileStorage,Filename): If String, a filename otherwise a werkzeug.utils.FileStorage 
        securit (Any@Container,FileStorage, optional): [description]. Defaults to ....

    Raises:
        Exception

    Returns:
        werkzeug.TypeDef[Container]: 
    """

class DataReader:
    def __init__(self,import_name) -> None:
        self.holder = import_name
        self.content = open(import_name).read()
        
def raise_error(error,*,stream=sys.stdout):
    with contextlib.redirect_stdout(stream):
        raise error

def concat(*args,**kwargs):
    """Concatenate multiple items together. Trap Occuring errors and log them without crashing.
    """
    errorhandler = kwargs['errorhandler'] or raise_error

    try:
        return "".join(args)
    except Exception as _E:
        with open('error.wkzg.err','w') as f:
            errorhandler(_E,stream=f)

class method(object):
    def __init__(self) -> None:
        super().__init__()