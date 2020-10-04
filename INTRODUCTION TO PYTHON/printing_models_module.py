def printing_designs(unprinted_designs, printed_designs):

  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")

    printed_designs.append(current_design)


def summarize_prints(printed_designs):
  for printed_design in printed_designs:
    print(printed_design)