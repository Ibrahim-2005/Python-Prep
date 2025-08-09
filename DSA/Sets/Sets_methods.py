"""
add()	 	            Adds an element to the set
clear()	 	            Removes all the elements from the set
copy()	 	            Returns a copy of the set
difference()"-"	        Returns a set containing the difference between two or more sets
difference_update()"-="	Removes the items in this set that are also included in another, specified set
discard()	 	        Remove the specified item
intersection()"&"	    Returns a set, that is the intersection of two other sets
intersection_update()"&=" Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	    Returns whether two sets have a intersection or not
issubset()"<="	        Returns True if all items of this set is present in another set
 	       "<"	        Returns True if all items of this set is present in another, larger set
issuperset()">="        Returns True if all items of another set is present in this set
 	       ">"	        Returns True if all items of another, smaller set is present in this set
pop()	 	            Removes an element from the set
remove()	 	        Removes the specified element
symmetric_difference()"^"   Returns a set with the symmetric differences of two sets
symmetric_difference_update()"^="	Inserts the symmetric differences from this set and another
union()	"|"	            Return a set containing the union of sets
update()"|="        	Update the set with the union of this set and others

"""


# Initial sets
set1 = {"Apple", "Orange", "Banana", "Grapes", "Apple"}
set2 = {"Banana", "Papaya", "Watermelon", "Orange"}

print("Original set1:", set1)
print("Original set2:", set2)

# 1. add()
set1.add("Kiwi")
print("After add():", set1)

# 2. clear()
temp_set = set1.copy()
temp_set.clear()
print("After clear():", temp_set)

# 3. copy()
copy_set = set1.copy()
print("After copy():", copy_set)

# 4. difference()
diff_set = set1.difference(set2)
print("After difference():", diff_set)

# 5. difference_update()
set1_diff = set1.copy()
set1_diff.difference_update(set2)
print("After difference_update():", set1_diff)

# 6. discard()
set1_discard = set1.copy()
set1_discard.discard("Banana")
print("After discard():", set1_discard)

# 7. intersection()
intersect = set1.intersection(set2)
print("After intersection():", intersect)

# 8. intersection_update()
set1_inter = set1.copy()
set1_inter.intersection_update(set2)
print("After intersection_update():", set1_inter)

# 9. isdisjoint()
is_disjoint = set1.isdisjoint(set2)
print("After isdisjoint():", is_disjoint)

# 10. issubset()
subset1 = {"Banana", "Apple"}
print("issubset():", subset1.issubset(set1))

# 11. "<" (strict subset)
print("subset1 < set1:", subset1 < set1)

# 12. issuperset()
print("issuperset():", set1.issuperset(subset1))

# 13. ">" (strict superset)
print("set1 > subset1:", set1 > subset1)

# 14. pop()
set1_pop = set1.copy()
popped = set1_pop.pop()
print("After pop():", popped, "| Remaining:", set1_pop)

# 15. remove()
set1_remove = set1.copy()
set1_remove.remove("Banana")
print("After remove():", set1_remove)

# 16. symmetric_difference()
sym_diff = set1.symmetric_difference(set2)
print("After symmetric_difference():", sym_diff)

# 17. symmetric_difference_update()
set1_sym = set1.copy()
set1_sym.symmetric_difference_update(set2)
print("After symmetric_difference_update():", set1_sym)

# 18. union()
union_set = set1.union(set2)
print("After union():", union_set)

# 19. update()
set1_update = set1.copy()
set1_update.update(set2)
print("After update():", set1_update)
