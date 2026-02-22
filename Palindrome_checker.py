def palindrome(text):
    # cleaned_list = ''
    # for i in text:
    #     if not i.isalnum():
    #         continue
    #     else:
    #         cleaned_list.append(i)
    cleaned_list = ''.join(i for i in text if i.isalnum()).lower()
    return cleaned_list[::-1] == cleaned_list


word = input("Enter your Text, which you want to validate for palindrome: ").strip()
result = palindrome(word)
if result:
    print("Your number is a palindrome.")
else:
    print("Your number is not a palindrome.")