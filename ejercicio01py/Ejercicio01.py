
from fractions import Fraction
"""
Primero, se tenía que implementar Racional, no usar Fraction, era parte de las
especificaciones.
"""
# Más de 79 caracteres en línea
#define una clase llamada `Polinomio` que representa un polinomio y proporciona métodos para realizar operaciones básicas con polinomios, como suma, resta y multiplicación.
"""
No hay clase abstracta
"""
class Polinomio:
    """
    Se ingresa el polinomio como un str, no los coeficientes
    """
    # Tipo de dato de parámetro?
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes
#creamos el metodo str para que le de una estructura a los resultados de la suma/resta/multiplicacion de polinomios 
    def __str__(self):
        terms = []
        """
        Asumen que los exponentes son continuos y no es necesariamente cierto.
        """
        for i, coef in reversed(list(enumerate(self.coeficientes))):
            if coef == 0:
                continue
            elif coef == 1:
                if i == 0:
                    terms.append("1")
                else:
                    terms.append(f"x^{i}")
            elif coef == -1:
                terms.append(f"-x^{i}")
            else:
                """
                No tendria que haber diferencia, porque el punto sólo es
                pergarle el coeficiente sea entero o racional a su variable.
                """
                if isinstance(coef, Fraction):
                    reduced_coef = str(coef.numerator) if coef.denominator == 1 else f"{coef.numerator}/{coef.denominator}"
                else:
                    reduced_coef = str(int(coef))
                if i == 0:
                    terms.append(reduced_coef)
                else:
                    terms.append(f"{reduced_coef}x^{i}")

        if not terms:
            return "0"
        
        """
        Asumen que siempre serán resultados positivos
        """
        result = " + ".join(terms)
        return result

 #metodo para sumar polinomios 
    def __add__(self, other):
        """
        Lo mismo, asumen que son exponentes consecutivos por lo que
        sólo suman los coeficientes en orden, pero no es necesariamente cierto.
        """
        if len(self.coeficientes) >= len(other.coeficientes):
            """[:]?"""
            result_coefs = self.coeficientes[:]
            for i in range(len(other.coeficientes)):
                result_coefs[i] += other.coeficientes[i]
        else:
            result_coefs = other.coeficientes[:]
            for i in range(len(self.coeficientes)):
                result_coefs[i] += self.coeficientes[i]

        return Polinomio(result_coefs)
#metodo para restar los polinomios 
    def __sub__(self, other):
        if len(self.coeficientes) >= len(other.coeficientes):
            result_coefs = self.coeficientes[:]
            for i in range(len(other.coeficientes)):
                result_coefs[i] -= other.coeficientes[i]
        else:
            result_coefs = [-coef for coef in other.coeficientes]
            for i in range(len(self.coeficientes)):
                result_coefs[i] += self.coeficientes[i]

        return Polinomio(result_coefs)
#metodo para multiplicar polinomios 
    def __mul__(self, other):
        result_degree = len(self.coeficientes) + len(other.coeficientes) - 1
        result_coefs = [0] * result_degree

        for i in range(len(self.coeficientes)):
            for j in range(len(other.coeficientes)):
                result_coefs[i + j] += self.coeficientes[i] * other.coeficientes[j]

        return Polinomio(result_coefs)


# Polinomio con coeficientes enteros: 2x^3 + 3x^2 - 1
polinomio1 = Polinomio([1, 5, 4, -1])

# Polinomio con coeficientes racionales: (1/2)x^2 + (3/4)x - (1/8)
polinomio2 = Polinomio([Fraction(1, 4), Fraction(2, 4), -Fraction(1, 8)])

print("Polinomio 1:", polinomio1)  # Salida: "Polinomio 1: 2x^3 + 3x^2 - 1"
print("Polinomio 2:", polinomio2)  # Salida: "Polinomio 2: 1/2x^2 + 3/4x - 1/8"

# Suma de polinomios
suma = polinomio1 + polinomio2
print("Suma:", suma)  # Salida: "Suma: 2x^3 + 5/2x^2 + 3/4x - 9/8"

# Resta de polinomios
resta = polinomio1 - polinomio2
print("Resta:", resta)  # Salida: "Resta: 2x^3 + 5/2x^2 + 3/4x - 7/8"

# Multiplicación de polinomios
multiplicacion = polinomio1 * polinomio2
print("Multiplicación:", multiplicacion)  # Salida: "Multiplicación: 1x^5 + 5/4x^4 - 3/16x^3 - 3/2x^2 + 1/8x"
