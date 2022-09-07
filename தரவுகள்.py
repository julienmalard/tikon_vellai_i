import os

from tikon.central import Parcela as வயில்
from tikon.central.exper import Exper as சோதனை
from tikon.central.parc import GeomParcela
from tikon.móds.rae.red.obs import ObsPobs

from மாதிரி import வெள்ளை_ஈ_ஆ_ரூஜியோ, வெள்ளை_ஈ_பா_போந்தாரி, கிரைசோபெர்லா_மா_போனியன்சிஸ், கிரைசோபெர்லா_ஆ_அஸ்தூர்

# கண்டறியப்பட்ட தரவுகள்
மூல்_கோப்புரை = os.path.split(__file__)[0]
எண்ணிக்கை = ObsPobs.de_cuadro(
    os.path.join(மூல்_கோப்புரை, 'பூச்சி.csv'),
    parcela='வயல் அ',
    tiempo='நாள்',
    corresp={
        'A. rugioperculatus nymph/ leaves/ frond/ tree': வெள்ளை_ஈ_ஆ_ரூஜியோ['juvenil 1'] + வெள்ளை_ஈ_ஆ_ரூஜியோ['juvenil 2']+  வெள்ளை_ஈ_ஆ_ரூஜியோ['juvenil 3'] +  வெள்ளை_ஈ_ஆ_ரூஜியோ['pupa'],
        'P. bondari nymph/ leaves/ frond/ tree': வெள்ளை_ஈ_பா_போந்தாரி['pupa'],
        'Mallada boniensis': கிரைசோபெர்லா_மா_போனியன்சிஸ்['pupa'],
        'Apertochrysa astur': கிரைசோபெர்லா_ஆ_அஸ்தூர்['pupa'],
    },
    factor=200 / 10 * 20 / 5 * 100 / 10  # தெண்ணைக்கையின் கூட்டி இலை மூலம் ஹெக்டேருக்கு மாற்றம்
)
# வெள்ளை_ஈ_ஆ_ரூஜியோ.activar_ecs({'huevo': {'muerte': 'Lluvia linear'}})

வயில்_அ = சோதனை('வயல் அ', வயில்('வயல் அ', geom=GeomParcela((7.297, 79.865))))
வயில்_அ.datos.agregar_obs(எண்ணிக்கை)
