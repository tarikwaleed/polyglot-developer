class Base:
    def foo(self, x):
        print("Base foo", self, x)


class Derived(Base):
    def foo(self, x):
        print("Derived foo", self, x)
        super().foo(x)


derived = Derived()
derived.foo(42)
