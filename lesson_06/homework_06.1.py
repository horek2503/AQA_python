source_string = input("Please enter  your message:")
print(f"10+ unique symbols check result: {True if len(set(source_string)) > 10 else False}")