import os, re

rs = os.popen("./iat_sample")
text = rs.read()
pattern = re.compile(r"=============================================================(.+)=============================================================")
match_text = pattern.findall(text)
print(match_text)