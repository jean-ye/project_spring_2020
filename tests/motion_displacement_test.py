from Jeans_Package.compute_motion_displacement import *

def test_column_avg1():
    sample_data = {'roll':[1, 1, 1], 'pitch':[2, 2, 2], 'yaw':[3, 3, 3], 'z':[4, 4, 4], 'x':[5, 5, 5], 'y':[6, 6, 6]}
    sample_df = pd.DataFrame(data = sample_data)
    results = compute_mean_for_each_column(sample_df)
    assert len(results) == 6

def test_column_avg2():
    sample_data = {'roll':[1, 1, 1], 'pitch':[2, 2, 2], 'yaw':[3, 3, 3], 'z':[4, 4, 4], 'x':[5, 5, 5], 'y':[6, 6, 6]}
    sample_df = pd.DataFrame(data = sample_data)
    results = compute_mean_for_each_column(sample_df)
    output = [1,2,3,4,5,6]
    assert results == output

def test_column_avg3():
    """This is to make sure the function can handle negative numbers too"""
    sample_data = {'roll':[0, 1, -4], 'pitch':[2, 2, -10], 'yaw':[-6, 3, 3], 'z':[4, -8, 4], 'x':[5, 5, 5], 'y':[6, 6, 6]}
    sample_df = pd.DataFrame(data = sample_data)
    results = compute_mean_for_each_column(sample_df)
    output = [-1,-2,0,0,5,6]
    assert results == output

def test_avg_sum1():
    sample_data = {'roll':[1, 1, 1], 'pitch':[2, 2, 2], 'yaw':[3, 3, 3], 'z':[4, 4, 4], 'x':[5, 5, 5], 'y':[6, 6, 6]}
    sample_df = pd.DataFrame(data = sample_data)
    results = compute_mean_for_each_column(sample_df)
    sum_results = compute_mean_of_all_columns(results)
    assert sum_results == 3.5

def test_avg_sum2():
    """This is to make sure the function can handle negative numbers too"""
    sample_data = {'roll':[0, 1, -4], 'pitch':[2, 2, -10], 'yaw':[-6, 3, 3], 'z':[4, -8, 4], 'x':[3, 3, 3], 'y':[6, 6, 6]}
    sample_df = pd.DataFrame(data = sample_data)
    results = compute_mean_for_each_column(sample_df)
    sum_results = compute_mean_of_all_columns(results)
    assert sum_results = 1