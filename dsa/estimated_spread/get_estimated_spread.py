def get_estimated_spread(audiences_followers):
    if not audiences_followers:
        return 0
    else:
        average_audience_followers = sum(audiences_followers) / len(audiences_followers)
        return average_audience_followers * (len(audiences_followers) ** 1.2)
