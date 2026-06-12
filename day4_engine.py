from pypdf import PdfReader

# 1. Open the local file stream reader object
reader = PdfReader("document.pdf")
all_text = ""

# 2. Iterate through every page layout layer and strip textual text info
for page in reader.pages:
    text = page.extract_text()
    if text:
        all_text += text + "\n"

# 3. Slice the aggregate string into uniform chunks of 400 characters each
chunk_size = 400
chunks = [all_text[i:i+chunk_size] for i in range(0, len(all_text), chunk_size)]

# 4. Print layout diagnostic reports to the terminal screen
print("PDF asset loaded successfully!")
print(f"Sliced the target document text into {len(chunks)} individual blocks.")
print("Technical preview of Chunk Index Position 0:")
print("--------------------------------------------------")
print(chunks[0])
print("--------------------------------------------------")
