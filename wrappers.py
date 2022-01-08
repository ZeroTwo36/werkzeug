import timeit

class ABC:
    def __init__(self) -> None:
        self.__slots__ = ()

class AbstractSink:
    def __init__(self) -> None:
        pass

class Model:
    def __init__(self,iterable = None) -> None:
        """THe Class, most DeploymentModels() inherit from

        :param: Iterable. Defaults to None.
        
        Example Usage:
        ```py
        from werkzeug.wrappers import Model
        from werkzeug.deployment import dir2list,CustomPush,PushType

        class Pusher(CustomPush):
            def __init__(self,*args):
                super().__init__(*args)
                self.config(pushType=PushType.MODEL)
            
        pushData = Model(dir2list())
        Pusher(pushData).commit('test.wkzg.cmt')
        ```
        """
        self.iter = iterable

    def kill(self,__obj):
        if hasattr(self,__obj):
            self.__setattr__(__obj,None)

    def fetch(self,iterable,**optn):
        for i in iterable:
            if i == optn['key']:
                return i

    def fetch_iterable(self):
        return self.iter if self.iter else ('Null','Unspecified')

    @property
    def initialized(self):
        return not not self.iter

    def init_iterable(self,it):
        self.kill('iter')
        self.init()
        self.iter = it

    def init(self):
        if self.initialized:
            return False

        self.iter = ()

class BaseDeploymentModel(Model):
    def __init__(self, iterable=()) -> None:
        super().__init__(iterable=iterable)

    def init_deployment(self,__dp):
        self.set_deployment = __dp
        