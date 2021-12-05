data =: 1!:1 <'1.txt'
lines =: cutopen toJ data
nums =: > 0 ". each lines
ans1 =: +/ >&0 }. nums - _1 |. nums
ans2 =: +/ >&0 (3 }. nums - _3 |. nums)