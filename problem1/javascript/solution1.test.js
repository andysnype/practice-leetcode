const { describe, expect, it } = require('@jest/globals');
const { problem1} = require('./solution1');

let arr = [], k = 0;

describe("Problem 1", () => {
  it('Empty array should be false', () => {
    arr = [];
    k = 15;
    expect(problem1(arr, k)).toBeFalsy();
  });

  it('Sample problem should be true', () => {
    arr = [10, 15, 3, 7];
    k = 17;
    expect(problem1(arr, k)).toBeTruthy();
  });

  it('Negative inputs should work', () => {
    arr = [41, 15, 245242, -24]
    k = 17;
    expect(problem1(arr, k)).toBeTruthy();
  });
});