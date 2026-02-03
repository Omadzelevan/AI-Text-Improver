
print("=== AI Portfolio Text Improver ===")
print()

text = input("Enter your portfolio text:\n> ")

print()
print("Processing with AI styles...")
print()


def professional_style(t):
    return f"""
[Professional Version]
{t}

This project demonstrates strong technical understanding,
problem-solving ability, and practical implementation skills.
"""

def short_style(t):
    words = t.split()
    short = " ".join(words[:12])
    return f"""
[Short Version]
{short}...
"""

def friendly_style(t):
    return f"""
[Friendly Version]
{t}

I enjoy building projects like this and continuously improving my skills.
"""


print(professional_style(text))
print(short_style(text))
print(friendly_style(text))

print()
print("Done! AI text variations generated.")
