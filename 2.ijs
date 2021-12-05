data =: 1!:1 <'2.txt'
lines =: > 	cutopen toJ data

remove_spaces =: #~ ~:&' '

NB. Fetch lines from y that start with character x, and remove all spaces.
startswith =: dyad define
i =. =&x @ {."1 y
lines =. remove_spaces"1 i # y
)

NB. Obtain the net result of the moves for that direction.
NB. Relies on each move being a single digit.
net_change =: monad define
+/ "."0 {:"1 y startswith lines
)

f =: net_change 'f'
u =: net_change 'u'
d =: net_change 'd'

ans1 =: f * (d - u)

NB. TODO: second part