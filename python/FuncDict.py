# Subclasses dict and provides an alternative to the original get

# set the function using dict_var.func = function

# the input function should be of form

class FuncDict(dict):

    # self.func
    # (key, self) => (value, [newKeys], [newValues])

    def clear(self):
        self.func = None
        return super(FuncDict, self).clear()

    # (self, key, default) => (value, success)
    # success is true if self.func worked
    def fget(self, key, default=None):
        if key in self:
            return self[key]
        try:
            value, newKeys, newValues = self.func(key, self)
            success = True
            if len(newKeys) != len(newValues):
                success = False
            else:
                for key, value in zip(newKeys, newValues):
                    self[key] = value
            return value, success
        except AttributeError:
            return (super(FuncDict, self).get(key, default), False)
