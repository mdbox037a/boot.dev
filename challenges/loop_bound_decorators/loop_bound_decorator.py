from functools import wraps


def log_with(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{level}: {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


handlers = []
levels = ["DEBUG", "INFO", "WARN"]

for i, level in enumerate(levels):

    @log_with(level)
    def handler(x):
        # Pretend this uses i and level in real work
        return (i, level, x)

    handlers.append(handler)

# Later, they oddly behave as if they all captured the last i/level
for h in handlers:
    print(h(42))
