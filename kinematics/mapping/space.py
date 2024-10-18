from pandas import DataFrame, concat
from itertools import product
from kinematics.forward.robo import Robo

class Spacemapping:
    def __init__(self, robo: Robo) -> None:
        self._robo = robo
        self._LABELSJOINS = self._robo._JointNames
        self._LABELSOPERATIONAL =  ['R_11','R_12','R_13','p_x','R_21','R_22','R_23','p_y','R_31','R_32','R_33','p_z']

    # Mapeia o espaço da juntas
    def joint_space(self, joins: list, steps: list):
        ranges = [list(range(joins[i][0], joins[i][1] + 1, steps[i])) for i in range(len(joins))]
        
        all_combinations = list(product(*ranges))
        
        data_join = [list(comb) for comb in all_combinations]
        return data_join

    # Mapeia o espaço operacional
    def operational_space(self, data_join: list[list], n_atributos=12, output_format: str = 'list'):
        data = []
        for pose in data_join:
            matrix = self._robo.frame(pose)
            data.append(self.float(matrix[:n_atributos]))
        if output_format == 'DataFrame':
          data = DataFrame(data,columns=self._LABELSOPERATIONAL)
        return data

    # Relaciona os espaços mapeados melhorado
    def space_mapping(self, joins: list, steps: list, n_atributos=12):
        data_joint = self.joint_space(joins, steps) 
        data_operational = self.operational_space(data_joint, n_atributos)
       
        return self.dataframe(data_operational, data_joint)
    
    # Cria um dataframe
    def dataframe(self, data_operational, data_joint):
        df_operacional = DataFrame(data_operational, columns=self._LABELSOPERATIONAL)
        df_joint = DataFrame(data_joint, columns=self._LABELSJOINS)

        return concat([df_joint,df_operacional], axis=1)
    
    # Tranforma os dados em float
    def float(self, list):
        list_float = [float(val) for val in list] 
        return list_float