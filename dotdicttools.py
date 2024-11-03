__version__ = "0.0.18"


class DotDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, d={}):
        for k, v in d.items():
            self[k] = v

    def __setitem__(self, k, v):
        return dict.__setitem__(self, k, DotDict(v) if isinstance(v, dict) else v)
