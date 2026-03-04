# 1
import re

pattern = r"^ab*$"
text = "abbb"

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")



# 2
import re

pattern = r"^ab{2,3}$"
text = "abb"

if re.match(pattern, text):
    print("Match found")




# 3
import re

text = "hello_world test_case example"
pattern = r"\b[a-z]+_[a-z]+\b"

matches = re.findall(pattern, text)
print(matches)



# 4

import re

text = "Hello World Python"
pattern = r"\b[A-Z][a-z]+\b"

matches = re.findall(pattern, text)
print(matches)



# 5
import re

pattern = r"^a.*b$"
text = "axxxb"

if re.match(pattern, text):
    print("Match found")



# 6
import re

text = "Hello, world. How are you"
result = re.sub(r"[ ,\.]", ":", text)

print(result)



# 7
import re

def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)

print(snake_to_camel("hello_world_example"))



# 8
import re

text = "HelloWorldPython"
result = re.findall(r"[A-Z][^A-Z]*", text)

print(result)



# 9
import re

text = "HelloWorldPython"
result = re.sub(r"([A-Z])", r" \1", text).strip()

print(result)


# 10
import re

def camel_to_snake(text):
    return re.sub(r"([A-Z])", r"_\1", text).lower()

print(camel_to_snake("helloWorldExample"))