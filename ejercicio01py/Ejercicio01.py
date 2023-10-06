from abc import ABC, abstractmethod
from fractions import Fraction

class Polinomio(ABC):
     """
    Clase que representa un polinomio y proporciona métodos para realizar operaciones básicas
    como suma, resta y multiplicación entre polinomios.
    """

     def __init__(self, coeficientes):
        """
        Constructor de la clase Polinomio.

        Args:
            coeficientes (list): Una lista de coeficientes que representan los términos del polinomio.
        """
        self.coeficientes = coeficientes

     @abstractmethod
     def __str__(self):
        pass

     @abstractmethod
     def operacion(self, other):
        pass

     @abstractmethod
     def multiplicar(self, other):
        pass



     @abstractmethod
     def restar(self, other):
        pass


class PolinomioModificado(Polinomio):
    def __str__(self):
        """
        Método para representar el polinomio en forma de cadena.

        Returns:
            str: Representación en cadena del polinomio.
        """
        terms = []
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

        result = " + ".join(terms)
        return result

    def operacion(self, other):
        """
        Método para realizar la suma de dos polinomios.

        Args:
            other (Polinomio): Otro objeto de tipo Polinomio para sumar.

        Returns:
            Polinomio: Un nuevo objeto Polinomio que representa la suma.
        """
        
        result_degree = max(len(self.coeficientes), len(other.coeficientes))
        result_coefs = [0] * result_degree

        for i in range(len(self.coeficientes)):
            result_coefs[i] += self.coeficientes[i]

        for i in range(len(other.coeficientes)):
            result_coefs[i] += other.coeficientes[i]

        return PolinomioModificado(result_coefs)

    def multiplicar(self, other):
         """
        Método para realizar la multiplicación de dos polinomios.

        Args:
            other (Polinomio): Otro objeto de tipo Polinomio para multiplicar.

        Returns:
            Polinomio: Un nuevo objeto Polinomio que representa la multiplicación.
        """

         result_degree = len(self.coeficientes) + len(other.coeficientes) - 1
         result_coefs = [0] * result_degree

         for i in range(len(self.coeficientes)):
            for j in range(len(other.coeficientes)):
                result_coefs[i + j] += self.coeficientes[i] * other.coeficientes[j]

         return PolinomioModificado(result_coefs)


    def restar(self, other):
         """
        Método para realizar la resta de dos polinomios.

        Args:
            other (Polinomio): Otro objeto de tipo Polinomio para restar.

        Returns:
            Polinomio: Un nuevo objeto Polinomio que representa la resta.
        """
         result_degree = max(len(self.coeficientes), len(other.coeficientes))
         result_coefs = [0] * result_degree

         for i in range(len(self.coeficientes)):
            result_coefs[i] += self.coeficientes[i]

         for i in range(len(other.coeficientes)):
            result_coefs[i] -= other.coeficientes[i]

         return PolinomioModificado(result_coefs)

# Ejemplo de uso
polinomio1 = PolinomioModificado([1, 2, 3])
polinomio2 = PolinomioModificado([Fraction(1, 4), Fraction(2, 4), Fraction(-1, 8)])

print("El polinomio 1 es: ",polinomio1) #salida: El polinomio 1 es:  3x^2 + 2x^1 + 1
print("El polinomio 2 es: ",polinomio2) #salida: El polinomio 2 es:  -1/8x^2 + 1/2x^1 + 1/4

resultado_suma = polinomio1.operacion(polinomio2) 
resultado_resta = polinomio1.restar(polinomio2)
resultado_multiplicacion = polinomio1.multiplicar(polinomio2)


print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)
print("Resultado de la multiplicación:", resultado_multiplicacion)

