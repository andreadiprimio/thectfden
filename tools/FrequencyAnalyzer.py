from collections import Counter

def FrequencyAnalyzer(string, fromFile=False):
    if not (isinstance(string, str) and isinstance(fromFile, bool)):
        raise TypeError('Incorrect argument typing.')
    else:
        if fromFile:
            f = open(string, 'r')
            data = f.read()
        else:
            data = string
        res = Counter(data)
        for el in res.keys():
            res[el] = [res[el], res[el]/len(data)]
        print(res)
        return res

s = "AJODajdjaiodjoajcisojasoicjoasjdajoadfaofosiajdasjcpasdpasokdpaoskdpakpkacfkpaokdpaskdpasokdac"
FrequencyAnalyzer(s)
