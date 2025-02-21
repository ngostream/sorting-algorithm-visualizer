# main.py

from algorithms import bubble_sort, merge_sort
from ui import visualize_sorting
from utilities import generate_array

def main():
    print("Sorting Algorithm Visualizer")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    choice = int(input("Choose an algorithm (1/2): "))
    n = int(input("Enter the size of the array: "))
    speed = float(input("Enter visualization speed (in seconds): "))
    
    array = generate_array(n)
    if choice == 1:
        visualize_sorting(array, bubble_sort, speed, "Bubble Sort")
    elif choice == 2:
        visualize_sorting(array, merge_sort, speed, "Merge Sort")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
