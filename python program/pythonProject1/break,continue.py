# for i in range(10):
#     print(i)
#     if i==5:
#         break
# l=[11,'xzy','abc',33,5.5,'hello','pqr',33,44,55,66]
# for i in l:
#     print(i)
#     if i=='hello':
#         break
for i in range(10):

    if i % 2 == 0:
        continue         # skip value which is represented after condition
    print(i)                  # without continue statement compiler check condition and give output