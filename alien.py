
class Alien:
    def __init__(self, color: str, points: int) -> None:
        # Type hints for vsCode
        self.color = color
        self.points = points

    def __repr__(self) -> str:
        # for easy printing 
        return f"{self.color} {self.points}" 

def main():
    a0 = Alien("green", 5)
    print(a0)
    print(f"You just earned {a0.points} points!")

if __name__ == "__main__":
    main()

# Original Code

og_code = """
alien_0 = {'color' : 'green', 'points' : 5}  
# the '_0' in 'alien' holds no significance as to if the dictionary was just 'alien'

print(f"{alien_0['color']} {alien_0['points']}")
print("{0} {1}".format(alien_0['color'], alien_0['points']))

new_points = alien_0['points']
print(f'You just earned {new_points} points!')
"""