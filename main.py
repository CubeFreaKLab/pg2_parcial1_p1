from conversor_distancia import ConversorDistancia

def main():
    conversor = ConversorDistancia()
    
    # Método metros_a_centimetros:
    print("\nConversión de metros a centímetros")
    conversor.metros_a_centimetros(10)
    
    # Método centimetros_a_kilometros:
    print("\nConversión de centímetros a kilómetros")
    conversor.centimetros_a_kilometros(1000)

if __name__ == "__main__":
    main()