# IEEE Common Commands
# validos para todos los instrumentos

# Estructura general:
# - el comando comienza con Q, W o R
# - cada uno indexa una tupla donde
# - 1. tipo de comando
#   2. comando general
#   3. indicador si admite parametro

dicc_IEEE={'Q_identifier'            :('Q','*IDN',False),
           'W_reset'                 :('W','*RST' ,False),
           'Q_operation_complete'    :('Q','*OPC',False),
           'Q_service_request_enable':('Q','*SRE',True),
           'W_clear_status'          :('W','*CLS',False),
           'Q_event_status_register' :('Q','*ESR',True),
           'Q_status_byte'           :('Q','*STB',True),
           'Q_event_status_en'       :('Q','*ESE',True)}

# USO:
# debe pasar por build_command ( command, *parameter ):
# este metodo compone el comando y chequea errores en
# parametros.
# Luego el metodo cmd(command,*parameter):
# automatiza el envio y recepcion segun corresponda.
# El usuario con la primer letra del comando sabe de
# antemano si debe recibir o no.