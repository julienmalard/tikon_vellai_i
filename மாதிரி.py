from tikon.móds.rae.orgs.insectos import MetamCompleta
from tikon.móds.rae.red import RedAE as வலை
from tikon.central import Modelo as மாதிரி

வெள்ளை_ஈ_ஆ_ரூஜியோ = MetamCompleta("A. rugioperculatus", njuvenil=3)
வெள்ளை_ஈ_பா_போந்தாரி = MetamCompleta("P. bondari", njuvenil=3)

கிரைசோபெர்லா_மா_போனியன்சிஸ் = MetamCompleta("M. boniensis", njuvenil=3)
கிரைசோபெர்லா_ஆ_அஸ்தூர் = MetamCompleta("A. astur", njuvenil=3)

# உணவு வலை உருவாக்கம்
வெள்ளை_ஈ_வலை = வலை([வெள்ளை_ஈ_ஆ_ரூஜியோ, வெள்ளை_ஈ_பா_போந்தாரி, கிரைசோபெர்லா_மா_போனியன்சிஸ், கிரைசோபெர்லா_ஆ_அஸ்தூர்])

with வெள்ளை_ஈ_வலை:
    கிரைசோபெர்லா_மா_போனியன்சிஸ்.secome(வெள்ளை_ஈ_ஆ_ரூஜியோ)
    கிரைசோபெர்லா_மா_போனியன்சிஸ்.secome(வெள்ளை_ஈ_பா_போந்தாரி)

    கிரைசோபெர்லா_ஆ_அஸ்தூர்.secome(வெள்ளை_ஈ_ஆ_ரூஜியோ)
    கிரைசோபெர்லா_ஆ_அஸ்தூர்.secome(வெள்ளை_ஈ_பா_போந்தாரி)

வெள்ளை_ஈ_மாதிரி = மாதிரி(வெள்ளை_ஈ_வலை)