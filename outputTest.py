import matplotlib.pyplot as plt
import numpy as np
#import FileDialog

def sum():
   #first = 5
   first = input('What number do you want to start with? [greater or equal to 1] ')
   first = int(first)
   print('First number is {}'.format(first))
   second = 10
   result = first + second
   print('second number is {}'.format(second))
   print('Sum is = {}'.format(result))
   
   
sum()
# Prepare the data
x = np.linspace(0, 10, 100)
# Plot the data
plt.plot(x, x, label='linear')
# Add a legend
plt.legend()
# Show the plot
plt.show()

end=input('enter to exit ')