import numpy as np


class DataAnalytics:

    def __init__(self):
        self.array = None

    def run(self):

        print("Welcome to the NumPy Analyzer!")
        print("="*40)

        while True:
            print("\nChoose an option:")
            print("1. Create a Numpy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    self.create_array()
                case 2:
                    self.math_operations()
                case 3:
                    self.combine_or_split()
                case 4:
                    self.search_sort_filter()
                case 5:
                    self.aggregates_statistics()
                case 6:
                    print("\nThank you for using the NumPy Analyzer! Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")

    def create_array(self):

        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                elements = input("Enter elements separated by space: ").split()
                elements = [int(x) for x in elements]
                self.array = np.array(elements)

            case 2:
                rows = int(input("\nEnter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total = rows*cols
                elements = input(
                    f"\nEnter {total} elements separated by space: ").split()
                elements = [int(x) for x in elements]
                self.array = np.array(elements).reshape(rows, cols)

            case 3:
                layer = int(input("Enter the number of layers: "))
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total = layer*rows*cols
                elements = input(
                    f"Enter {total} elements separated by space: ").split()
                elements = [int(x) for x in elements]
                self.array = np.array(elements).reshape(layer, rows, cols)

            case _:
                print("Invalid choice.")
                return

        print("\nArray created successfully:")
        print(self.array)

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")

        operation = int(input("Enter your choice: "))

        match operation:
            case 1:
                self.index_array()
            case 2:
                self.slice_array()
            case 3:
                pass
            case _:
                print("Invalid choice.")

    def index_array(self):

        r_index = int(input("Enter row index: "))
        c_index = int(input("Enter column index: "))
        print("Element:", self.array[r_index][c_index])

    def slice_array(self):

        row_range = input("Enter the row range (start:end): ").split(":")
        col_range = input("Enter the column range (start:end): ").split(":")
        print("Sliced Array:")
        print(self.array[int(row_range[0]):int(row_range[1]),
              int(col_range[0]):int(col_range[1])])

    def combine_or_split(self):

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                elements = input(
                    f"\nEnter {self.array.size} elements for second array separated by space: ").split()
                elements = [int(x) for x in elements]
                second_array = np.array(elements).reshape(self.array.shape)
                print("\nOriginal Array:")
                print(self.array)
                print("\nSecond Array:")
                print(second_array)

                print("\nHow would you like to combine array?")
                print("1. Horizontal (side by side)")
                print("2. Vertical (one on the top of other)")
                combine_choice = int(input("Enter your choice:"))

                if combine_choice == 1:
                    combined_h = np.hstack((self.array, second_array))
                    print("\nCombined array (Horizontal stack):")
                    print(combined_h)

                elif combine_choice == 2:
                    combined_v = np.vstack((self.array, second_array))
                    print("\nCombined array (Vertical stack):")
                    print(combined_v)

            case 2:
                print("\n1. Vertical Split")
                print("2. Horizontal Split")

                split_choice = int(input("Enter your choice: "))
                parts = int(input("Enter number of parts to split into: "))
                print("Original Array:")
                print(self.array)

                if split_choice == 1:
                    split_result = np.vsplit(self.array, parts)
                    print("\nVertical Split :")
                    print(split_result)

                elif split_choice == 2:
                    split_result = np.hsplit(self.array, parts)
                    print("\nHorizontal Split :")
                    print(split_result)

                else:
                    print("Invalid choice.")

            case _:
                print("Invalid choice.")

    def math_operations(self):

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))

        elements = input(
            f"\nEnter {self.array.size} elements for second array separated by space: ").split()
        elements = [int(x) for x in elements]
        second_array = np.array(elements).reshape(self.array.shape)
        print("\nOriginal Array:")
        print(self.array)
        print("\nSecond Array:")
        print(second_array)

        match choice:
            case 1:
                print("\nResult of Addition:")
                print(self.array + second_array)
            case 2:
                print("\nResult of Subtraction:")
                print(self.array - second_array)
            case 3:
                print("\nResult of Multiplication:")
                print(self.array * second_array)
            case 4:
                print("\nResult of Division:")
                print(self.array / second_array)
            case _:
                print("Invalid choice.")

    def search_sort_filter(self):

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                value = int(input("Enter value to search: "))
                flat_list = self.array.flatten().tolist()
                print("Original Array:")
                print(self.array)
                if value in flat_list:
                    print(f"Value {value} is FOUND in the array.")
                else:
                    print(f"Value {value} is NOT found in the array.")

            case 2:
                print("\n1. Ascending")
                print("2. Descending")
                order = int(input("Enter your choice: "))

                print("\nSort by:")
                print("1. Row-wise")
                print("2. Column-wise")
                axis_choice = int(input("Enter your choice :"))

                if axis_choice == 1:
                    axis = 1
                else:
                    axis = 0

                sorted_arr = np.sort(
                    self.array, axis=axis)
                if order == 2:
                    if axis == 0:
                        sorted_arr = sorted_arr[::-1]
                    else:
                        sorted_arr = sorted_arr[:, ::-1]
                    print("\nSorted Array (Descending):")
                else:
                    print("\nSorted Array (Ascending):")
                print(sorted_arr)

            case 3:
                value = int(input("Show elements greater than: "))
                flat_list = self.array.flatten().tolist()
                filtered = []
                for item in flat_list:
                    if item > value:
                        filtered.append(item)
                print("Original Array:")
                print(self.array)
                print(f"Elements greater than {value}: {filtered}")
            case _:
                print("Invalid choice.")

    def aggregates_statistics(self):

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        choice = int(input("Enter your choice: "))
        print("\nOriginal Array:")
        print(self.array)

        match choice:
            case 1:
                print("\nSum:", np.sum(self.array))
            case 2:
                print("\nMean:", np.mean(self.array))
            case 3:
                print("\nMedian:", np.median(self.array))
            case 4:
                print("\nStandard Deviation:", np.std(self.array))
            case 5:
                print("\nVariance:", np.var(self.array))
            case _:
                print("Invalid choice.")


DataAnalytics().run()
