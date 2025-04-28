print("-=" * 20)
print("Analisador de Triângulos")
print("-=" * 20)

primeiro_segmento = float(input("Valor do Primeiro Segmento do Triângulo : "))
segundo_segmento = float(input("Valor do Segundo Segmento do Triângulo : "))
terceiro_segmento = float(input("Valor do Terceiro Segmento do Triângulo: "))

if primeiro_segmento < segundo_segmento + terceiro_segmento and segundo_segmento < primeiro_segmento + terceiro_segmento and terceiro_segmento < segundo_segmento + primeiro_segmento:
    print("Os segmentos acima PODEM FORMAR um triângulo!", end="")
    if primeiro_segmento == segundo_segmento == terceiro_segmento:
        print("E o triângulo é EQUILÁTERO")
    elif primeiro_segmento != segundo_segmento and segundo_segmento != terceiro_segmento and terceiro_segmento != primeiro_segmento:
        print("E o triângulo é ESCALENO")
    else:
        print("E o triângulo é ISÓCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")