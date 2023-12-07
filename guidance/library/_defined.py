def defined(name, _parser_context=None):
  variable_stack = _parser_context['variable_stack']
  return name in variable_stack