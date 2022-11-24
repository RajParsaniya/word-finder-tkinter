import webbrowser
from random import choice
from random import shuffle
from tkinter import *

from words import words

root = Tk()
root.title('Word Finder')
root.geometry("600x400")

hint_count = 0
shuffled_word = ""
word = ""
my_label = Label(root, text="", font=("Helvetica", 48))
my_label.pack(pady=20)


def explore_more_projects():
    url = "https://github.com/RajParsaniya"
    webbrowser.open_new_tab(url)
    root.destroy()


def main():
    entry_answer.delete(0, END)
    answer_label.config(text='')
    hint_label.config(text='')

    global hint_count
    hint_count = 0

    global word
    word = choice(words)
    my_label.config(text=word)

    break_apart_word = list(word)
    shuffle(break_apart_word)
    # print(break_apart_word)

    global shuffled_word
    shuffled_word = ''
    for letter in break_apart_word:
        shuffled_word += letter

    my_label.config(text=shuffled_word)


def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct word !!!")
    else:
        answer_label.config(text="Incorrect word !!!")


def hint(count):
    global hint_count
    hint_count = count

    word_length = len(word)
    if count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {word[count]}')
        hint_count += 1


entry_answer = Entry(root, font=("Helvetica", 24))
entry_answer.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Check", command=answer)
answer_button.grid(row=0, column=0, padx=10)

my_button = Button(button_frame, text="Skip", command=main)
my_button.grid(row=0, column=1, padx=10)

hint_button = Button(button_frame, text="Hint", command=lambda: hint(hint_count))
hint_button.grid(row=0, column=2, padx=10)

web_button = Button(button_frame, text="Explore more projects", command=explore_more_projects)
web_button.grid(row=0, column=3, padx=10)

answer_label = Label(root, text='', font=("Helvetica", 18))
answer_label.pack(pady=20)

hint_label = Label(root, text='', font=("Helvetica", 18))
hint_label.pack(pady=10)

main()
root.mainloop()
