class ConversorBasico:
    def __init__(self):
        self._valor_original = 0
        self._unidad_origen = ""
        self._unidad_destino = ""
        self._valor_convertido = 0
    
    def _conversion_generica(self, cantidad_a_convertir, equivalencia_unidad_origen, equivalencia_unidad_destino):
        """
        Método protegido para realizar conversiones genéricas
        
        Args:
            cantidad_a_convertir: Valor a convertir
            equivalencia_unidad_origen: Equivalencia de la unidad de origen
            equivalencia_unidad_destino: Equivalencia de la unidad de destino
        
        Returns:
            El valor convertido
        """
        # Guardamos los valores en las variables protegidas
        self._valor_original = cantidad_a_convertir
        
        # Realizamos la conversión
        self._valor_convertido = (cantidad_a_convertir * equivalencia_unidad_destino) / equivalencia_unidad_origen
        
        return self._valor_convertido
    
    def _mostrar_resultados(self):
        """
        Método protegido para mostrar los resultados de la conversión
        """
        print(f"{self._valor_original} {self._unidad_origen} son {self._valor_convertido} {self._unidad_destino}")