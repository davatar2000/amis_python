def reverse(s):
    if (len(s) < 2):
        return s
    else:
        mid = len(s)//2
        return (reverse(s[mid:]) + reverse(s[:mid]))
 
