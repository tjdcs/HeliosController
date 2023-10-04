from helios_controller import HeliosController


def main():
    hc = HeliosController("192.168.1.105")
    hc.patch("dev.display.brightness", 50)
    hc.patch("dev.display.blackout", False)

    hc.patch(hc.Paths.TEST_PATTERN_TYPE, hc.PatternTypes.RED)
    pass


if __name__ == "__main__":
    main()
