x = input()
parts = x.split('-')

result = 0
for i, part in enumerate(parts):
    part_sum = sum(int(num) for num in part.split('+'))
        
    if i == 0:
        result += part_sum
    else:
        result -= part_sum

print(result)