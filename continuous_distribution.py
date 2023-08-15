import math

def exponential_distribution(l,a):
    # l: lambda
    # a: number on x axis
    
    ######################################################
    #                                                    #
    #    Make sure to know what values we are given      #
    #                                                    #
    ######################################################

    print(f"mean or rate parameter: {1/l}")
    
    answer = 1 - (math.e**(-l*a))
    print(f"P(x<{a} : {answer})")
    print(f"P(x>{a} : {1-answer})")

    print(f"mean: {1/l}")
    print(f"standard dev: {1/l}")

def uniform_distribution(a,b,percentile=0):

    # X ranges from a to b
    # percentile: calculates percentile
    print(f"f(x) or Probability density function = {1}/{b-a} or {1/(b-a)}")

    print(f"mean: {(a+b)/2}")

    print(f"standard dev : {(b-a)/math.sqrt(12)}")

    if percentile > 0:
        ans = a + (b-a) * (percentile/100)
        print(f"{percentile}th percentile : {ans}")
