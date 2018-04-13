# creates an xml file for upload to cisco call managor using a csv file as input

filename = input("Enter input filename: ")

entries = []
with open(filename, 'r') as infile:
  entries = (infile.readlines())
print(entries)
outfile = input("Enter output filename (example.xml): ")
with open(outfile, 'w') as ofile:
  ofile.write("<CiscoIPPhoneDirectory>\n")
  for entry in entries:
    name, number = entry.split(',')
    print(name, number)
    ofile.write("<DirectoryEntry>\n")
    ofile.write("<Name>\"{0}\"</Name>\n".format(name.strip()))
    ofile.write("<Telephone>\"{0}\"</Telephone>\n".format(number.strip()))
    ofile.write("</DirectoryEntry>\n")
  ofile.write("</CiscoIPPhoneDirectory>\n")
