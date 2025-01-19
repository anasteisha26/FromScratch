# Euclidian dictance between 2 points in any space

def euc_d(vec1, vec2):

  if len(vec1) == len(vec2):
    sum = 0
    for i in range(0, len(vec1)):
      i_order = (vec1[i] - vec2[i])*(vec1[i] - vec2[i])
      sum += i_order
    result = math.sqrt(sum)   

  else:
    print("An error occured")

  return result

def generate_centroid_coordinates():
  arr = []

  for i in range(0, len(list_highest)):
    arr.append(random.uniform(list_lowest[i]-3, list_highest[i]+3))
  arr = np.array(arr)
  return arr
