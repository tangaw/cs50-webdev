def announce(f):
  def wrapper():
    print("Starting function")
    f()
    print("Function completed execution")
  return wrapper

@announce
def hello():
  print("Hello, world!")


hello()