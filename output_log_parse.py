import sys


def info_store(epoch_info):
    if len(epoch_info) == 5:
        id.append(epoch_info["id"])
        valid_micro.append(epoch_info["valid_micro"])
        valid_f1.append(epoch_info["valid_f1"])
        test_micro.append(epoch_info["test_micro"])
        test_f1.append(epoch_info["test_f1"])


def info_parse(stat, epoch_info, line):
    if "Epoch" in line and "begin" in line:
        epoch_info["id"] = int(line.split("Epoch ")[1].split(" ")[0])
    elif "Evaluate on valid" in line:
        stat = 1
    elif "Evaluate on test" in line:
        stat = 2
    elif stat == 1:
        if "auprc@micro" in line:
            epoch_info["valid_micro"] = float(line.split("auprc@micro:")[1])
        elif "f1_max" in line:
            epoch_info["valid_f1"] = float(line.split("f1_max:")[1])
    elif stat == 2:
        if "auprc@micro" in line:
            epoch_info["test_micro"] = float(line.split("auprc@micro:")[1])
        elif "f1_max" in line:
            epoch_info["test_f1"] = float(line.split("f1_max:")[1])

    return stat, epoch_info

def main():
    stat = 0
    epoch_info = {}
    for line in sys.stdin:
        line = line.strip()
        if "Epoch" in line and "begin" in line:
            info_store(epoch_info)

            stat = 0
            epoch_info.clear()

            stat, epoch_info = info_parse(stat, epoch_info, line)
        else:
            stat, epoch_info = info_parse(stat, epoch_info, line)
    info_store(epoch_info)


if __name__ == "__main__":
    id = []
    valid_micro = []
    valid_f1 = []
    test_micro = []
    test_f1 = []

    main()
    print(id)
    print(valid_micro)
    print(valid_f1)
    print(test_micro)
    print(test_f1)
