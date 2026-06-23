import os

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return # Skip binary files

    new_content = content
    # Safe replacements for mythril -> aegisevm
    replacements = {
        'import aegisevm': 'import aegisevm',
        'from aegisevm': 'from aegisevm',
        'aegisevm.': 'aegisevm.',
        '"aegisevm"': '"aegisevm"',
        "'aegisevm'": "'aegisevm'",
        'aegisevm/': 'aegisevm/',
        'aegis analyze': 'aegis analyze',
        'bin/aegis': 'bin/aegis',
        'entry_points={"console_scripts": ["aegis=aegisevm.interfaces.cli:main"]}': 'entry_points={"console_scripts": ["aegis=aegisevm.interfaces.cli:main"]}'
    }

    for old, new in replacements.items():
        new_content = new_content.replace(old, new)

    # Special handling for setup.py
    if os.path.basename(filepath) == 'setup.py':
        new_content = new_content.replace("name='aegisevm'", "name='aegisevm'")
        new_content = new_content.replace("packages=find_packages(exclude=['tests'])", "packages=find_packages(exclude=['tests'])")
        new_content = new_content.replace("myth=", "aegis=")

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

def main():
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'node_modules' in root or '.github' in root:
            continue
        for file in files:
            if file.endswith('.py') or file.endswith('.md') or file.endswith('.yml') or file.endswith('.toml') or file.endswith('.txt') or file == 'setup.py':
                replace_in_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
