import os

from tikon.central import Modelo, Parcela
from tikon.central.exper import Exper
from tikon.central.parc import GeomParcela
from tikon.móds.rae.orgs.insectos import MetamCompleta
from tikon.móds.rae.red import RedAE
from tikon.móds.rae.red.obs import ObsPobs

வெள்ளை_ஈ_1 = MetamCompleta("A. rugioperculatus", njuvenil=3)
வெள்ளை_ஈ_2 = MetamCompleta("P. bondari", njuvenil=3)

கிரைசோபெர்லா_1 = MetamCompleta("M. boniensis", njuvenil=3)
கிரைசோபெர்லா_2 = MetamCompleta("A. astur", njuvenil=3)

கிரைசோபெர்லா_1.secome(வெள்ளை_ஈ_1)
கிரைசோபெர்லா_1.secome(வெள்ளை_ஈ_2)

கிரைசோபெர்லா_2.secome(வெள்ளை_ஈ_1)
கிரைசோபெர்லா_2.secome(வெள்ளை_ஈ_2)

# உணவு வலை உருவாக்கம்
வலை = RedAE([வெள்ளை_ஈ_1, வெள்ளை_ஈ_2, கிரைசோபெர்லா_1, கிரைசோபெர்லா_2])

# கண்டறியப்பட்ட தரவுகள்
மூல்_கோப்புரை = os.path.split(__file__)[0]
எண்ணிக்கை = ObsPobs.de_cuadro(
    os.path.join(மூல்_கோப்புரை, 'பூச்சி.csv'),
    parcela='வயல் அ',
    tiempo='நாள்',
    corresp={
        'A. rugioperculatus nymph/ leaves/ frond /tree': வெள்ளை_ஈ_1['pupa'],
    },
    factor=200 / 10 * 20 / 5 * 100 / 10  # எண்ணைக்கையை கூட்டி இலை மூலம் ஹெக்டேருக்கு மாற்றம்
)
வெள்ளை_ஈ_1.activar_ecs({'huevo': {'muerte': 'Lluvia linear'}})

வயில்_அ = Exper('வயல் அ', Parcela('வயல் அ', geom=GeomParcela((7.297, 79.865))))
வயில்_அ.datos.agregar_obs(எண்ணிக்கை)
மாதிரி = Modelo(வலை)
