def solution(phone_book):
    phone_dict = {}
    for phone_number in phone_book:
        phone_dict[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for n in phone_number:
            temp += n
            if phone_dict.get(temp, 0) and temp != phone_number:
                return False
    return True