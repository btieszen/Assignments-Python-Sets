#Set Operations in Data Analysis
#Task 1: Duplicate Entries Cleanup 
#Write a Python script to remove duplicates and display the unique customer IDs.



customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
customer=set(customer_ids)
print(customer)