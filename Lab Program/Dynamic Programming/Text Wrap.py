import textwrap 
value = """I AM A CSE STUDENT LOVE CODING"""
wrapper = textwrap.TextWrapper(width=10) 
word_list = wrapper.wrap(text=value) 
for element in word_list: 
	print(element)
