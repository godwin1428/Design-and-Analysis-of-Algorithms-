def brute_force(text, pattern):
  n = len(text)
  m = len(pattern)
  for i in range(n - m + 1):
    j = 0
    while j < m and text[i + j] == pattern[j]:
      j += 1
    if j == m:
      return i
  return -1
text = "abracadabra"
pattern = "abra"
index = brute_force(text, pattern)
if index != -1:
  print("The pattern was found at index",index)
else:
  print("The pattern was not found.")
