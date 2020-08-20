def read_template(location):
    """ reads the template from the location and returns it """
    return open(location, 'r').read()

def write_file(location, text):
    """ writes text to location !OVERRIDES! """
    f = open(location, "w")
    f.write(text)
    f.close()

def fill_template(template_location, output_location, **kwargs):
    template = read_template(template_location)
    in_brackets = False
    lines = template.split('\n')
    for line_count,line in enumerate(lines):
        tokens = line.split()
        for count, token in enumerate(tokens):
            if token[0] == '{' and token[-1] == '}':
                tokens[count] = kwargs[token[1:-1]]
        lines[line_count] = ' '.join(tokens)
    to_write = '\n'.join(lines)
    write_file(output_location, to_write)
