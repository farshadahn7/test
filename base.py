from abc import ABC


class Base(ABC):
    _id = 0
    object_list = list()

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.save(self)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def save(cls, obj):
        obj.object_list.append(obj)
