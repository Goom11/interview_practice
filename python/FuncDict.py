# Subclasses dict and provides an alternative to the original get

class FuncDict(dict):
    def set_func(self, func):
        self.func = func

    def f_get(self, key, default=None):
        if key in self:
            return self[key]
        try:
            return self.func(key)
        except AttributeError:
            return super(FuncDict, self).get(key, default)
