text = input("text: ")
sorted_text = ' '.join(''.join(sorted(i)) for i  in text.split())

print("Sorted letters:", sorted_text)
