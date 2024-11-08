to_visit = ["nashville", "myrtle beach", "san diego", "atlanta", "boston"]

print("Here is the origional list: ")
print(to_visit)

print("\nHere is the sorted list: ")
print(sorted(to_visit))

print("\nHere is the origional list again: ")
print(to_visit)

print("\nHere is the reverse sorted list: ")
print(sorted(to_visit, reverse=True))

print("\nHere is the origional list again: ")
print(to_visit)

print("\nHere is the reversed list: ")
to_visit.reverse()
print(to_visit)

print("\nHere is the reversed list again: ")
to_visit.reverse()
print(to_visit)

print("\nHere is the list with sort: ")
to_visit.sort()
print(to_visit)

print("\nHere is the list with reverse sort: ")
to_visit.sort(reverse=True)
print(to_visit)