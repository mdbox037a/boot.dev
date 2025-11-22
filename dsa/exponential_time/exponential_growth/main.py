def exponential_growth(n, factor, days):
    growth_sequence = []
    followers = n
    for day in range(0, days + 1):
        growth_sequence.append(followers)
        followers = followers * factor
    return growth_sequence
