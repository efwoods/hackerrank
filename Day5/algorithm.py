# Algorithm
# main list 1 -> 3 -> 7 -> NULL
# compar list 1 -> 2 -> NULL
# if main list == comparison list 
# save the next node of the main list: 3 -> 7 -> NULL
# save the next node of the comparison list: 2 -> NULL
# comparison list node.next = None: 1 -> NULL
# main list node.next = comparison list: 1 -> 1-> Null
# main list node.next.next = saved next node of the main list: 1 -> 1 -> 3 -> 7 -> NULL
# comparison list = saved next node of the comparison list: 2 -> NULL
# compare main list and comparison list (comparison list should be new or none)

# main list: 1 -> 1 -> 3 -> 7 -> NULL
# compare list: 2 -> NULL

# check to see if comparison list.next is null; if yes then set a condition, continue and return the main list at the end; else continue
# if main list < comparison list
# traverse(main list) until main list > comparison list or main list is null
# if main list is null; traverse the main list and return the last node; node.next from this return = compare list
# state: main list is not null & the main list is > comparison list (3); traverse the main list with a stop value until the stop value is reached. this will return the penultimate node ( the second 1->); this is stored as a temp, but references the main list because it is not copied.; return the ulitimate node (3 ->...)
# set the temp main list next = comparison list: 1 -> 1 -> 2 -> NULL
# set the temp main list next.next = ultimate node: 1 -> 1 -> 2 -> 3 -> 7 -> NULL
# if the condition was set, then return the main list. Done.

# Example test case for the ALgorithm
# main list 2 -> 3 -> 7 -> NULL
# compar list 1 -> 2 -> 3-> NULL

# check to see if comparison list.next is null; if yes then set a condition, continue and return the main list; else continue

# if main list == comparison list 
# save the next node of the main list: 3 -> 7 -> NULL
# save the next node of the comparison list: 2 -> NULL
# comparison list node.next = None: 1 -> NULL
# main list node.next = comparison list: 1 -> 1-> Null
# main list node.next.next = saved next node of the main list: 1 -> 1 -> 3 -> 7 -> NULL
# comparison list = saved next node of the comparison list: 2 -> NULL
# compare main list and comparison list (comparison list should be new or none)

# if main list < comparison list
# check to see if comparison list.next is null; if yes then set a condition, continue and return the main list; else continue
# traverse(main list) until main list > comparison list or main list is null
# if main list is null; traverse the main list and return the last node; node.next from this return = compare list
# state: main list is not null & the main list is > comparison list; traverse the main list with a stop value until the stop value is reached. this will return the penultimate node ( the second 1->); this is stored as a temp, but references the main list because it is not copied.; return the ulitimate node (3 ->...)
# set the temp main list next = comparison list: 1 -> 1 -> 2 -> NULL
# set the temp main list next.next = ultimate node: 1 -> 1 -> 2 -> 3 -> 7 -> NULL
# if the condition was set, then return the main list. Done.

# if main list > comparison list
# travserse( comparison list ) until the comparison > main list or the comparison list is null
# if compare list is null; traverse the compare list and return the last node; node.next from this return = main list
# state: comparison list is not null & the comparison list is > main list; traverse the comparison list with a stop value until the stop value is reached. this will return the penultimate node ( the 2->); this is stored as a temp, but references the comparison list because it is not copied.; return the ulitimate node (3 ->...)
# set the temp comparison list next = main list: 1 -> 2 -> 2 -> 3 -> 7 -> Null
# set the temp comparison list next.next = ultimate node: 3 -> NULL
# if the condition was set then return the comparison list

# if the condition was not set then continue the loop 