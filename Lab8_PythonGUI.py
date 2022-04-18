from cgitb import text
from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_info

def main():

    root = Tk()
    root.title("Pokemon Information")
    root.iconbitmap("Poke-Ball.ico")
    #root.geometry('400x400')
    
    
    frame_top = ttk.Frame(root)
    frame_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    frame_info = ttk.LabelFrame(root, text='Info')
    frame_info.grid(row=1, column=0, padx=10, pady=10)

    frame_stats = ttk.LabelFrame(root, text='stats')
    frame_stats.grid(row=1, column=1, padx=10, pady=10)

    lbl_name = ttk.Label(frame_top, text='Pokemon Name:')
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    ent_name = ttk.Entry(frame_top)
    ent_name.grid(row=0, column=1, pady=10)

    def btn_get_info_click():
        pokemon_name = ent_name.get()
        poke_dict = get_pokemon_info(pokemon_name)

        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + ' hg'
            types_list = [t['type']['name'] for t in poke_dict['types']]
            lbl_type_val['text'] = ', '.join(types_list)
        
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attack['value'] = poke_dict['stats'][1]['base_stat']
            prg_defence['value'] = poke_dict['stats'][2]['base_stat']
            prg_sattack['value'] = poke_dict['stats'][3]['base_stat']
            prg_sdefence['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']

    btn_get_info = ttk.Button(frame_top, text='Get Info', command=btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10)


    lbl_height = ttk.Label(frame_info, text='Height:')
    lbl_height.grid(row=100, column=100, padx=(10,0), pady=10, sticky=E)

    lbl_height_val = ttk.Label(frame_info)
    lbl_height_val.grid(row=100, column=200, padx=(10), pady=10, sticky=W)


    lbl_weight = ttk.Label(frame_info, text='Weight:')
    lbl_weight.grid(row=200, column=100, padx=(10,0), pady=10, sticky=E)

    lbl_weight_val = ttk.Label(frame_info)
    lbl_weight_val.grid(row=200, column=200, padx=10, pady=10, sticky=W)


    lbl_type = ttk.Label(frame_info, text='Type:')
    lbl_type.grid(row=300, column=100, padx=(10,0), pady=10, sticky=E)

    lbl_type_val = ttk.Label(frame_info)
    lbl_type_val.grid(row=300, column=200, padx=10, pady=10, sticky=W)


    lbl_hp = ttk.Label(frame_stats, text='HP:')
    lbl_hp.grid(row=100, column=100, padx=(10,0), pady=10, sticky=E)
    prg_hp = ttk.Progressbar(frame_stats, length=200, maximum=250)
    prg_hp.grid(row=100, column=200, padx=(5,10), pady=10, sticky=W)
 
    lbl_attack = ttk.Label(frame_stats, text='Attack:')
    lbl_attack.grid(row=200, column=100, padx=(10,0), sticky=E)
    prg_attack = ttk.Progressbar(frame_stats, length=200, maximum=250)
    prg_attack.grid(row=200, column=200, padx=(5,10), sticky=W)

    lbl_defence = ttk.Label(frame_stats, text='Defence:')
    lbl_defence.grid(row=300, column=100, padx=(10,0), pady=10, sticky=E)
    prg_defence = ttk.Progressbar(frame_stats, length=200, maximum=250)
    prg_defence.grid(row=300, column=200, padx=(5,10), pady=10, sticky=W)

    lbl_sattack = ttk.Label(frame_stats, text='Special Attack:')
    lbl_sattack.grid(row=400, column=100, padx=(10,0), sticky=E)
    prg_sattack = ttk.Progressbar(frame_stats, length=200, maximum=250)
    prg_sattack.grid(row=400, column=200, padx=(5,10), sticky=W)

    lbl_sdefence = ttk.Label(frame_stats, text='Special Defence:')
    lbl_sdefence.grid(row=500, column=100, padx=(10,0), pady=10, sticky=E)
    prg_sdefence = ttk.Progressbar(frame_stats, length=200, maximum=250)
    prg_sdefence.grid(row=500, column=200, padx=(5,10), sticky=W)

    lbl_speed = ttk.Label(frame_stats, text='Speed:')
    lbl_speed.grid(row=600, column=100, padx=(10,0), sticky=E)
    prg_speed = ttk.Progressbar(frame_stats, length=200, maximum=250)
    prg_speed.grid(row=600, column=200, padx=(5,10), pady=10, sticky=W)


    root.mainloop()


main()
