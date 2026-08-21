# Electromagnetic Wave Monitoring Program
# Simulates EM wave levels from electronic devices and suggests
# preventive actions when levels are high, to protect animal and sea life.

SAFE_LIMIT = 50  # Safe EM wave level (arbitrary units)


def check_em_wave(level):
    print("EM Wave Level:", level)
    if level <= SAFE_LIMIT:
        print("Status: Safe for animals")
    else:
        print("Status: DANGEROUS")
        print("Prevention Actions:")
        print("- Reduce device power usage")
        print("- Turn off unused electronic devices")
        print("- Use EM shielding materials")
        print("- Maintain distance from wildlife areas")


if __name__ == "__main__":
    em_level = int(input("Enter electromagnetic wave level: "))
    check_em_wave(em_level)
    print("[Process completed]")
