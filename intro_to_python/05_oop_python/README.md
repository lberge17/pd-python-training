# Object Oriented Programming With Python

## Constructor | Initialize

```ruby
class Dog

    def initialize(name)
        @name = name
        @tricks = []
    end

    def add_tricks(trick)
        @tricks.append(trick)
    end

end
```

V.S

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
```

```python
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
=> ['roll over']
 e.tricks
=> ['play dead']
```

## Resources

[Classes Python Docs](https://docs.python.org/3/tutorial/classes.html)
