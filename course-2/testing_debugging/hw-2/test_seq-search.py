import pytest, seq_search

# pytest way to list used parameters to test function
@pytest.mark.parametrize('key, array, expected', [
    (3, ["B", "D", "B", "A"], "A"),
    (1, ["B", "D", "B", "A"], "D"),
    (7, ["B", "D", "B", "A"], False),
    (0, ["B"], "B"),
    (2, [2.5, "gbhg", 47], 47),
    (4, [8, 7, 9, 8, 10, 9, 7], 10),
    (0, [], False),
    (-1, ["A", "B", "C"], False),
])

def test_seq_search(key, array, expected): # test function
    result = seq_search.seq_search(key, array)
    assert result == expected # match against expected

observations = [1, 2, 3, 4]
frequencies = [7, 4, 11, 9]

count = 0
i = 0
while i < len(frequencies):
    count += frequencies[i]
    i += 1

rel_freqs = [0] * len(frequencies)
for (i, f) in enumerate(frequencies):
        val = f // count
        rel_freqs[i] = val

for (o, r) in zip(observations, rel_freqs):
    print(f'{o} : {r}')