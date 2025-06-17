""" Using nested control sattements to analyze examination results."""

# initialize variables
passes = 0    #number of passe
failures = 0   #number of fail


# process n students
n=int(input("Enter the number:"))
for students in range(n):
    # get one exam result
    result=int(input("Enter result (1 = pass, 2 = fail): "))

    if result == 1:
        passes += 1
    else:
        failures += 1

# termination phase
print("No of passed student = " , passes)
print("No. of failed student = ", failures)

if passes > 10:
    print("Bonus to instructer")
