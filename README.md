# Robotics

Esta biblioteca Python oferece ferramentas para modelar a cinemática direta de manipuladores robóticos utilizando a notação de **Denavit-Hartenberg (DH)**. É possível criar modelos robôs manipuladores e calcular a transformação homogênea que define a posição final do manipulador no espaço tridimensional. 

Além disso, oferece funcionalidades para mapear o **espaço das juntas** (ângulos das articulações) e o **espaço operacional** (posição e orientação do efetuador final), fornecendo a análise de movimentos robóticos e a verificação de configurações de junta.

## Recursos

- **Cinemática Direta**: Calcula a cinemática direta usando parâmetros DH.
- **Mapeamento do Espaço das Juntas**: Gera e analisa o espaço das variáveis de junta.
- **Mapeamento do Espaço Operacional**: Mapeia as posições e orientações no espaço operacional.
- **Customizável**: Funciona para qualquer manipulador definido por um conjunto de parâmetros DH.

## Funções e Classes
1. Elo:

    Representa um elo físico do manipulador baseado nos parâmetros DH.

    Atributos:

        - theta: Ângulo de rotação ao redor do eixo z.
        - d: Deslocamento ao longo do eixo z.
        - a: Comprimento do elo.
        - alpha: Ângulo de torção ao redor do eixo x.
        - phase: Fase do ângulo de rotação ao redor do eixo z.
2. Robo

    Representa o robô completo, composto por vários elos, e permite o cálculo da cinemática direta.

    Métodos:
    - frame(pose): Retorna a matriz de transformação para uma pose dada (configuração das juntas).
    - latex(): Gera a matriz de cinemática direta no formato LaTeX.
3. Spacemapping:

    Fornece ferramentas para mapear os espaços das juntas e operacional.

    Métodos:
        
        - joint_space(joins, steps): Mapeia o espaço das juntas com base nos intervalos e passos das variáveis de junta;
        - operational_space(data_join): Mapeia o espaço operacional para um conjunto de configurações de juntas; 
        - space_mapping(joins, steps): Mapeia simultaneamente os espaços das juntas e operacional;
        - dataframe(data_operational, data_joint): Converte os espaços mapeados em um DataFrame do Pandas para análise.

## Autor 

Matheus Soares