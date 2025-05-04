def binary_search(arr, target):
    """
    Performs binary search on a sorted list.
    Returns the index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if arr[mid] == target:
            return mid  # Target found

        elif arr[mid] < target:
            left = mid + 1  # Search in the right half

        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found

# Welcome Message
print("\n\t\t\t======== Welcome to the Binary Search Game! ========\n")
print("Think of a number, and I will find it in the sorted list!\n")

# Game Loop
while True:
    # Example sorted list
    numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72,]  
    print(f"Here is the list: {numbers}")

    # User input
    target = int(input("\nEnter the number you want to search for: "))

    # Perform binary search
    result = binary_search(numbers, target)

    # Display result
    if result != -1:
        print(f"\n\t\t\t===== Hooray! Your number {target} is at position {result}. =====")
    else:
        print(f"\n❌ Oops! The number {target} is not in the list.")

    # Ask if the user wants to play again
    play_again = input("\n Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n\t\t\t========= Thanks for playing! See you next time! =========")
        break
