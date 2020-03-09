
N = input()
A = list( map(int, input().split()) )

prev_id_A = id(A)
heapsort(A)
assert prev_id_A == id(A), "Your heapsort does not operate in-place!"
