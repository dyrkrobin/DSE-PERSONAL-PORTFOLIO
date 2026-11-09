
rows=6
chairs_per_row=8
total_chairs=rows*chairs_per_row

print("total chairs:", total_chairs)
print("111111")
print("classroom layout")
print("each $ represent one chair.\n")
for i in range(rows):
    print("row", i+1, ":", " ".join(["$"] * chairs_per_row))

print("\nNumber of rows:", rows)
print("chairs per row:", chairs_per_row)
print(" Total chairs:", total_chairs)
 
 