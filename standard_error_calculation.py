import math

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
    
print(calculate_standard_error(0.0112,12933,0.0157,12938,True)) # 0.00143