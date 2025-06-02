#!/usr/bin/env python3
import re

def fix_deferred_loading():
    # Read the HTML file
    with open('index.html', 'r') as f:
        content = f.read()
    
    # Remove the deferred loading JavaScript section that's causing issues
    pattern = r'\(function\(\) \{var items = \$\$\(\'\.deferred\'\).*?\}\)\(\);'
    content = re.sub(pattern, '// Deferred loading removed for GitHub Pages compatibility', content, flags=re.DOTALL)
    
    # Write the fixed content back
    with open('index.html', 'w') as f:
        f.write(content)
    
    print("✅ Deferred loading JavaScript removed successfully")
    print("🔧 This should fix the 'undefined' src attribute issue")

if __name__ == "__main__":
    fix_deferred_loading() 