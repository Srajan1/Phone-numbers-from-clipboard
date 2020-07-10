import pyperclip
import re 
text = str(pyperclip.paste())
phoneREgEx = re.compile(r'''(\d\d\s)?(\d{10})''')
mobile = []
tpl = phoneREgEx.findall(text)
mobile = []
for nums in tpl:
    num = str(nums[0]) + str(nums[1])
    mobile.append(num)
ans = ' '.join(mobile)
print(ans)
pyperclip.copy(ans)