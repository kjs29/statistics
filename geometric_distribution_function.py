import math

def geometric_distribution_function(p,trials):
    
    # Probability of getting 1st success on trial #$x$
    # Every trial should be an independent event of one another
    # p: probability of success
    # trials : how many trials it takes to have the first success.


    q = 1 - p
    print(f"mean(Expected value) : {1/p}")
    print(f"Standard deviation: {math.sqrt(q)/p}")
    print(f"probability of first success on {trials} trials : {(q**(trials - 1)) * p}")

    sum = 0
    for i in range(1, trials+1):
        sum += ((q**(i - 1)) * p)
    print(f"cumulative sum : {sum}")
