# Bundles index.html + style.css + app.js into one page for claude.ai publishing.
# Usage: python3 build/make_artifact.py OUTPUT.html
import re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
h = open(os.path.join(ROOT, 'index.html')).read()
css = open(os.path.join(ROOT, 'style.css')).read()
js = open(os.path.join(ROOT, 'app.js')).read()
head_end = h.index('</head><body>')
head = h[:head_end]
title = re.search(r'<title>.*?</title>', head).group(0)
keep = '\n'.join(re.findall(r'<meta name="(?:description|theme-color)"[^>]*>|<link rel="preconnect"[^>]*>|<link href="https://fonts[^>]*>', head))
body = h[head_end + len('</head><body>'):h.rindex('</body>')]
body = body.replace('<script src="app.js"></script>', '<script>\n' + js + '\n</script>')
open(sys.argv[1], 'w').write(title + '\n' + keep + '\n<style>\n' + css + '\n</style>\n' + body)
print('wrote', sys.argv[1])
