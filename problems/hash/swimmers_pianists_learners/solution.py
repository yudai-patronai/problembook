speakers = set(map(int, input().split()))
pianists = set(map(int, input().split()))
swimmers = set(map(int, input().split()))

ids_request = (swimmers & pianists) - speakers
print(*sorted(ids_request))
