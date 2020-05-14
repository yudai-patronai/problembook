a = input()
a = [int(el) for el in a.split()]

st = []
for n in a:
    if n == 0:
        break
    if n > 0:
        st.append(n)
    else:
        if st:
            if -n >= st[-1]:
                st.pop()
            else:
                st[-1] += n

print(str(len(st)) + ' ' + str(st[-1] if st else -1))
