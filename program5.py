import numpy as np

# rewrite this function without a for loop using NumPy array operations
def calc_mean_std(my_list):
    """
    Calculate the mean and standard deviation of numbers in a list.

    Parameters
    ----------
    my_list : list
        The list of numbers to calculate summary statistics of.

    Returns
    -------
    mean : float
        The mean of the list of numbers.
    std : float
        The standard deviation of the list of numbers.
    """
    my_list = np.array(my_list)
    
    # caluclate mean
    sum_of_list = np.sum(my_list)
    mean = sum_of_list / len(my_list)
    
    # calculate std dev
    sqrd_dev = np.sum((my_list - mean) ** 2)
    variance = sqrd_dev / (len(my_list) -1)
    std_dev = np.sqrt(variance)

    return mean, std_dev

my_list = [1, 2, 3, 4, 5]

print(calc_mean_std(my_list))