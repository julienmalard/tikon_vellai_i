from tikon.central.calibs import EspecCalibsCorrida
from tikon.datos.proc import distancia_del_centro, cuantiles, ens

from a_prioris import a_prioris
from தரவுகள் import வயில்_அ
from மாதிரி import வெள்ளை_ஈ_வலை, வெள்ளை_ஈ_மாதிரி

அளவீடு = False
முதிப்பீடும்_முறை = cuantiles

if __name__ == '__main__':
    # புது உணவு வலைக்காக ஆரம்ப நிகழ்வெண் பரவல்கள்
    for பூச்சி, நிகழ்வெண்_பட்டியல் in a_prioris.items():
        for நிகழ்வெண்_அகராதி in நிகழ்வெண்_பட்டியல்:
            படி = நிகழ்வெண்_அகராதி.pop('stage')
            try:
                வெள்ளை_ஈ_வலை[பூச்சி][படி].espec_apriori(**நிகழ்வெண்_அகராதி)
            except KeyError:
                pass

    # அளவீடு
    if அளவீடு:
        வெள்ளை_ஈ_மாதிரி.calibrar('வயல் அ test cuantiles', exper=வயில்_அ, proc=முதிப்பீடும்_முறை)

        # விளைவு சேமிப்பு
        வெள்ளை_ஈ_மாதிரி.guardar_calibs('வெளியீடு/அளவீடு வயில் அ cuantiles')
        வயில்_அ.guardar_calibs('வெளியீடு/அளவீடு வயில் அ cuantiles')

    # சரிபார்த்தல் மற்றும் வரைதல்
    விளைவுகள் = வெள்ளை_ஈ_மாதிரி.simular(
        'valid', exper=வயில்_அ, reps=40,
        calibs=EspecCalibsCorrida(aprioris=False), depurar=True,
        vars_interés=["red.Pobs", "red.Muerte"]
    )
    # pprint(விளைவுகள்.validar().a_dic())
    விளைவுகள்.graficar('வெளியீடு/உருப்படங்கள்')
