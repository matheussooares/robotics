from kinematics.forward.robo import Robo,Elo

# Modelagem da cinemática direta usando Denavit-hartenberg
Elos = [['theta_1',10,0,90,0],
        ['theta_2',0,18,180,0],
        ['theta_3',0,18,-180,0],
        ['theta_4',0,0,90,90],
        ['theta_5',18,0,0,0]
]

Elos = [Elo.revolute(joint_name = 'theta_1', d= 10, a = 0, alpha = 90),
        Elo.revolute(joint_name = 'theta_2', d = 0, a = 18, alpha = 180),
        Elo.revolute(joint_name = 'theta_3', d = 0, a = 18, alpha = -180),
        Elo.revolute(joint_name = 'theta_4', d = 0, a = 0, alpha = 90, phase = 90),
        Elo.revolute(joint_name = 'theta_5', d = 18, a = 0, alpha= 0)
]

robo = Robo(name = "Robo",
            parameters = Elos
)

print(robo.frame([0,0,0,0,0]))