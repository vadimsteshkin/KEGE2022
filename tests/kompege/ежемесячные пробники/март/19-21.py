from functools import *
def m(h):
    return h+1,h+2,h*2
@lru_cache
def g(h):
    if h>21:return 'w'
    if any(g(i)=='w' for i in m(h)):return 'p1'
    if all(g(i)=='p1' for i in m(h)):return'v1'
    if any(g(i)=='v1' for i in m(h)):return 'p2'
    if all(g(i)=='p1' or g(i)=='p2' for i in m(h)):return 'v2'
    if any(g(i)=='v2' for i in m(h)):return 'p3'
    if all(g(i)=='p1' or g(i)=='p2' or g(i)=='p3' for i in m(h)):return 'v3'
    if any(g(i)=='v3' for i in m(h)):return 'p4'
    if all(g(i)=='p1' or g(i)=='p2'or g(i)=='p3'or g(i)=='p4' for i in m(h)):return 'v4'
    if any(g(i)=='v4' for i in m(h)):return 'p5'
    if all(g(i)=='p1' or g(i)=='p2'or g(i)=='p3'or g(i)=='p4'or g(i)=='p5' for i in m(h)):return 'v5'
for i in range(1,22):
    print(i,g(i))