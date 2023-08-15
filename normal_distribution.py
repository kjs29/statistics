import math

def normal_distribution_z_score(x, mean, std_dev):
    print(f"mean is {mean}")
    print(f"Z score is {(x-mean)/std_dev}")

    # print("Z represents standard deviation")
    # print("Z=1 ranges includes 68% of whole data")
    # print("Z=2 ranges includes 95% of whole data")
    # print("Z=3 ranges includes 99.7% of whole data")

def normal_distribution_x(z, mean, std_dev):
    print(f"x value : {(z*std_dev)+mean}")

