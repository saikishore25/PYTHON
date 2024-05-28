#Program to calculate simple interest 

principal = int(input("Enter the amount borrowed below: \n"))
time = int(input("Enter the duration below: \n"))
rate = float(input("Enter the interest at which you have borrowed: \n"))

simple_interest = (principal*time*rate)/100

print(f"The Simple Interest For the amount of {principal} borrowed at rate of{rate} for a period of {time} is {simple_interest}")