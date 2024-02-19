import re


def read_input():
    all_rules = {}
    with open('day7input.txt', 'r') as input_file:
        for line in input_file:
            bag = line.split("bags")[0].strip()
            contents = line.split("contain")[-1].strip('.\n')
            bag_contents = []
            for content in contents.split(','):
                if content == ' no other bags':
                    # print('no other bags')
                    continue
                else:
                    count = int(content.split()[0])
                    bag_colour = re.sub('[1-9]', '', content).strip(r"(\s)bag\w+")
                    bag_contents.append((count, bag_colour.strip()))

            all_rules[bag] = bag_contents

    return all_rules


def find_shiny_gold_bags(all_rules, rule):
    count = 0
    bag = all_rules[rule]

    if len(bag) == 0:
        return 0
    else:
        for sub_bag in bag:
            if sub_bag[1] == 'shiny gold':
                count += 1
            count += find_shiny_gold_bags(all_rules, sub_bag[1])

    return count


def bags_in_shiny_gold(all_rules, bags):
    count = 0
    contents = all_rules[bags]
    if len(contents) == 0:
        return 0
    else:
        for content in contents:
            amount = content[0]
            colour = content[1]
            count += amount
            bags_inside_bag = bags_in_shiny_gold(all_rules, colour)
            count += amount * bags_inside_bag
    return count


def solution():
    all_rules = read_input()
    contains_shiny_gold = []

    for key in all_rules.keys():
        shiny_gold_count = find_shiny_gold_bags(all_rules, key)
        if shiny_gold_count > 0:
            contains_shiny_gold.append(shiny_gold_count)

    print(f'solution 1: {len(contains_shiny_gold)} bags contain at least 1 shiny gold bag')

    print(f"solution 2: {bags_in_shiny_gold(all_rules, 'shiny gold')}")


if __name__ == '__main__':
    solution()
