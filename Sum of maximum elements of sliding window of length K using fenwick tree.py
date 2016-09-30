def left_extents(lst):
  result = []
  stack = [-1]
  for i in range(len(lst)):
    while stack[-1] >= 0 and lst[i] >= lst[stack[-1]]:
      del stack[-1]
    result.append(stack[-1] + 1)
    stack.append(i)
  return result


def right_extents(lst):
  result = []
  stack = [len(lst)]
  for i in range(len(lst) - 1, -1, -1):
    while stack[-1] < len(lst) and lst[i] > lst[stack[-1]]:
      del stack[-1]
    result.append(stack[-1])
    stack.append(i)
  result.reverse()
  return result


def sliding_window_totals(lst):
  delta_constant = [0] * (len(lst) + 2)
  delta_linear = [0] * (len(lst) + 2)
  for l, i, r in zip(left_extents(lst), range(len(lst)), right_extents(lst)):
    a = i - l
    b = r - (i + 1)
    if a > b:
      a, b = b, a
    delta_linear[1] += lst[i]
    delta_linear[a + 1] -= lst[i]
    delta_constant[a + 1] += lst[i] * (a + 1)
    delta_constant[b + 2] += lst[i] * (b + 1)
    delta_linear[b + 2] -= lst[i]
    delta_linear[a + b + 2] += lst[i]
    delta_constant[a + b + 2] -= lst[i] * (a + 1)
    delta_constant[a + b + 2] -= lst[i] * (b + 1)
  result = []
  constant = 0
  linear = 0
  for j in range(1, len(lst) + 1):
    constant += delta_constant[j]
    linear += delta_linear[j]
    result.append(constant + linear * j)
  return result

print(sliding_window_totals([30,30,72,72]))
