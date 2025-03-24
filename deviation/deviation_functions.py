import numpy as np

def normalise(df, features_to_normalise, mean_sd_df, reference_dataset):
    """
    df: pandas dataframe which contains features to normalise using reference data.
    features_to_normalise: an array of the feature columns to normalise. 
    mean_sd_df: a df with a row per reference dataset and a column for each of the features_to_normalise. The features should have a tuple of the (mean, sd) of that feature for the given dataset.
    reference_data_set: the dataset (row) in mean_sd_df to use for normalisation. 
    """
    if "dataset" not in mean_sd_df.columns:
        assert "the mean_sd_df column with the dataset names should be named 'dataset"
    
    normalised_df = df.copy()

    for feature in features_to_normalise:
        # find the mean and sd from the correct dataset for the correct feature
        feature_values = mean_sd_df.loc[mean_sd_df["dataset"] == reference_dataset, feature].iloc[0]
        mean, sd = feature_values[0], feature_values[1]
        # standardise
        normalised_df.loc[:, feature] = (normalised_df[feature] - mean)/sd


    print(f"[INFO] Successfully normalised with {reference_dataset}")
    return normalised_df



def calc_dev_scores(df, ri_df, feature_list):
    new_df = df.copy()
    
    for feature in feature_list:
        q3 = ri_df.loc[ri_df["feature"] == feature, "q3"].iloc[0]
        print(q3)
        q1 = ri_df.loc[ri_df["feature"] == feature, "q1"].iloc[0]
        print(q1)
        median = ri_df.loc[ri_df["feature"] == feature, "median"].iloc[0]
        print(median)

        new_df[feature] = new_df[feature].apply(lambda x: score_ds_q123(x, q1, q3, median))
    return new_df



# score_ds_123 function written by C. Botelho (https://github.com/mcatarinatb)
def score_ds_q123(value, q1, q3, median):
    """
    if feature in reference interval: score2 = 0
    otherwise, score2 will be the distance to the edge of th interval,
    normalized by the legth of the half interval. Notice that because we
    are not assuming a normal distribution, the upper and lower half-intervals
    may be different.
    """
    ri_length = np.abs(q3 - q1)/2
    if value > q3:
        return np.abs(q3 - value)/ri_length
   
    elif value < q1:
        return -np.abs(q1 - value)/ri_length
   
    else:
        return 0
