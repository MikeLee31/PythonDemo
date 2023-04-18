def f(x):
    return x * x - x - 1


a = -1
b = 1
e = 0.05
p = 0.312 * (b - a) + a
q = 0.618 * (b - a) + a
k = 1
while 1:
    print("%3d a %5.3f p %5.3f q %5.3f b %5.3f f(p) %5.3f f(q) %5.3f q-a %5.3f b-q %5.3f" % (
    k - 1, a, p, q, b, f(p), f(q), q - a, b - q))
    k = k + 1
    if f(p) <= f(q):
        if q - a < e:
            print("%.3f %.3f" % (p, f(p)))
            break
        else:
            b = q
            q=p
            p=a+0.382*(b-a)
    else:
        if b-p < e:
            print("%.3f %.3f" % (q, f(q)))
            break
        else:
            a=p
            p=q
            q = 0.618 * (b - a)
    if k == 100:
        break
