def generate_letter():
    try:
        with open("./input/names/invited_names.txt") as file:
            names = [name.rstrip("\n") for name in file.readlines()]

        with open("./input/letters/starting_letter.txt", "r") as file:
            lines = file.readlines()
      
            for name in names:
                with open(f"./output/ready_to_send/letter_for_{name}", "w") as file:
                    updated_lines = [line.replace("[name]", name) for line in lines]
                    file.writelines(updated_lines)

    except FileNotFoundError as err:
        print(f"{err.strerror}: {err.filename}")

generate_letter()