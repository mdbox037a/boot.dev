def get_follower_prediction(follower_count, influencer_type, num_months):
    rate = 4
    if influencer_type == "fitness":
        rate = 4
    elif influencer_type == "cosmetic":
        rate = 3
    else:
        rate = 2

    return follower_count * (rate**num_months)
