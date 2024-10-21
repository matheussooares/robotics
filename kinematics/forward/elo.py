from sympy import symbols

class Elo:
  """
    Classe que representa um elo físico de um robô, conforme a notação de Denavit-Hartenberg (DH).
    
    Parâmetros:
    ----------
    theta : sympy.Symbol ou float
        Ângulo de rotação em torno do eixo z (em graus).
    d : float
        Distância ao longo do eixo z (em cm).
    a : sympy.Symbol ou float
        Comprimento do elo (em cm).
    alpha : float
        Ângulo de rotação em torno do eixo x comum (em graus).
    phase : float, opcional
        Fase do ângulo de rotação em torno do eixo z (em graus). Padrão é 0.

    Métodos:
    -------
    - revolute: Cria um elo com uma junta revoluta, com rotação variável em torno do eixo z.
    - prismatic: Cria um elo com uma junta prismática, com translação variável ao longo do eixo z.
    
    Exemplo de uso:
    --------------
    >>> from sympy import symbols
    >>> theta = symbols('theta')
    >>> elo = Elo(theta=theta, d=10, a=0, alpha=90, phase=0)
    
    ou para criar elos com juntas revolutas e prismáticas:
    
    >>> elo_revolute = Elo.revolute(joint_name='theta1', d=10, a=0, alpha=90)
    >>> elo_prismatic = Elo.prismatic(joint_name='d2', theta=0, a=5, alpha=0)
    """
  def __init__(self,*, theta, d, a, alpha, phase = 0):
    """
    Inicializa um elo usando os parâmetros DH.

    Parâmetros:
    ----------
    theta : sympy.Symbol or float
        Ângulo de rotação em torno do eixo z (em graus).
    d : float
        Distância ao longo do eixo z (em cm).
    a : float
        Comprimento do elo (em cm).
    alpha : float
        Ângulo de rotação em torno do eixo x comum (em graus).
    phase : float, opcional
        Fase do ângulo de rotação em torno do eixo z (em graus). Padrão é 0.
    """
    self.theta = theta
    self.d = d
    self.a = a
    self.alpha = alpha
    self.phase = phase
  
  @classmethod
  def revolute(cls,*, joint_name: str, d: float, a: float, alpha: float, phase: float = 0):
    """
    Cria um elo com junta revoluta, onde o ângulo theta varia em torno do eixo z.

    Parâmetros:
    ----------
    joint_name : str
        Nome simbólico da junta (usado para definir o ângulo variável theta).
    d : float
        Distância ao longo do eixo z (em cm).
    a : float
        Comprimento do elo (em cm).
    alpha : float
        Ângulo de rotação em torno do eixo x comum (em graus).
    phase : float, opcional
        Fase do ângulo de rotação em torno do eixo z (em graus). Padrão é 0.

    Retorna:
    -------
    Elo : Instância da classe Elo configurada como junta revoluta.
    """
    return cls(theta = symbols(joint_name),
               d = d, 
               a = a, 
               alpha = alpha, 
               phase = phase
    )
  
  @classmethod
  def prismatic(cls, *, joint_name: str, theta: float, a: float, alpha: float, phase: float = 0):
    """
    Cria um elo com junta prismática, onde a distância d varia ao longo do eixo z.

    Parâmetros:
    ----------
    joint_name : str
        Nome simbólico da junta (usado para definir a distância variável d).
    theta : float
        Ângulo de rotação em torno do eixo z (em graus).
    a : float
        Comprimento do elo (em cm).
    alpha : float
        Ângulo de rotação em torno do eixo x comum (em graus).
    phase : float, opcional
        Fase do ângulo de rotação em torno do eixo z (em graus). Padrão é 0.

    Retorna:
    -------
    Elo : Instância da classe Elo configurada como junta prismática.
      """
    return cls(theta = theta,
               d = symbols(joint_name), 
               a = a, 
               alpha = alpha, 
               phase = phase
    )


