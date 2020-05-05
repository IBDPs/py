class number:
    def __init__(self):
        pass
    
    def cube_subtract(self, number1, cube_max1, cube_max2):
        for cube1 in range(0, cube_max1):
            for cube2 in range(0, cube_max2):
                if abs(cube1**3 - cube2**3) == number1:
                    print(str(number1) +" is also {} cubed".format(str(cube1)) + " minus {} cubed.".format(str(cube2)))
    
 
 
nineteen_cubes = number.cube_subtract(19, 5, 5)
 
*ROMAN NUMERALS*
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100,c'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
 
number = int(input("Enter Number: "))
def num2roman(num):
    roman = ''
 
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
 
    return roman
print("- Roman Numeral Of", number, ":", num2roman(number))
 
*BINARY*
number = int(input("Enter number: "))
binary = bin(number)[2:]
print("- Binary Number Of", number, ":", binary)
 
*HEXADECIMAL*
number = int(input("Enter number: "))
hexadecimal = hex(number)[2:]
print("- Hexadecimal Of", number, ":", hexadecimal)
 
*FACTORS*
factors_list = []
count = 0
number = int(input("Enter number: "))
 
for i in range(1, number+1):
         if number % i == 0:
              factors_list.append(i)
              count = count + 1
              
print("- Factors Of", number,":", factors_list)
print("- Number Of Divisible Factors Of", number, ":", count)
 
if count == 2:
    print("-",number, "Is Prime")
else:
  print("-",number, "Is Not Prime")
 
*PALINDROME*
number = int(input("Enter number: "))
store = number
reverse = 0
while(number>0):
    last_digit = number % 10
    reverse = reverse * 10 + last_digit
    number = number//10
if store == reverse:
    print("-", store, "Is A Palindrome")
else:
    print("-", store, "Is Not A Palindrome")
 
*PLOTS*
import matplotlib.pyplot as plt
import numpy as np
 
# Canvas
plt.style.use("ggplot")
 
# Frequency, Oscillations & TimeRange
f = int(input("Enter frequency: "))
n_o = int(input("Enter number of oscillations: "))
t_max = n_o/f
t = np.linspace(0, t_max, 1000)
 
# Sin, Cos & Tan
y_sin = np.sin(2*np.pi*f*t)
y_cosec = 1/y_sin
 
y_cos = np.cos(2*np.pi*f*t)
y_sec = 1/y_cos
 
y_tan = np.tan(2*np.pi*f*t)
y_cotan = 1/y_tan
 
# Setting subplots on separate axes
fig, axs = plt.subplots(4, 1, constrained_layout = True)
 
# Sine axis
axs[0].plot(t, y_sin, color = "firebrick", label = "sin({}Hz)".format(f))
axs[0].plot(t, y_cosec, color = "firebrick", linestyle = "dashed", label = "cosec({}Hz)".format(f))
axs[0].axhline(y = 0, color = "grey", linestyle = "dashed", label = "y = 0")
axs[0].legend(loc = "lower left", frameon = True, fancybox = True,
              shadow = True, facecolor = "white")
 
# Title
axs[0].set_title("Sine", fontweight = "bold")
axs[0].set_xlabel("Time(s)")
axs[0].set_ylabel("Amplitude")
 
# Axis limits
axs[0].axis([-0.05*t_max, t_max+0.05*t_max, -1.5, 1.5])
 
# Cosine axis
axs[1].plot(t, y_cos, color = "teal", label = "cos({}Hz)".format(f))
axs[1].plot(t, y_sec, color = "teal", linestyle = "dashed", label = "sec({}Hz)".format(f))
axs[1].axhline(y = 0, color = "grey", linestyle = "dashed", label = "y = 0")
axs[1].legend(loc = "lower left", frameon = True, fancybox = True,
              shadow = True, facecolor = "white")
 
# Title
axs[1].set_title("Cosine", fontweight = "bold")
axs[1].set_xlabel("Time(s)")
axs[1].set_ylabel("Amplitude")
 
# Axis limits
axs[1].axis([-0.05*t_max, t_max+0.05*t_max, -1.5, 1.5])
 
# Tan axis
axs[2].plot(t, y_tan, color = "Tomato", label = "tan({}Hz)".format(f))
axs[2].plot(t, y_cotan, color = "Tomato", linestyle = "dashed", label = "cotan({}Hz)".format(f))
axs[2].axhline(y = 0, color = "grey", linestyle = "dashed", label = "y = 0")
axs[2].legend(loc = "lower left", frameon = True, fancybox = True,
              shadow = True, facecolor = "white")
 
# Title
axs[2].set_title("Tan", fontweight = "bold")
axs[2].set_xlabel("Time(s)")
axs[2].set_ylabel("Amplitude")
 
# Axis limits
axs[2].axis([-0.05*t_max, t_max+0.05*t_max, -10, 10])
 
#FFT
N = len(t)
dt = t[1]-t[0]
H_max = 5
 
yf = np.fft.fft(y_sin)
xf = np.linspace(0.0, 1.0/(2.0*dt), N//2)
 
axs[3].plot(xf, 2/N * np.abs(yf[:N//2]), color = "SteelBlue")
 
axs[3].set_xlim([0,H_max*f])
 
axs[3].annotate("Peak\n({}Hz)".format(f), xy=(f, 1), xytext=(f*2, 0.5),
                ha = "center", bbox=dict(boxstyle="round", fc="white", ec="gray"),
                arrowprops=dict(arrowstyle = "-|>", color = "k"))
 
axs[3].set_title("Fast Fourier Transform", fontweight = "bold")
axs[3].set_xlabel("Frequency(Hz)")
axs[3].set_ylabel("$||H_i||_2$")
 
plt.savefig("Trigonometric_Plots_{}Hz.pdf".format(f))
plt.show()
 
 
 
Subtraction of two cubes == num
Sum of two cubes == num
Prime factors 
Plots
Composite or prime
Palindromes
Fourier transform individual frequency
Modular Arithmetic %
Modular functions
Binary
Hexadecimal
Roman Numerals



Cubic and quadratic functions differentiation
1, 16, 81, 256, 625, 1296
15, 65, 175, 369, 671
50, 110, 194, 302
60, 84, 108
24, 24

1, 8, 27, 64, 125
7, 19, 37, 61
6, 12, 18, 24
6, 6, 6,

1, 4, 9, 16, 25, 36
3, 5, 7, 9
2, 2, 2,
