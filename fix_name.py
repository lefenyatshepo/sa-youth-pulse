lines = open('app/main.py', 'r', encoding='utf-8').readlines()
# Fix line 33 - replace corrupted _name_ with correct version
lines[32] = '    ' + chr(95)*2 + 'name' + chr(95)*2 + ',\n'
open('app/main.py', 'w', encoding='utf-8').writelines(lines)

# Verify
lines2 = open('app/main.py', 'r', encoding='utf-8').readlines()
print('Line 33:', repr(lines2[32]))
print('Done')