def insertion_sort_desc(arr):
    """
    Sorts an array in descending order using the insertion sort algorithm.
    
    Algorithm: Build the final sorted array one item at a time. Each iteration
    takes an element from the unsorted part and inserts it into its correct
    position in the sorted part.
    
    Time Complexity: O(n²) - worst and average case
    Space Complexity: O(1) - in-place sorting
    
    Args:
        arr (list): The array to be sorted
        
    Returns:
        list: The sorted array in descending order
    """
    # Start from the second element (index 1) since the first element is considered sorted
    for i in range(1, len(arr)):
        # Store the current element as the key to be inserted
        key = arr[i]
        # Start comparing with the element just before the current position
        j = i - 1

        # Move elements of arr[0..i-1] that are smaller than key
        # to one position ahead of their current position
        # Note: We use < instead of > for descending order
        while j >= 0 and arr[j] < key:
            # Shift the larger element to the right
            arr[j + 1] = arr[j]
            # Move to the previous element
            j -= 1

        # Insert the key into its correct position
        # j+1 is the correct position because we decremented j in the loop
        arr[j + 1] = key

    return arr

if __name__ == "__main__":
    # Main execution block - runs when the script is executed directly
    print("Enter numbers separated by spaces (e.g., 5 2 9 1 5 6):")
    try:
        # Get input from user and convert to list of integers
        user_input = input().strip()  # Remove leading/trailing whitespace
        data = [int(x) for x in user_input.split()]  # Convert string to list of integers
        
        # Handle case where no valid numbers were entered
        if not data:
            print("No valid numbers entered. Using default array.")
            data = [5, 2, 9, 1, 5, 6]  # Default test array
        
        # Display the original array
        print(f"Original array: {data}")
        
        # Sort the array in descending order
        sorted_data = insertion_sort_desc(data)
        print("Sorted in decreasing order:", sorted_data)
        
    except ValueError:
        # Handle invalid input (non-numeric values)
        print("Invalid input. Please enter only numbers separated by spaces.")
