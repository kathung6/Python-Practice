# This python program finds pythragorean triples up to 20

#create lists for each side of a triangle
a = list(range(1,21))
b = list(range(1,21))
c = list(range(1,21))

#create a set so as to remove any duplicates
pythagorean_triples = set()

#triple nested for loops calculates all possible combinations
for i in a:
    for j in b:
        for k in c:
            if (i * i) + (j * j) == (k * k):
                #adds the pythagorean triple to the set and sorts the ints
                pythagorean_triples.add(tuple(sorted([i, j, k])))
            else:
                continue
#sorts the set in ascending order

sorted_pythagorean_triples = sorted(pythagorean_triples)

#prints the set with a space instead of comma
for triple in sorted_pythagorean_triples:
    print(*triple, sep = ' ')