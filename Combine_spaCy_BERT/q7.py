abbrivations_map = {"ml":"machine learning","ds":"data structures"}
skills = ["ml","ds","python"]
resolved = [abbrivations_map.get(s , s)
for s in skills]

print(resolved)
