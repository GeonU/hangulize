# -*- coding: utf-8 -*-
from .. import *


class Polish(Language):
    """For transcribing Polish."""

    vowels = 'a', 'e', 'i', 'o', 'u', 'y'
    notation = Notation(
        (u'ą{lł}',      'o'),
        (u'ą',          'oN'),
        (u'ę{lł}',      'e'),
        (u'ę$',         'e'),
        (u'ę',          'eN'),
        (u'ół',         'u'),
        (u'łł',         u'ł'),
        (u'ł{@}',       'W'),
        (u'ł',          'Xu'),
        (u'ó',          'u'),
        ('rz',          u'ż'),
        (u'dź',         u'ć'),
        (u'ć',          'cj'),
        ('hh',          'h'),
        ('ch',          'h'),
        (u'ź{cfhkpst}', 'sj'),
        (u'ź$',         'sj'),
        (u'ź',          'zj'),
        (u'ś',          'sj'),
        ('dz{cfhkpst}', 'c'),
        ('dz$',         'c'),
        ('dz',          'z'),
        (u'dż{@}',      'z'),
        (u'dż',         'C'),
        ('cz',          'C'),
        ('cj',          'C'),
        (u'C$',         'ci'),
        ('C{@}',        'c'),
        ('C',           'ci'),
        ('b{cfhkpst}',  'p'),
        ('b$',          'p'),
        ('d{cfhkpst$}', 't'),
        ('d$',          't'),
        ('g{cfhkpst$}', 'k'),
        ('g$',          'k'),
        ('w{cfhkpst$}', 'f'),
        ('w$',          'f'),
        (u'ż{cfhkpst}', 'sz'),
        (u'{cfhkpst}ż', 'sz'),
        (u'ż$',         'sz'),
        (u'ż{@}',       'z'),
        (u'żj',         'zj'),
        (u'ż',          'zu'),
        ('ji{@}',       'ij'),
        ('jy{@}',       'ij'),
        ('sz{@}',       'sJ'),
        ('szj',         'sJ'),
        ('sz$',         'sj'),
        ('sz',          'sJu'),
        ('z{cfhkpst$}', 's'),
        ('z$',          's'),
        ('xx',          'x'),
        ('x',           'ks'),
        ('tt',          't'),
        ('w',           'v'),
        ('q',           'kv'),
        ('aa',          'a'),
        ('bb',          'b'),
        ('dd',          'd'),
        ('ee',          'e'),
        ('ff',          'f'),
        ('jj',          'ij'),
        ('ii',          'i'),
        ('zj{@}',       'z'),
        ('^j{@}',       'J'),
        ('{@}j{@}',     'J'),
        ('j',           'i'),
        ('ij',          'i'),
        ('yj',          'y'),
        ('kk',          'k'),
        ('ll',          'l'),
        ('{@}mm{@}',    (Jongseong(M), Choseong(M))),
        ('mm',          'm'),
        ('{@}nn{@}',    (Jongseong(N), Choseong(N))),
        ('oo',          'o'),
        ('pp',          'p'),
        ('rr',          'r'),
        ('ss',          's'),
        ('tt',          't'),
        ('uu',          'u'),
        ('X',           None),
        ('vv',          'v'),
        ('^y{@}',       'J'),
        ('yy',          'y'),
        ('y',           'i'),
        ('zz',          'z'),
        ('^k',          (Choseong(K),)),
        ('{@}k{pstz}',  (Jongseong(G),)),
        ('^p',          (Choseong(P),)),
        ('{@}p{kstz}',  (Jongseong(B),)),
        ('k',           (Choseong(K),)),
        ('p',           (Choseong(P),)),
        ('b',           (Choseong(B),)),
        ('c',           (Choseong(C),)),
        ('d',           (Choseong(D),)),
        ('f',           (Choseong(P),)),
        ('g',           (Choseong(G),)),
        ('h',           (Choseong(H),)),
        ('^l',          (Choseong(L),)),
        ('l{@}',        (Jongseong(L), Choseong(L))),
        ('l',           (Jongseong(L),)),
        ('^m',          (Choseong(M),)),
        ('m{@}',        (Choseong(M),)),
        ('m',           (Jongseong(M),)),
        ('^n',          (Choseong(N),)),
        ('n{@J}',       (Choseong(N),)),
        ('n',           (Jongseong(N),)),
        ('N',           (Jongseong(NG),)),
        ('r',           (Choseong(L),)),
        ('s',           (Choseong(S),)),
        ('t',           (Choseong(T),)),
        ('v',           (Choseong(B),)),
        ('z',           (Choseong(J),)),
        ('Ja',          (Jungseong(YA),)),
        ('Je',          (Jungseong(YE),)),
        ('Ji',          (Jungseong(I),)),
        ('Jo',          (Jungseong(YO),)),
        ('Ju',          (Jungseong(YU),)),
        ('Wa',          (Choseong(NG), Jungseong(WA),)),
        ('We',          (Choseong(NG), Jungseong(WE),)),
        ('Wi',          (Choseong(NG), Jungseong(WI),)),
        ('Wo',          (Choseong(NG), Jungseong(WEO),)),
        ('Wu',          (Choseong(NG), Jungseong(U),)),
        ('a',           (Jungseong(A),)),
        ('e',           (Jungseong(E),)),
        ('i',           (Jungseong(I),)),
        ('o',           (Jungseong(O),)),
        ('u',           (Jungseong(U),))
    )

    def normalize(self, string):
        def normalize_only_unsafe(string):
            map = {u'Ą': u'ą',
                   u'Ć': u'ć',
                   u'Ę': u'ę',
                   u'Ł': u'ł',
                   u'Ó': u'ó',
                   u'Ś': u'ś',
                   u'Ź': u'ź',
                   u'Ż': u'ż'}
            safe = map.keys() + map.values()
            for c in string:
                if c not in safe:
                    yield normalize_roman(c)
                elif c in map:
                    yield map[c]
                else:
                    yield c
        return ''.join(normalize_only_unsafe(string))


pl = Polish
