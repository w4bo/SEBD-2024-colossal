import re
import argparse

parser = argparse.ArgumentParser(description='Cleaning bibliography.')
parser.add_argument('--dropunused', help='Drop unused bib', type=bool)
parser.add_argument('--input', help='Input bib file', type=str, default="../refs.bib")
parser.add_argument('--logfile', help='Log file', type=str, default="../thesis.log")
parser.add_argument('--texfile', help='Latex file', type=str, default="../main.tex")
args = parser.parse_args()

reg_bib = r"(@[a-zA-Z]*\{[a-zA-Z\:\/0-9,\n\s\=\{\}\-\t\.\(\)\\`\+'\"&’\*\_]*\}\n)"
reg_unused = r"Unused bibitem `([a-zA-Z0-9\:\/]*)'"
reg_biburl = r"[\t\s]*\b(biburl|bibsource|timestamp|doi)\b[\t\s]*\=[\s\t]*\{[a-zA-Z0-9\:\/\.\,\s\+]*\},?"
reg_title = r"\s+title\s*=\s*\{([a-zA-Z0-9\s:\-,\._!\"]*)\}"
reg_key = r"@\w+\{([\w:\/]*)"

unused_res = []

if args.dropunused:
    refs = ""
    with open(args.texfile, "r") as t:
        tex = t.read()
        with open(args.input, "r") as r:
            refs = r.read()
            pattern = re.compile(reg_bib)
            pattern_name = re.compile(reg_key)
            allrefs = print("Initial references: " + str(len(re.findall(pattern, refs))))
            for y in re.findall(pattern, refs):
                for x in re.findall(pattern_name, y):
                    if not x in tex:
                        refs = refs.replace(y, "")
                        unused_res.extend([x])
    print("Useless references: " + str(len(unused_res)))
    with open(args.input, "w") as r:
        refs = re.sub('\n+', '\n', refs)
        r.write(refs)

# refs = ""
# names = {}
# with open(args.input, "r", encoding="utf-8") as f:
#     refs = re.sub("è", "\`e", refs)
#     refs = re.sub("é", "\'e", refs)
#     refs = re.sub("à", "\`a", refs)
#     refs = re.sub("ò", "\`o", refs)
#     refs = re.sub("ù", "\`u", refs)
#     refs = re.sub("ì", "\`i", refs)
#     refs = re.sub(reg_biburl, "", refs)
#     refs = re.sub('\n+', '\n', refs)
#     pattern = re.compile(reg_bib)
#     pattern_name = re.compile(reg_title)
#     for x in re.findall(pattern, refs):
#         for orig_name in re.findall(pattern_name, x):
#             name = re.sub("\n", "", re.sub("\s", "", orig_name)).lower()
#             if name in names:
#                 names[name].append(orig_name)
#             else:
#                 names[name] = [orig_name]
# 
#         for y in unused_res:
#             if y in x:
#                 unused_res.remove(y)
#                 refs = refs.replace(x, "")    
# 
# 
# print("Remaining unused bibs: " + str(len(unused_res)))
# print("Still to remove: " + str(unused_res))
# print("Redundant papers:")
# for k, v in names.items():
#     if len(v) > 1:
#         print(v)
