# Create a small command-line program in Python to Calculate the total invoice amount for the below purchases - 
# Book - Introduction to Python Programming: Rs 499.00
# Book - Python Libraries Cookbook: Rs. 855.00
# Book - Data Science in Python: Rs. 645.00
# - Taxes and additional charges are described as details - 
# GST: 12%
# Delivery Charges: Rs. 250.00

print("-----------------------------------------------------")
print("Your Invoice Details are Below...")
book1 = 499.00
book2 = 855.00
book3 = 645.00
gst = 0.12 
deliveryCharge = 250.00

subtotal = book1+book2+book3
tax = subtotal * gst
total = subtotal + tax + deliveryCharge

print("-----------------------------------------------------")
print("Introduction to Python Programming: Rs.",book1)
print("Python Libraries Cookbook: Rs.",book2)
print("Data Science in Python: Rs.",book3)
#print("Delivery Charges are: ",deliveryCharge, " And GST applied",gst, "%")
print("-----------------------------------------------------")

print("Subtotal is: ", subtotal)
print("Additional tax: ", tax)
print("Delivery charges applied: ", deliveryCharge)

print("-----------------------------------------------------")
print("Total Amount: ", total)
print("-----------------------------------------------------")
print("Thank You. Visit again...")