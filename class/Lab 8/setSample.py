>>> set1=set()
>>> set1
set()
>>> set1.add(1)
>>> set1
{1}
>>> set1.add(2)
>>> set1
{1, 2}
>>> set2={2,3,4,5}
>>> set2
{2, 3, 4, 5}
>>> set1.difference(set2)
{1}
>>> set2.difference(set1)
{3, 4, 5}
>>> set1.union(set2)
{1, 2, 3, 4, 5}
>>> set1.isdisjoint(set2)
False
>>> set3={2,3}
>>> set3.issubset(set2)
True
>>> set3.issuperset(set2)
False