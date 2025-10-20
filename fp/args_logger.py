def args_logger(*args, **kwargs):
    i = 1
    for arg in args:
        print(f"{i}. {arg}")
        i += 1
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")

