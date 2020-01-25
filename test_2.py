class Base:
    __slots__ = 'foo', 'bar'


class Right(Base):
    __slots__ = 'baz',


class Wrong(Base):
    __slots__ = 'foo', 'bar', 'baz'


b = Wrong()
print([b.__slots__])
