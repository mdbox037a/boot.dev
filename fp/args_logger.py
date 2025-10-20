def args_logger(*args, **kwargs):
    count = 0
    for arg in args:
        count += 1
        print(f"{count}. {arg}")

    alpha_kwargs = sorted(kwargs.items())
    count = 0
    for entry in alpha_kwargs:
        print(f"* {alpha_kwargs[count][0]}: {alpha_kwargs[count][1]}")
        count += 1
