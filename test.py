s = 'aba'*2
i, start, end, length = 1, 0, 1, len(s)
while i < length:
    if s[i] != s[start]:
        end = i + 1
        i += 1
    else:
        tmp = i + end - start
        if tmp <= length:
            if s[start:end] == s[i:tmp]:
                i = tmp
                continue
            else:
                end = tmp
                i = end
        else:
            end = length
            break

if end - start < length:
    print(''.join(s[start:end]))
else:
    print(s)
