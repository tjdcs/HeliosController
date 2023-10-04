from helios_controller import HeliosController, CommonPaths, PatternTypes


def main():
    hc = HeliosController("192.168.1.105")
    hc.patch("dev.display.brightness", 50)
    hc.patch("dev.display.blackout", False)

    hc.patch(CommonPaths.TEST_PATTERN_TYPE, PatternTypes.RED)
    pass


if __name__ == "__main__":
    main()
