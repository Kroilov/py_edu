# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle(in_str):
    output = []
    current_char = in_str[0]
    count = 1

    for i in range(1, len(in_str)):
        if in_str[i] == current_char:
            count += 1
        else:
            output.append((current_char, count))
            current_char = in_str[i]
            count = 1

    output.append((current_char, count))

    return output


def rle_decomp(compressed):
    output = ''
    for char, count in compressed:
        output += char * count

    return output


with open('L:\gb_edu\Python_edu\homework_py\practice_05\input_text.txt', 'r') as f:
    in_str = f.read()

output = rle(in_str)

with open('L:\gb_edu\Python_edu\homework_py\practice_05\output_file.txt', 'w') as f:
    f.write(f'{output}\n{str(rle_decomp(output))}')

# print(output, '\n')
# print('Decompressed string:', rle_decomp(output))
