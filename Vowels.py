def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(final)

string = "sonic solutions"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels)