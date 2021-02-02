import sys

def merge_sort(index, a_list, left = None, right = None):
    """Recursive implementation of merge sort. This method
    will split a_list into its appropriate sub-arrays and
    call merge for each"""
    # if left points to same index, or surpasses right,
    # no need to keep splitting the array
    if left is None:
        left = 0
    if right is None:
        right = len(a_list)
    if left >= right:
        return

    # split array in half, into 2 smaller arrays
    mid = (left + right) // 2
    merge_sort(index, a_list, left, mid)
    merge_sort(index, a_list, mid + 1, right)
    merge(index, a_list, left, right, mid)
    return a_list

def merge(index, a_list, left, right, mid):
    """function that utilizes the series of arrays in order
    to sort the original array, by methodically merging the smaller
    arrays"""
    L = a_list[left:mid+1]
    R = a_list[mid+1:right+1]

    track_left = 0
    track_right = 0

    sorted_thru = left

    while track_left < len(L) and track_right < len(R):
        # actual sorting occurs -- compare left and right indices
        if L[track_left][index] <= R[track_right][index]:
            a_list[sorted_thru] = L[track_left]
            # increment left index tracker
            track_left += 1
        else:
            # right is greater
            a_list[sorted_thru] = R[track_right]
            track_right += 1

        sorted_thru += 1

    # it is possible to have more elements in L or R than the other
    # so this section sorts any remaining elements
    while track_left < len(L):
        a_list[sorted_thru] = L[track_left]
        track_left += 1
        sorted_thru += 1
    while track_right < len(R):
        a_list[sorted_thru] = R[track_right]
        track_right += 1
        sorted_thru += 1
    return a_list

def activitySelector(all_activities):
    merge_sort(1, all_activities)
    n = len(all_activities)
    opt = []
    opt.append(all_activities[-1])
    k = 1
    for m in range(2, n+1):
        if all_activities[-m][2] <= all_activities[-k][1]:
            opt.append(all_activities[-m])
            k = m
    merge_sort(0, opt)
    opt_ids = [x[0] for x in opt]
    return opt_ids


sys.stdin = open('act.txt', 'r')
testcases = int(input())
all_data = []

for case in range(1, testcases+1):
    # let x be number of activities
    x = int(input())
    all_activities = []
    for i in range(x):
        # get item info
        activity = input()
        activity = activity.split()
        order = int(activity[0])
        start = int(activity[1])
        finish = int(activity[2])
        # recombine
        activity_info = [order, start, finish]
        all_activities.append(activity_info)
    opt_activities = activitySelector(all_activities)
    all_data.append(opt_activities)

for case_number in range(len(all_data)):
    print("Test case: " + str(case_number+1))
    print("Number of Activities = " + str((len(all_data[case_number]))))
    print("Activities: " + str(all_data[case_number]))

# write to file
dataOut = open('test_results.txt', 'w')
for case_number in range(len(all_data)):
    dataOut.write("Test Case ")
    dataOut.write(str(case_number+1))
    dataOut.write("\n")
    dataOut.write("Number of Activities = ")
    dataOut.write(str(len(all_data[case_number])))
    dataOut.write("\n")
    dataOut.write("Activities:")
    dataOut.write("\n")
    for j in all_data[case_number]:
        dataOut.write(str(j))
        dataOut.write(" ")
    dataOut.write("\n")
dataOut.close()