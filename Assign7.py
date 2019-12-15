#Bubble sort O(n^2)
def bubble_sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if(lst[j]>lst[j+1]):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

#InsertionSort O(n^2)
def insertionSort(lst):
    for i in range(1, len(lst)):
        #Get element to compare
        curr = lst[i]

        #Compare curr with currently sorted
        while (i>0 and lst[i-1] > curr):
            lst[i] = lst[i-1]
            i -= 1
            lst[i] = curr


#Merge sorting O(nlogn)
def mergeSort(lst):
    if(len(lst) > 1):
        lstLeft = [len(lst)/2]
        lstRight = [len(lst)-len(lstLeft)]

        for i in range(len(lstLeft)):
            lstLeft[i] = lst[i]

        for i in range(len(lstRight)):
            lstRight[i] = lst[len(lstLeft)+i]

        mergeSort(lstLeft)
        mergeSort(lstRight)

        leftPos = 0
        rightPos = 0

        for i in range(len(lst)):
            if(rightPos >= len(lstRight)):
                lst[i] = lstLeft[leftPos]
                leftPos += 1
            elif(leftPos >= len(lstRight)):
                lst[i] = lstRight[rightPos]
                rightPos += 1
            elif(lstLeft[leftPos] >= lstRight[rightPos]):
                lst[i] = lstLeft[leftPos]
                leftPos += 1
            else:
                lst[i] = lstRight[rightPos]
                rightPos += 1


#main
def main():
    ###BUBBLE SORT###
    lst = [10,9,8,7,6,5]
    print(lst)
    bubble_sort(lst)
    print(lst)

    ###INSERTION SORT###
    lst = [10,9,8,14,6,5,4,12,3]
    print(lst)
    insertionSort(lst)
    print(lst)

    ###MERGE SORTING###
    lst = [10,9,8,7,14,5,4,12,3]
    print(lst)
    insertionSort(lst)
    print(lst)
    

main()
