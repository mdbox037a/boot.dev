def get_avg_brand_followers(all_handles, brand_name):
    matches = 0
    num_lists = len(all_handles)
    for influencer_list in all_handles:
        for handle in influencer_list:
            if brand_name in handle:
                matches += 1
    if num_lists == 0:
        return None
    return matches / num_lists
