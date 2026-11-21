from pedido import Pedido, FreteSedex, FretePac, FreteTransportadora, FreteMotoboy, FreteDrone

def main():
    pedido = Pedido(peso_kg=2.5)
    
    pedido.set_estrategia(FreteSedex())
    print(f"Valor do frete SEDEX: R$ {pedido.calcular_frete():.2f}")  

    pedido.set_estrategia(FretePac())
    print(f"Valor do frete PAC: R$ {pedido.calcular_frete():.2f}")  
    
    pedido.set_estrategia(FreteTransportadora())
    print(f"Valor do frete TRANSPORTADORA: R$ {pedido.calcular_frete():.2f}") 
    
    pedido.set_estrategia(FreteMotoboy())
    print(f"Valor do frete MOTOBOY: R$ {pedido.calcular_frete():.2f}") 

    pedido.set_estrategia(FreteDrone())
    print(f"Valor do frete DRONE: R$ {pedido.calcular_frete():.2f}")

if __name__ == "__main__":
    main()