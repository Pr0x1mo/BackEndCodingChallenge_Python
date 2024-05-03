def solution (pin):

    adjacent = {
        '1':['1','2','4'],
        '2':['1','2','3','5'],
        '3':['2','3','6'],
        '4':['1','4','5','7'],
        '5':['2','4','5','6','8'],
        '6':['3', '5', '6','9'],
        '7':['4', '7', '8'],
        '8':['5','7','8','9','0'],
        '9':['6','8','9'],
        '0':['8','0']
    }

    def generate_pins(current_pin, index):
        if index ==len(pin):
            results.append(current_pin)
            return

        current_digit= pin[index]
        for adj_digit in adjacent[current_digit]:
            generate_pins(current_pin + adj_digit, index +1)
    
    results = []
    generate_pins('',0)
    results = sorted(set(results))
    return results

pin = input()

out_ = solution(pin)
for i_out_ in out_:
    print (i_out_)