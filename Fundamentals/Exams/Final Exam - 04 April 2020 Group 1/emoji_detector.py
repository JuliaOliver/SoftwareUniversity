import re
text = input()
cool_threshold = 1
cool_emojis = []

for ch in text:
    if ch.isdigit():
        cool_threshold *= int(ch)

pattern = r"(::|\*{2})([A-Z][a-z]{2,})(\1)"

matches = re.findall(pattern, text)

for mat in matches:
    match = mat[1]
    emoji_threshold = 0
    for ch in match:
        num = ord(ch)
        emoji_threshold += num
    if emoji_threshold >= cool_threshold:
        cool_emojis.append(mat[0] + mat[1] + mat[2])

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(f"{emoji}")
