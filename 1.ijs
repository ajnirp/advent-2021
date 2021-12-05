data =: 1!:1 <'1.txt'
lines =: cutopen toJ data
n =: > 0 ". each lines
ans1 =: +/ >&0 }. n - _1 |. n
ans2 =: +/ >&0 (3 }. n - _3 |. n)