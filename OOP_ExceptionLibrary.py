
@implements_to_string
class HTTPException(Exception):

    """
    Baseclass for all HTTP exceptions. This exception can be called as WSGI
    application to render a default error page or you can catch the subclasses
    of it independently and render nicer error message. 
    """

    code = None
    description = None

    def __init__(self, description = None, response = None):
        Exception.__init__(self)
        if description is not None:
            self.description = description
        self.response = response 

@classmethod
def wrap(cls, exception, name=None):
    class newcls(cls, exception):
        def __init__(self, arg=None, *args , **kwargs):
            cls.__init__(self, *args, **kwargs)
            exception.__init__(self, arg)
    
    newcls.__module__ = sys._getframe(1).f_globals.get('__name__')
    newcls.__name__ = name or cls.__name__ + exception.__name__
    return newcls 

@property 
def name(self):
    pass
