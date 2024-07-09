import math
from scipy.stats import norm

def calculate_standard_error(p1,n1,p2=0,n2=0,diff=False):
    """
    Calculate the standard error for a proportion or the difference between two proportions.
    
    Parameters:
    p1 (float): Point estimate for sample 1
    n1 (int): Sample size for sample 1
    p2 (float, optional): Point estimate for sample 2 (default is 0)
    n2 (int, optional): Sample size for sample 2 (default is 0)
    diff (bool, optional): If True, calculate the standard error for the difference between two proportions (default is False)
    
    Returns:
    float: The standard error
    """
    if diff:
        return math.sqrt((p1 * (1 - p1)) / n1 + (p2 * (1 - p2)) / n2)
    else:
        return math.sqrt((p1 * (1 - p1)) / n1)

def calculate_z_score(confidence_level):
    """
    Calculate the z-score for a given confidence level.
    
    Parameters:
    confidence_level (float): The confidence level for which to calculate the z-score
    
    Returns:
    float: The z-score
    """
    alpha = 1 - confidence_level
    cumulative_probability = 1 - alpha / 2
    z_score = norm.ppf(cumulative_probability)
    
    return z_score

def calculate_confidence_interval(p1, n1, confidence_level=0.95, diff=False, p2=0, n2=0):
    """
    Calculate the confidence interval for a proportion or the difference between two proportions.
    
    Parameters:
    p1 (float): Point estimate for sample 1
    n1 (int): Sample size for sample 1
    confidence_level (float, optional): Confidence level for the interval (default is 0.95)
    diff (bool, optional): If True, calculate the confidence interval for the difference between two proportions (default is False)
    p2 (float, optional): Point estimate for sample 2 (default is 0)
    n2 (int, optional): Sample size for sample 2 (default is 0)
    
    Returns:
    tuple: The lower and upper bounds of the confidence interval
    """
    # Calculate the standard error
    standard_error = calculate_standard_error(p1, n1, p2, n2, diff)
    
    # Calculate the z-score for the given confidence level
    z_score = calculate_z_score(confidence_level)
    
    # Calculate the margin of error
    margin_of_error = z_score * standard_error
    
    # Calculate the confidence interval
    if diff:
        point_estimate = p1 - p2
    else:
        point_estimate = p1

    lower_bound = point_estimate - margin_of_error
    upper_bound = point_estimate + margin_of_error
    
    return lower_bound, upper_bound


se1 = calculate_standard_error(0.0112,12933,0.0155,12938,True)
ci1 = calculate_confidence_interval(0.0112, 12933, 0.95, True, 0.0155, 12938)

print(se1) # 0.0014267986837244186
print(ci1) # (-0.007096474033289016, -0.0015035259667109842)