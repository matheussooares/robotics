from sympy import sin, cos, Matrix, symbols, simplify, nsimplify, eye, Symbol, rad, latex
from numpy import radians
from kinematics.forward.elo import Elo

class Robo:
    
    def __init__(self, *, name: str = 'Manipulator', parameters: list):
      self._name = name
      self.series_link(parameters = parameters)
      self.__homogeneous_transformations()
      self.__joints()

    @property
    def matrixForwardKinematics(self):
      return self._matrixForwardKinematics
    
    @property
    def parameters(self):
      return self._parameters
    
    @property
    def name(self):
       return self._name
    
    @property
    def Joints(self):
      return self._JointVariable

    # Cria a cadeia cinemática de elos
    def series_link(self, *, parameters):

      self._parameters = parameters
      serieslink = []
      
      for parameter in self._parameters:
        if isinstance(parameter, Elo): 
          serieslink.append(parameter)
        else: 
          parameter_list = []
          for value in parameter:
              if isinstance(value, str):
                  parameter_list.append(symbols(value))
              else:
                  parameter_list.append(value)
          serieslink.append(Elo(theta = parameter_list[0], 
                                d  = parameter_list[1], 
                                a =  parameter_list[2], 
                                alpha  = parameter_list[3], 
                                phase = parameter_list[4]
                              )
          )
      
      self._serieslink = serieslink

    # Método privado que define a matriz de tranformação total do manipulador
    def __homogeneous_transformations(self):
      matrix_TH = eye(4)
      for Elo in self._serieslink:
        matrix = self.__matrix_homogeneous(Elo)
        matrix_TH = matrix_TH @ matrix
    
      self._matrixForwardKinematics = matrix_TH

      self.simplify_ForwardKinematics()
    
    # Método que aplica uma simplificação na matriz de transformação 
    def simplify_ForwardKinematics(self):
      self._matrixForwardKinematics = simplify(nsimplify(self._matrixForwardKinematics))
    
    # Método privado que cria uma matriz de transformação homogênea de DH genérica
    def __matrix_homogeneous(self,Elo):
        theta = Elo.theta + rad(Elo.phase)
        alpha = rad(Elo.alpha)
        matrix = Matrix([
            [cos(theta), -sin(theta) * cos(alpha), sin(theta) * sin(alpha), Elo.a * cos(theta)],
            [sin(theta), cos(theta) * cos(alpha), -cos(theta) * sin(alpha), Elo.a * sin(theta)],
            [0, sin(alpha), cos(alpha), Elo.d],
            [0, 0, 0, 1]
        ])
        return matrix
    
    # Método privado que coleta informações das variáveis de junta
    def __joints(self):
      joins = []
      names = []
      for elo in self._serieslink:
         for _,val in elo.__dict__.items():
            if isinstance(val, Symbol):
              joins.append(val)
              names.append(val.name)
      
      self._JointVariable = joins
      self._JointNames = names
      self._lenjoin = len(joins)
      
    # Método público que retorna a matriz de transformação de um frame
    def frame(self, pose: list):
      if len(pose) == self._lenjoin:
        pose = radians(pose)
        input = dict(zip(self._JointVariable,pose))
        return self._matrixForwardKinematics.evalf(subs=input)
      else:
         print("Número de entradas inválidos")
    
    def latex(self):
       return latex(self._matrixForwardKinematics)