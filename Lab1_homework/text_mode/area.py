# คํานวณพื้นที่ของที่ดินรูปสี่เหลี่ยม จากความกว้างและความยาว (หน่วยเป็นเมตร)
# แสดงพื้นที่ในหน่วยตารางเมตร และตารางวา

#Acquire user input for width and length
width = float(input("Width (m): "))
length = float(input("Length (m): "))

sqr_m = width * length # Calculate area in square meters
sqr_wah = sqr_m / 4 # Convert square meters to square wah

print("Area =", sqr_m, "square metres") # Display area in square meters
print("Area =", sqr_wah, "square wah") # Display area in square wah