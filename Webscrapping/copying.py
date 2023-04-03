import csv

# Open the first file in read mode and read its contents into a list
with open('Webscrapping/IFND.csv', 'r', newline='', encoding='ISO-8859-1') as file1:
    file1_reader = csv.reader(file1)
    file1_contents = list(file1_reader)

# Open the second file in read mode
with open('Webscrapping/news_headlines.csv', 'r', newline='', encoding='ISO-8859-1') as file2:
    # Create a CSV reader object for the second file
    file2_reader = csv.reader(file2)
    # Skip the header row in the second file
    next(file2_reader)
    
    # Iterate over each row in the second file
    for row2 in file2_reader:
        # Extract the three columns from row2
        Statement, Web, Label = row2[0], row2[1], row2[2]
        
        # Check if the row already exists in the first file
        if [Statement, Web, Label] in file1_contents:
            continue
        else:
            # Append the three columns to the first file
            file1_contents.append([Statement, Web, Label])

# Open the first file in write mode and write the updated contents to it
with open('Webscrapping/IFND.csv', 'w', newline='', encoding='ISO-8859-1') as file1:
    file1_writer = csv.writer(file1)
    file1_writer.writerows(file1_contents)

print('Contents of file2 have been appended to file1.')






