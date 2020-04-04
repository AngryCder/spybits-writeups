first get the ciphertext for 2 then 3 call then c2 and c3.

c=m^{e} mod {n}
c =m^{e} - kn
kn =m^{e} - c

calculate  vn = 2^{e} - c2 and un = 3^{e} - c3

then n = gcd(un,vn)

to get the flag you have to return an c1 != c .you have to return c1 = c + kn

