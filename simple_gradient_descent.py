x_old = 0 # The value does not matter as long as abs(x_new - x_old) > precision
x_new = 6 # The algorithm starts at x=6
gamma = 0.01 # step size
precision = 0.00001

# The df/dx for the function x**4 - 3x**3 + 2
def df(x):
    y = 4 * x**3 - 9 * x**2
    return y

# Every iteration updates the x value by calculating the gradient using the current x
# The condition "abs(x_new - x_old) > precision" is used as break condition because as x draws close to the
# desired minimum the gradient is smaller => smaller x updates.
while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new += -gamma * df(x_old)
    print "gradient df({}) was {}. x_new is now -> {}".format(x_old, df(x_old), x_new)
