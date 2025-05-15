import json
#data aktivity
class TDEE():
    sangat_tidak_aktif = 1.2
    Tidak_aktif =  1.375
    Cukup_aktif = 1.55
    Aktif = 1.725
    Sangat_aktif = 1.9


def hitung_bmr():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    gender = data["gender"].lower()
    berat = float(data["weight"])
    tinggi = float(data["height"])
    usia = int(data["age"])
    activity = data["activity"]

    # Hitung BMR
    if gender == "male":
        bmr = 10 * berat + 6.25 * tinggi - 5 * usia + 5

    elif gender == "female":
        bmr = 10 * berat + 6.25 * tinggi - 5 * usia - 161
    else:
        print("Gender tidak valid.")
        return
    faktor_aktivitas = getattr(TDEE, activity, None)
    if faktor_aktivitas is None:
        print("Aktivitas tidak valid.")
        return
    
    tdee = bmr * faktor_aktivitas
    print(f"Total BMR kamu adalah: {bmr:.2f}")
    print(f"Total kebutuhan kalori harian (TDEE) kamu adalah: {tdee:.2f}")
    with open("data.json", "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4)
    
    exit
    
def get_data():
    data = {}
    data["gender"] = input("enter your gender(male/female):")
    data["age"] = input("enter your age:")
    data["weight"] = input("enter your weight:")
    data["height"] = input("enter your height:")
    print("tolong pilih salah satu(tulis seperti yang tanpil di layar):sangat_aktif, Tidak_aktif, Cukup_aktif, Aktif, Sangat_aktif")
    data["activity"] = input("activity:")
    if data["gender"] == "" or data["age"] == "" or data["height"] == "" or data["weight"] == "" or data["activity"] == "":
      print("invalid")
      return get_data()

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    hitung_bmr()