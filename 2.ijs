data =: 1!:1 <'2.txt'
lines =: > cutopen toJ data

NB. Fetch lines from y that start with character x.
startswith =: dyad define
i =. =&x @ {."1 y
lines =. ~."1 i # y NB. Nub removes trailing spaces in this case.
)

NB. Net result of the moves for a direction 'f' 'd' or 'u'.
NB. Relies on each move value being a single digit.
net_change =: monad : '+/ "."0 {:"1 y startswith lines' "0

changes =: net_change 'fdu' NB. 3-array
ans1 =: ({. * -/@}.) changes

NB. TODO: second part