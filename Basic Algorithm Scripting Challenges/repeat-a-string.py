#Repeat a given string (first argument) num times (second argument). Return an empty string if num is not a positive number.

def repeat_string_num_times(str, num):
    if num >= 0:
        return str * num
    else:
        return ' '


print(repeat_string_num_times("*", 3))
print(repeat_string_num_times("abc", 3))
print(repeat_string_num_times("abc", 4))
print(repeat_string_num_times("abc", 1))
print(repeat_string_num_times("*", 8))
print(repeat_string_num_times("abc", -2))
