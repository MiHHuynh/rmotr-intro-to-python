# Append X

# Write a function append_x that receives a string and appends the character 'X' to it ONLY if the string is not empty:

# append_x('hello')  # hellox
# append_x('')  # ''


def append_x(a_string):
    if (a_string):
        return a_string + 'x'
    else:
        return ''