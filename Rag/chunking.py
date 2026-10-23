text = """"
Our Data Analyst course lasts for 6 months.
Student get access to all recorded classes.
Live classes hapen form Monady to Friday.
Refund requests are accepted within 7 days of placement support starts.
Student must complete all assigment before placement support starts.
Eligible student receive minimum 3 interview opportunities.
""" 
chunks = text.strip().split("\n") 
print(chunks)
for chunk in chunks:
    print("CHUNK:")
    print(chunk)
    print()