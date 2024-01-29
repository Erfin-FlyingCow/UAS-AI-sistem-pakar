def evaluate_rule(rule, facts):
    conditions = rule['conditions']
    for condition in conditions:
        if not facts.get(condition, False):
            return False
    return True



def main():
    # Definisikan aturan dan fakta
    dental_diseases = {
    'T1': 'Gingivitis',
    'T2': 'Karies gigi',
    'T3': 'Trench Mouth',
    'T4': 'Pulpitis',
    'T5': 'Nekrosis Pulpa',
    'T6': 'Periodentitis',
    'T7': 'Impaksi Gigi',
    'T8': 'Glositis'
}
    
    # Membuat dictionary dengan Q sebagai key
    dental_symptoms = {
    'Q1': 'Mulut berbau.',
    'Q2': 'Nyeri saat makan atau menelan.',
    'Q3': 'Pendarahan dari gusi saat ditekan sedikit.',
    'Q4': 'Perubahan warna gusi.',
    'Q5': 'Adanya inflamasi atau peradangan di sekitar gigi yang mengenai jaringan lunak pada gigi.',
    'Q6': 'Gusi kendor, bergeser atau lepas.',
    'Q7': 'Gigi yang menjadi lebih sensitif.',
    'Q8': 'Ada noda coklat, hitam atau putih pada permukaan gigi.',
    'Q9': 'Rasa tidak nyaman pada mulut.',
    'Q10': 'Sakit gigi muncul secara tiba-tiba tanpa sebab yang jelas.',
    'Q11': 'Luka seperti kawah di antara gigi dan gusi.',
    'Q12': 'Demam dan kelelahan.',
    'Q13': 'Pembengkakan kelenjar limfa di sekitar kepala, leher atau rahang.',
    'Q14': 'Rasa sakit yang menusuk tajam dan intens.',
    'Q15': 'Nyeri pada gigi berlangsung beberapa jam.',
    'Q16': 'Nyeri tambah parah di malam hari.',
    'Q17': 'Nyeri muncul atau bertambah pada saat posisi tubuh tertentu (merunduk).',
    'Q18': 'Gusi nyeri saat disentuh.',
    'Q19': 'Ada nanah antara gigi dan gusi.',
    'Q20': 'Gigi goyang.',
    'Q21': 'Penumpukan plak dan karang gigi.',
    'Q22': 'Sakit kepala berkepanjangan.',
    'Q23': 'Pembengkakan di rahang.',
    'Q24': 'Gusi merah atau membengkak.',
    'Q25': 'Rasa sakit pada area lidah.',
    'Q26': 'Bengkak pada lidah.',
    'Q27': 'Perubahan warna lidah jadi pucat atau merah terang.'
}


    # Membuat dictionary dengan aturan-aturan
    dental_rules = {
    1: {
        'conditions': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'],
        'conclusion': 'T1'
    },
    2: {
        'conditions': ['Q1', 'Q2', 'Q7', 'Q8', 'Q9', 'Q10'],
        'conclusion': 'T2'
    },
    3: {
        'conditions': ['Q1', 'Q2', 'Q3', 'Q4', 'Q6', 'Q9', 'Q11', 'Q12', 'Q13'],
        'conclusion': 'T3'
    },
    4: {
        'conditions': ['Q1', 'Q2', 'Q9', 'Q12'],
        'conclusion': 'T4'
    },
    5: {
        'conditions': ['Q14', 'Q15', 'Q16', 'Q17'],
        'conclusion': 'T5'
    },
    6: {
        'conditions': ['Q1', 'Q3', 'Q11', 'Q18', 'Q19', 'Q20', 'Q21'],
        'conclusion': 'T6'
    },
    7: {
        'conditions': ['Q2', 'Q13', 'Q22', 'Q23', 'Q24'],
        'conclusion': 'T7'
    },
    8: {
        'conditions': ['Q24', 'Q25', 'Q26', 'Q27'],
        'conclusion': 'T8'
    }
}


    dental_facts = {
    
}
    

    # Membuat dictionary bobot
    bobot_gejala = {
    'Q1': 5,
    'Q2': 10,
    'Q3': 10,
    'Q4': 10,
    'Q5': 15,
    'Q6': 15,
    'Q7': 15,
    'Q8': 10,
    'Q9': 5,
    'Q10': 15,
    'Q11': 15,
    'Q12': 20,
    'Q13': 20,
    'Q14': 20,
    'Q15': 15,
    'Q16': 20,
    'Q17': 25,
    'Q18': 20,
    'Q19': 15,
    'Q20': 5,
    'Q21': 20,
    'Q22': 15,
    'Q23': 20,
    'Q24': 15,
    'Q25': 20,
    'Q26': 20,
    'Q27': 25
}

    

    # Evaluasi aturan dan perbarui fakta
    index = 1

    for key, value in dental_symptoms.items():
        user_input = input(f"Apakah anda mengalami {value}. Enter 'ya' or 'tidak': ")
        if user_input.lower() == 'ya':
        # Menggunakan f-string untuk membuat kunci yang dinamis
            dental_facts[f'Q{index}'] = True
        elif user_input.lower() == 'tidak':
            dental_facts[f'Q{index}'] = False
    # Menambahkan nilai index setiap loop
        index += 1

    total_bobot = 0  # Inisialisasi total bobot
    gejala_dialami = []  # Inisialisasi daftar gejala yang dialami

    # Perhitungan bobot berdasarkan fakta yang benilai True
    for key, value in dental_facts.items():
        if value:  # Cek apakah fakta bernilai True
            total_bobot += bobot_gejala[key]  # Tambahkan bobot ke total_bobot
            gejala_dialami.append(dental_symptoms[key])  # Tambahkan gejala ke daftar gejala yang dialami

    
    print(f"Total bobot berdasarkan fakta yang benilai True: {total_bobot}")

    for key, rule_value in dental_rules.items():
        if evaluate_rule(rule_value, dental_facts):
            print(f"Anda mungkin mengalami: {dental_diseases[rule_value['conclusion']]}")
            print(f"Dengan Tingkat Keparahan: {total_bobot}%")

            break
    else:
        print("Tidak ada diagnosis yang sesuai dengan gejala yang Anda alami.")

    
main()