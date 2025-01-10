import os
import time
import random
import subprocess
import winsound 

def print_text(text, delay=1):
    """Выводит текст с задержкой."""
    print(text)
    time.sleep(delay)

def reboot_pc():
    """Перезагружает компьютер."""
    print_text("Rebooting...",1)
    time.sleep(1)
    os_name = os.name #Определяем текущую систему
    if os_name == "nt":
        subprocess.Popen("shutdown /r /t 1", shell=True)
    elif os_name == "posix":
        subprocess.Popen("sudo reboot", shell=True)
        
def play_sound():
  """Издаёт неприятный звук"""
  if os.name == "nt":
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)


def show_scare(text="A strange symbol appeared!", delay=1, reboot=False):
    """Показывает скример с возможностью перезагрузки."""
    print_text(text, delay)
    
    if random.random() < 0.4:
      play_sound()
      time.sleep(0.5)
      print("\n\n\n\n\n\n")
      if reboot:
        reboot_pc()
    else:
       print_text("\n\n\n\n")

def look_for_coke():
    """Сцена, когда игрок ищет колу."""
    print_text("You decide to look for your coke.", 2)
    print_text("The kitchen is dimly lit...", 1.5)
    time.sleep(1)
    print_text("You search the fridge...", 1)
    time.sleep(1)
    print_text("Nothing. Just pickles and a pulsating jelly.", 2)
    
    print_text("You hear a soft whisper from your room. You slowly go back...", 2)
    time.sleep(2)
    
    choice = input("Do you hide under the bed or look at the mirror? (hide/mirror): ").lower()
    if choice == "hide":
        print_text("You crawl under the bed. The air is thick with dust and a strange scent.", 2)
        show_scare("Something brushed against your leg... █", 1, reboot=True)
    elif choice == "mirror":
      print_text("You approach the mirror. You see your face distorted, it is...wrong. ▒ ", 2)
      show_scare("Your face is replaced with a screaming mask. ░░░", 1, reboot=True)
    else:
        print_text("You can not decide. A deafening crash from the window!", 1)
        show_scare("A dark figure appears briefly! Screen flickering",1, reboot=True)

def play_game():
    print_text("You are slumped on the sofa, controller in hand.", 2)
    print_text("The TV flickers with the last light of your PS4.", 2)
    print_text("You spot a pack of crab chips abandoned on the table.", 2)
    print_text("Your stomach rumbles. A familiar question surfaces...", 2)
    
    while True:
        open_choice = input("Open it and eat it? (yes/no): ").lower()
        if open_choice == "yes":
            print_text("You rip open the bag with greedy satisfaction.", 2)
            print_text("The intense aroma fills your senses...", 1.5)
            print_text("You finish the bag with the strange taste in your mouth.", 2)
            print_text("You immediately want some coke to wash it down...", 2)
            print_text("But there's no coke. You remember buying it. Maybe in a different reality?", 3)

            look_for_coke()

            break
        elif open_choice == "no":
            print_text("You decide to leave the chips alone. It's better for your diet.", 2)
            show_scare("A whisper says your name...", 2, reboot=True)
            break
        else:
            print_text("Please, enter 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()
