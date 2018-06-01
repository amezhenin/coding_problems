#!/usr/bin/python
"""
https://www.codechef.com/problems/TOTR

Input:
5 qwertyuiopasdfghjklzxcvbnm
Ph
Pcssi
Bpke_kdc_epclc_jcijsc_mihyo?
Epcf_kdc_liswhyo_EIED_hy_Vimcvpcn_Zkdvp_siyo_viyecle.
Ipp!

Output:
Hi
Hello
What are these people doing?
They are solving TOTR in Codechef March long contest.
Ohh!
"""
import string


def alg(a, l):
    """
    >>> alg("qwertyuiopasdfghjklzxcvbnm", "Ph")
    'Hi'

    >>> alg("qwertyuiopasdfghjklzxcvbnm", "Pcssi")
    'Hello'

    >>> alg("qwertyuiopasdfghjklzxcvbnm", "Bpke_kdc_epclc_jcijsc_mihyo?")
    'What are these people doing?'

    >>> alg("qwertyuiopasdfghjklzxcvbnm", "Epcf_kdc_liswhyo_EIED_hy_Vimcvpcn_Zkdvp_siyo_viyecle.")
    'They are solving TOTR in Codechef March long contest.'

    >>> alg("qwertyuiopasdfghjklzxcvbnm", "Ipp!")
    'Ohh!'
    """
    A = {"_": " ", ".": ".", ",": ",", "!": "!", "?": "?"}
    for a, b in zip(a, string.ascii_lowercase):
        A[b] = a
        A[b.upper()] = a.upper()

    res = []
    for c in l:
        res.append(A[c])

    return "".join(res)


if __name__ == "__main__":
    n, alphabet = raw_input().split()
    for i in range(int(n)):
        line = raw_input()
        print alg(alphabet, line)
