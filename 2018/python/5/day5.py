with open('input.txt', 'r') as f:
    slurp = f.read()

polymer = slurp.strip()

lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = lowers.upper()

def reduce_polymer(poly):

    xlate = {k: v for k, v in zip(lowers, uppers)}
    xlate.update({k: v for k, v in zip(uppers, lowers)})
    length = len(poly)
    result = ''
    i = 0
    while i < length:
        if i < length - 1 and xlate[poly[i]] == poly[i+1]:
            i += 2
        else:
            result = result + poly[i]
            i += 1

    return result


def fully_reduce(poly):
    reduced_length = 0
    p = poly

    while len(p) != reduced_length:
        reduced_length = len(p)
        p = reduce_polymer(p)

    return p


reduced1 = fully_reduce(polymer)
answer1 = len(reduced1)
print(answer1)


units = zip(lowers, uppers)
final_poly = reduced1
max_reduction = len(final_poly)

for (l, u) in units:
    tmp_poly = fully_reduce(reduced1.replace(l, '').replace(u, ''))
    if len(tmp_poly) < max_reduction:
        max_reduction = len(tmp_poly)
        final_poly = tmp_poly

print(max_reduction)



