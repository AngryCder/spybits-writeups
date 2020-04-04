first get the ciphertext for 2 then 3 call then c2 and c3.

{\displaystyle c=m^{e}\mod {n}}
{\displaystyle c =m^{e} - kn}
{\displaystyle kn =m^{e} - c}

calculate {\displaystyle vn = 2^{e} - c2} and {\displaystyle un = 3^{e} - c3}

then n {\displaystyle \n = gcd(un,vn)} 

to get the flag you have to return an c1 != c .you have to return c1 = c + kn

