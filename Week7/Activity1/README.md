# Factory Design Pattern Explanation

The sample code in `factory_pattern.py` demonstrates the Factory Design Pattern by using a factory class to create animal objects without the client code directly creating those objects.

## How the Factory Pattern Is Used

The `Factory` class is an abstract base class. It defines an abstract method called `create_product()`, which means any concrete factory class should provide its own implementation of that method.

`AnimalFactory` is the concrete factory. Its `create_product()` method receives a value called `kind` and decides which animal object to create:

- If `kind == "dog"`, it creates and returns a `Dog` object.
- If `kind == "cat"`, it creates and returns a `Cat` object.

This means the client code does not need to know the details of how a `Dog` or `Cat` object is created. The client only asks the factory for a product.

Example from the client code:

```python
animal_factory = AnimalFactory()
dog = animal_factory.create_product(kind="dog")
dog.run()
```

Here, the client creates an `AnimalFactory`, asks it to create a `"dog"`, and then calls the `run()` method on the returned object.

## Classes and Subclasses in the Code

Yes, the sample code contains classes and subclasses.

`Factory` is an abstract parent class. `AnimalFactory`, `DogFactory`, and `CatFactory` are subclasses of `Factory`.

`Animals` is another abstract parent class. `Dog` and `Cat` are subclasses of `Animals`.

The inheritance structure is:

```text
Factory
  AnimalFactory
  DogFactory
  CatFactory

Animals
  Dog
  Cat
```

`DogFactory` and `CatFactory` are included as subclasses of `Factory`, but their `create_product()` methods are empty in the current implementation. The working factory in this sample is `AnimalFactory`.

## Outcome of the Implementation

When the program runs, it creates an `AnimalFactory` object. Then it asks the factory to create a dog by passing `kind="dog"`.

The factory returns a `Dog` object. After that, the client calls:

```python
dog.run()
```

The `Dog` class implements the `run()` method, so the output is:

```text
I'm a Dog, I can run!!
```

The main outcome is that object creation is separated from the client code. Instead of writing `Dog()` directly in the client section, the code uses `AnimalFactory.create_product()` to decide which object should be created. This makes the code easier to extend because new animal types can be added by updating the factory logic and creating new animal subclasses.

