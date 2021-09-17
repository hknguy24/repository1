#Huy Kevin Nguyen
#PSID: 1346435


# 3.19

# part 1

height1 = int(input("Enter wall height (feet):"))
width1 = int(input("Enter wall width (feet):"))
area1 = int(height1 * width1)
print("Wall area:", area1, "square feet")

# part 2
# 1 gallon paint = 350 sq ft

one_gal_bucket_coverage = 350
num_buckets_needed = area1 / one_gal_bucket_coverage
print("Paint needed:", '{:.2f}'.format(num_buckets_needed), "gallons")

# part 3

num_cans_needed = round(num_buckets_needed)
print("Cans needed:", num_cans_needed, "can(s)")
