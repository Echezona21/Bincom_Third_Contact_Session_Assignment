#Open and read the HTML file
file = open("baby2008.html", "r")
values = file.read()
file.close()
#Extraction using regex
import re
pattern = r'<td>\d+</td><td>([A-Za-z]+)</td><td>([A-Za-z]+)</td>'
matches = re.findall(pattern, values)
print("Extracted Names: ", matches[:5])
names = []
for boy, girl in matches:
    names.append(boy)
    names.append(girl)
print(names[:5])

#Sort the names in alphabetical order
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_names = bubble_sort(names)
print("Sorted Names: ", sorted_names[:20])
