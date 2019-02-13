class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("New sequence created!")

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases


# Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# Access the attribute strbases for printing the sequence
str1 = s1.strbases
str2 = s2.strbases

print("Sequence 1: {}".format(str1))
print("Sequence 2: {}".format(str2))
print("Testing the sequence objects")
