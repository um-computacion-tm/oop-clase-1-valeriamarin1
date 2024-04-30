class Profesor:
    def __init__(self, el_nombre, el_email): #el init es el constructor 
        self.__nombre__ = el_nombre
        self.__email__ = el_email
         #este self es yo mismo
    def dame_tu_nombre(self):
        return self.__nombre__
    #esta dentro del profesor
class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None
    #este el modelado de la clase alumno
    def mentoria(self, profesor):
        self.__mentor__ = profesor


    def falta(self):
        self.__inasistencias__ += 1

    
    def elegir_dieta_especial(self, la_dieta):
        self.__dieta__ = la_dieta
    
    def esta_libre(self):
        if self.__inasistencias__ >= 5:
            return "ESTA LIBRE"
        else:
            return "OK"



alumno_juan = Alumno("juancito")
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())  # Debería imprimir "OK"
alumno_juan.falta()
print(alumno_juan.esta_libre())

profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")
print(profe_elio.dame_tu_nombre())

alumno_maria = Alumno("Maria")
alumno_maria.elegir_dieta_especial("vegetariana")
print(alumno_maria.obtener_dieta())

alumno_juan.mentoria(profe_elio)
print(alumno_juan.dame_tu_nombre())
#print(profe_elio.dame_tu_nombre())
#print(profe_gabi.dame_tu_nombre())

#esta es la clase
#quiero un objedo de elio
#creo una segunda estancia la del profe gabi
#import ipdb; ipdb.set_trace()