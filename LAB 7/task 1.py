words = ["football", "volleyball", "", "basketball"]
total_num = 0

for word in words:
    total_num += len(word)

print(words)
print(f"Сумма всех длин строк: {total_num}")