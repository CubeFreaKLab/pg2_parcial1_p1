from conversor_basico import ConversorBasico

class ConversorDistancia(ConversorBasico):
    def __init__(self):
        # Llamamos al constructor de la clase padre
        super().__init__()
    
    def metros_a_centimetros(self, cantidad_metros):
        """
        Convierte metros a centímetros
        
        Args:
            cantidad_metros: Cantidad en metros a convertir
        
        Returns:
            La cantidad equivalente en centímetros
        """
        # Establecemos las unidades
        self._unidad_origen = "metros"
        self._unidad_destino = "centímetros"
        
        # Utilizamos el método de conversión genérica de la clase padre
        # 1 metro = 1 en unidad base, 1 centímetro = 0.01 en unidad base
        resultado = self._conversion_generica(cantidad_metros, 1, 100)
        
        # Mostramos los resultados
        self._mostrar_resultados()
        
        return resultado
    
    def centimetros_a_kilometros(self, cantidad_centimetros):
        """
        Convierte centímetros a kilómetros
        
        Args:
            cantidad_centimetros: Cantidad en centímetros a convertir
        
        Returns:
            La cantidad equivalente en kilómetros
        """
        # Establecemos las unidades
        self._unidad_origen = "centímetros"
        self._unidad_destino = "kilómetros"
        
        # Utilizamos el método de conversión genérica de la clase padre
        # 1 centímetro = 0.01 en unidad base (metros), 1 kilómetro = 1000 en unidad base
        resultado = self._conversion_generica(cantidad_centimetros, 100, 0.001)
        
        # Mostramos los resultados
        self._mostrar_resultados()
        
        return resultado