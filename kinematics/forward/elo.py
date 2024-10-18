class Elo:
  """
    Classe que define um elo físico do rôbo. Essa representação de elo é descrito 
    por meio dos parâmetros da notação de Denavit-Hartenberg (DH).
    
    Os parâmetros que compõem a classe:
      - theta: ângulo de rotação em torno do eixo z (graus)
      - d: distância ao longo do eixo z (cm)
      - a: comprimento do elo (cm)
      - alpha: ângulo de rotação em torno do eixo x comum (graus)
      - phase: fase do ângulo de rotação em torno do eixo z (graus)

    Exemplo:
      import sympy

      theta = sympy.symbols('theta')

      elo = Elo(theta,10,0,90,0)    
  """
  def __init__(self,theta,d,a,alpha,phase):
    self.theta = theta
    self.d = d
    self.a = a
    self.alpha = alpha
    self.phase = phase