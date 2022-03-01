from collections import OrderedDict


class Field(object):
    def __init__(self, name, name_of_type):
        self.name = name
        self.ttype = name_of_type

class SerializerMetaclassTest(type):
    """
    This metaclass sets a dictionary named `_declared_fields` on the class.

    Any instances of `Field` included as attributes on either the class
    or on any of its superclasses will be include in the
    `_declared_fields` dictionary.
    """

    @classmethod
    def _get_declared_fields(cls, bases, attrs):
        print(attrs.items()) # dict_items([('__module__', '__main__'), ('__qualname__', 'Dog'), ('id', <__main__.Field object at 0x10bb1d8d0>), ('age', <__main__.Field object at 0x10bb1d9d0>)])
        print(type(attrs.items()))  # <class 'dict_items'>
        fields = [(field_name, attrs.pop(field_name))
                  for field_name, obj in list(attrs.items())
                  if isinstance(obj, Field)]
        print(fields)   # [('id', <__main__.Field object at 0x10b51a890>), ('age', <__main__.Field object at 0x10b51a990>)]
        fields.sort(key=lambda x: x[1]._creation_counter)

        # Ensures a base class field doesn't override cls attrs, and maintains
        # field precedence when inheriting multiple parents. e.g. if there is a
        # class C(A, B), and A and B both define 'field', use 'field' from A.
        known = set(attrs)

        def visit(name):
            known.add(name)
            return name

        base_fields = [
            (visit(name), f)
            for base in bases if hasattr(base, '_declared_fields')
            for name, f in base._declared_fields.items() if name not in known
        ]

        return OrderedDict(base_fields + fields)

    def __new__(cls, name, bases, attrs):
        print(name) # dog
        print(bases)    # ()
        print(attrs)    # {'__module__': '__main__', '__qualname__': 'Dog', 'id': <__main__.Field object at 0x100a0a8d0>, 'age': <__main__.Field object at 0x100a0a9d0>}
        attrs['_declared_fields'] = cls._get_declared_fields(bases, attrs)
        return super().__new__(cls, name, bases, attrs)


class Dog(metaclass=SerializerMetaclassTest):
    id = Field('id', 'str')
    age = Field('age', 'int')
