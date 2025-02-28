suits = ["h", "d", "c", "s"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [v+s for v in values for s in suits]

def draw():
    pass

def main():
    assert len(deck) == 52, "There should be 52 cards in a standard deck"


if __name__ == "__main__":
    main()