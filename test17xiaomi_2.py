#! python3
x = ["X", "Ks", "S", "К", "Sh", "Ss", "К", "Кс", "С", "Х", "Ш", "Сс", "Х"]
i = ["i", "y", "e", "u", "m", "э", "ю", "и", "е", "м", "о", "а"]
a = ["a", "o", "y", "m", "", "a", "a", "o", "у", "м", "", "а"]
o = ["o", "u", "y", "o", "u", "y", "о", "у", "ю", "у", "", "", ]
m = ["m", "m", "m", "", "", "", "", "", "", "м", "м", "м"]
i_ = ["i", "y", "e", "u", "m", "ъ", "ы", "э", "ю", "и", "е", "м"]

cnt = 0

for x_ in x:
    for i__ in i:
        for a_ in a:
            for o_ in o:
                for m_ in m:
                    for i___ in i_:
                        print("Компания", x_+i__+a_+o_+m_+i___)

print("ALL NAMES OF XIAOMI NOW IS KNOWN!")
