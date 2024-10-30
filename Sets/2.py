# s1={1,2,5,6};
# s2={3,6,7};
# print(s1.union(s2));

# s1.update(s2);
# print(s1,s2);




cities={"Tokyo", "Madrid", "Berlin", "Delhi"};
cities2={"Tokyo", "Seoul", "Kabul","Madrid"};

cities3=cities.intersection(cities2);
cities4=cities.symmetric_difference(cities2);
# cities5=cities.remove("Tokyo2");
# cities6=cities.discard("Tokyo2")




# print(cities3);
# print(cities4);
# print(cities.isdisjoint(cities2));

# print(cities5);
# print(cities6);
# print(cities.pop());

# del cities; #delete the entire set
cities.clear(); # delete the all items in the set
print(cities);