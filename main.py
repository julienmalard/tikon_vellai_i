from tikon.central import Tiempo
from tikon.central.calibs import EspecCalibsCorrida

from a_prioris import a_prioris
from மாதிரி import மாதிரி, வலை, வயில்_அ

if __name__ == '__main__':
    # புது உணவு வலைக்காக ஆரம்ப நிகழ்வெண் பரவல்கள்
    for பூச்சி, நிகழ்வெண்_பட்டியல் in a_prioris.items():
        for நிகழ்வெண்_அகராதி in நிகழ்வெண்_பட்டியல்:
            படி = நிகழ்வெண்_அகராதி.pop('stage')
            try:
                வலை[பூச்சி][படி].espec_apriori(**நிகழ்வெண்_அகராதி)
            except KeyError:
                pass

    # அளவீடு
    ஆரம்பு_தேதி = '2021-01-01'
    கடைசியான_தேதி = '2021-05-30'
    # மாதிரி.calibrar('வயல் அ', exper=வயில்_அ, t=ஆரம்பு_தேதி)

    # விளைவு சேமிப்பு
    # மாதிரி.guardar_calibs('வெளியீடு/அளவீடு வயில் அ')
    # வயில்_அ.guardar_calibs('வெளியீடு/அளவீடு வயில் அ')

    # சரிபார்த்தல் மற்றும் வரைதல்
    விளைவுகள் = மாதிரி.simular(
        'valid', exper=வயில்_அ, reps=30, t=Tiempo(ஆரம்பு_தேதி, கடைசியான_தேதி), calibs=EspecCalibsCorrida(aprioris=False), depurar=True,
        vars_interés=["red.Pobs", "red.Muerte"]
    )
    # pprint(விளைவுகள்.validar().a_dic())
    விளைவுகள்.graficar('வெளியீடு/உருப்படங்கள்')
