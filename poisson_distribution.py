import math

def factorial(n):
    ans = [1,1]

    for i in range(2, n+1):
        ans.append(ans[-1]*i)
    
    return ans[-1]

def poisson_distribution(l, number_of_events, cumulative=False):
    # l: lambda
    
    print(f"mean : {l}")
    print(f"Standard deviation : {math.sqrt(l)}")
    print(f"probability of {number_of_events} : {((math.e**-l)*(l**number_of_events))/factorial(number_of_events)}")

    if (cumulative):
        answer = 0
        for i in range(0,number_of_events+1):
            answer += ((math.e**-l)*(l**i))/factorial(i)
        print(f"Cumulative up to {number_of_events} : {answer}")
        return answer    
    else:
        return ((math.e**-l)*(l**number_of_events))/factorial(number_of_events)
