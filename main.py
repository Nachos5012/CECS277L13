# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 05/-7/2024
# Module 13 - state
# Purpose - This module contains the main loop where users can interact with a simulated puppy. The user can feed or play with the puppy, and the puppy's reactions depend on its state.

import check_input
import puppy

def main():
  """
  The main function of the program.

  This function serves as the entry point to the program. It performs the following tasks:
  - Initializes a Puppy object.
  - Simulates interaction with the puppy by throwing a ball and giving food.
  - Prints out the actions performed and the puppy's state changes.

  Returns:
  None
  """
  print("Congratulations on your new puppy!")
  dog = puppy.Puppy()
  while True:
    print("What would you like to do?")
    print("1. Feed the puppy")
    print("2. Play with the puppy")
    print("3. Quit")
    choice = check_input.get_int_range("Enter choice: ", 1, 3)
    if choice == 1:
      print(dog.give_food())
    elif choice == 2:
      print(dog.throw_ball())
    else:
      print("Goodbye!")
      break
    print()

if __name__ == "__main__":
  main()

  
    