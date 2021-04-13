# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

words = ['I', 'love', 'Python']
for w in words:
    print(w, len(w))

x = int(input("Please enter an integer:"))
if x < 0:
    print("negative")
elif x == 0:
    print("Zero")
elif x == 1:
    print("One")
else:
    print("More")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
