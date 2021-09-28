function problem1(arr, desiredSum)  {
  const visitedSet = new Set();
  for (let i = 0; i < arr.length; ++i) {
    if (visitedSet.has(arr[i])) {
      return true;
    }
    visitedSet.add(desiredSum - arr[i]);
  }
  return false;
}

module.exports = { problem1 };