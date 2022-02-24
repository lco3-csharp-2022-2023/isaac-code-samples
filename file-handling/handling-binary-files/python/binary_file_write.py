# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import pickle  # Module for working with binary files

def write_file(player_stats):
    """Simple example of writing to a binary file"""
    with open("treasure.game", "wb") as gamefile:
        pickle.dump(player_stats, gamefile) 

    
def main():
    player_stats = {"health": 100, "hunger":10, "money": 20.00, "lives":3}
    write_file(player_stats)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main()
