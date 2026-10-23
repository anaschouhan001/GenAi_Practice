text = """"
Our Data Analyst course lasts for 6 months.
Student get access to all recorded classes.
Live classes hapen form Monady to Friday.
Refund requests are accepted within 7 days of placement support starts.
Student must complete all assigment before placement support starts.
Eligible student receive minimum 3 interview opportunities.
""" 
lines = text.strip().split("\n") 
chunks = []

for i in range(0, len(lines), 2):
    chunk = " ".join(lines[i:i+2])
    chunks.append(chunk)
    
    
    for chunk in chunks:
        print("CHUNK:")
        print(chunk)
        print()