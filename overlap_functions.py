def overlap(speech_feature, data_x, data_y):
    """
    speech_feature: the feature for which the overlap is being calculated. 
    data_x : first dataset
    data_y: second dataset
    
    data_x and data_y should be pandas dfs with three columns: 'feature', 'RI_lower_limit', and 'RI_upper_limit'. 
    speech_feature should be the value of a row in the 'feature' column for both data_x and data_y
    """

    # lower bounds
    x_lower = data_x.loc[data_x["feature"] == speech_feature,:]["RI_lower_limit"].iloc[0]
    y_lower = data_y.loc[data_y["feature"] == speech_feature,:]["RI_lower_limit"].iloc[0]
    
    # upper bounds
    x_upper = data_x.loc[data_x["feature"] == speech_feature,:]["RI_upper_limit"].iloc[0]
    y_upper = data_y.loc[data_y["feature"] == speech_feature,:]["RI_upper_limit"].iloc[0]

    # want the highest lower bound of the two datasets and the lower of the upper bound
    overlap_start = max([x_lower, y_lower])
    overlap_end = min([x_upper, y_upper])

    # size of the overlap
    overlap_len = max(0, overlap_end - overlap_start)

    # calcualte % overlap
    total_range = max(x_upper, y_upper) - min(x_lower, y_lower)
    percent_overlap = round((overlap_len / total_range) * 100, 1) if total_range > 0 else 0

    return percent_overlap



def overlap_features(data_x, data_y, speech_features, overlap_df, comparisons):
    for i in speech_features:
        overlap_df.loc[overlap_df["feature"] == i,comparisons] = overlap(i, data_x, data_y)

    return overlap_df
