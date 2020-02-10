Months = set(["January","February", "March", "April", "May", "June"])

print("printing the original set ... ")
print(Months)

print("Removing some months from the set...");

Months.discard("January");
Months.discard("aaa");

print("Printing the modified set...");
print(Months)

print("looping through the set elements ... ")
for i in Months:
    print(i)