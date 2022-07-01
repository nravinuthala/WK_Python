def decorator_fn(fn):
    print('Extra functionality')
    name = "Bob"
    fn(name)


@decorator_fn
def decorated_fn(name):
    print(f"basic functionality for {name}")