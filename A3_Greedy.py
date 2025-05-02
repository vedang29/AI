# Selection Sort Function
def selection_sort(num):
    for i in range(len(num)):
        min_index = i
        for j in range(i + 1, len(num)):
            if num[j] < num[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        num[i], num[min_index] = num[min_index], num[i]

# Input Function for Selection Sort
def inp():
    num = []
    n = int(input("Enter number of elements to sort: "))
    for i in range(n):
        a = int(input("Enter element: "))
        num.append(a)
    selection_sort(num)
    print("Sorted array is ", num)

# Bubble Sort Function (used in Job Scheduling)
def bubble_sort(jobs):
    n = len(jobs)
    for i in range(n):
        for j in range(0, n-i-1):
            if jobs[j][2] < jobs[j+1][2]:  # Compare profits and swap if needed
                jobs[j], jobs[j+1] = jobs[j+1], jobs[j]

# Job Scheduling Function
def job_scheduling(jobs, n):
    bubble_sort(jobs)  # Sort jobs by profit using bubble sort
    
    result = [None] * n  # Result array to store job sequences
    slot = [False] * n   # Slot availability array

    # Iterate over the sorted jobs
    for job in jobs:
        for j in range(min(n, job[1]) - 1, -1, -1):  # Find a free slot for this job
            if not slot[j]:
                result[j] = job[0]
                slot[j] = True
                break
    
    # Print the scheduled jobs
    print("Jobs scheduled in order:", [job for job in result if job])

# Menu Function
def menu():
    while True:
        print("\nMenu:")
        print("1. Job Scheduling Problem")
        print("2. Selection Sort")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            print("\nJob Scheduling Problem")
            n = int(input("Enter number of jobs: "))
            jobs = []
            for i in range(n):
                job_id = input("Enter job ID: ")
                deadline = int(input("Enter deadline for job: "))
                profit = int(input("Enter profit for job: "))
                jobs.append([job_id, deadline, profit])  # Store job as a list [id, deadline, profit]
            
            job_scheduling(jobs, n)
        
        elif choice == 2:
            inp()  # Selection Sort
        elif choice == 3:
            break
        else:
            print("Invalid choice, please try again.")

# Run the menu
menu()
