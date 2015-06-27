from clint.textui import puts, indent, colored

puts('not indented text')
with indent(4):
    puts(colored.red('indented text'))
