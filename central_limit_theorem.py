import math

def z_score_for_samples(mean, n, stdev, x):

    # mean: mean
    # n : size
    # stdev : standard deviation
    # x : sample point on x axis
    sem = stdev/math.sqrt(n)
    print(f"Standard deviation of the sample mean : {sem}")

    print(f"Z-score : {(x-mean)/sem}")

def z_score_to_probability(z):
    if z < 0:
        print("if z is -2.83, then find (0.5 - P(x=|2.83|))")
        print("for example, if P(x<=2.83) = 0.99767,")
        print("answer is 1 - 0.99767")
    else:
        print("if z is 1.5, then find 0.5 + P(1.5)")
