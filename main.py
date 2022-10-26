import matplotlib.pyplot as plt #importing plotting tool

def collatz_conjecture(n): #collatz conjecture with plotting
    array_for_the_plot = [] #array for storing collatz conjecture values
    array_for_the_plot.append(n)
    #collatz conjecture itself
    while(n != 1):
        if(n % 2 == 0):
            n = n // 2
            array_for_the_plot.append(n)
        else:
            n = n * 3 + 1
            array_for_the_plot.append(n)
    #ploting
    steps = [x+1 for x in range(len(array_for_the_plot))]
    plt.plot(steps, array_for_the_plot)
    plt.axis([1, len(steps), 0, max(array_for_the_plot)])
    plt.ylabel("collatz conjecture values")
    plt.xlabel("step")
    plt.show() #show the plot

print("Enter a positive integer to display a plot with collatz conjecture values for the positive integer: ", end='')

n = int(input()) #reading the positive integer

if(n >= 1): #checking if the input is valid
    collatz_conjecture(n)
else:
    print("The number that was given is not valid for the collatz conjecture.")