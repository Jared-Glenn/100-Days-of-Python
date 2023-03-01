from tika import parser


raw = parser.from_file("C:/Users/Jared/Downloads/Taming Survey.pdf")
print(raw['content'])