

def search_anagram(array):
    sorted_array = [sorted(word) for word in array]
    sorted_array.sort()

    for i in range(len(sorted_array) - 1):
        if sorted_array[i] == sorted_array[i+1]:
            return True
    return False







    

        

    ...

if __name__ == "__main__":

    data = ['stamp', 'state', 'pasta', 'paste', 'taste']
    result = search_anagram(data)
    print(result)
