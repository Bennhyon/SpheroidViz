import tkinter as tk
import sim_visu
import time
window_min_width = "500"
window_min_height = "281"
window_collection = []

main_window = tk.Tk()
window_collection.append(main_window)
main_window.minsize(width=window_min_width, height=window_min_height)


def windowPop():
    popup = sim_visu.popup()
    window_collection.append(popup)
    popup.update()

texte = tk.Label(main_window, text="hélo waurld")
texte.grid(row=0, column=0, sticky="n")
bouton = tk.Button(main_window, text="Lancer la visualisation", command=windowPop)
bouton.grid(row=1, column=0)
main_window.mainloop()