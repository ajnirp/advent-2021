data =: 1!:1 <'2.txt'
lines =: > 	cutopen toJ data

NB. Fetch only lines from y starting with character x
startswith =: dyad define
i =. =&x @ {."1 y
lines =. i # y
)

NB. obtain the moves. Relies on each move being a single digit
moves =: dyad define
trim =. x {."1 y
moves =. > ". each {. |. |: trim
)

f =: +/ 9 moves 'f' startswith lines
u =: +/ 4 moves 'u' startswith lines
d =: +/ 6 moves 'd' startswith lines

ans1 =: f * (d - u)

NB. TODO: second part