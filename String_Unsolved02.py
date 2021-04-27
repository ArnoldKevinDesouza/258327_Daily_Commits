st = input("Enter String:")
  
# index to remove character at
index=int(input("Index u want to remove:"))
  
# extracts 0 to n-1th index
first_part = st[0:index]
  
# extracts characters from n+1th index until the end
second_part = st[index+1:]
print("Modified string after removing ", index, "th character ")
  
# combining both the parts together
print(first_part+second_part)