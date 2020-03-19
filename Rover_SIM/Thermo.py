import numpy as np
a_pressure = 101325
a_temperature = 279
e_temperature = 294
k = 1.4
C_v = 718
eta_t = 0.40
V = (1.5*0.001)/5
V_ans = (1-eta_t)**((k-1)**-1)*V
T_1 = a_temperature
T_4 = e_temperature
T_2 = ((1-eta_t)**-1)*T_1
T_3 = (T_4*T_2)/T_1
q_in = C_v*(T_3-T_2)
q_out = C_v*(T_4-T_1)

T_1 = np.array([17+273.15, 23+273.15])
T_2 = np.array([575+273.15, 425+273.15])
k = 1.4
CR=((((1-(T_1/T_2))-1)*-1)**((k-1)**-1))**-1

k = np.array([1.44, 1.47])
eta_t = np.array([0.45, 0.5])
CR = ((1-eta_t)**((k-1)**-1))**-1

CR = np.array([10.5, 7.5])
p_1 = np.array([80, 85])*1000
T_1 = np.array([21+273.15, 26+273.15])
T_3 = np.array([1175+273.15, 1200+273.15])
k = 1.4
C_p = 1004
C_v = C_p/k
T_2 = (((1/CR)**(k-1))**-1)*T_1
q_in = C_v*(T_3-T_2)
T_4 = (T_3*T_1)/T_2
q_out = C_v*(T_4-T_1)
eta_t = 1-T_1/T_2

p_2 = np.array([93000, 93300])
T_2 = np.array([275, 285])
comp = np.array([8, 8.25])
p_4 = np.array([721680, 746633.25])
T_4 = np.array([1440, 1470])
C_p = 1000
m_dot = 3
k = 1.4
T_1 = ((comp**((k-1)/k))**-1)*T_2
T_8 = ((comp**((k-1)/k))**-1)*T_4
T_3 = ((comp**((k-1)/k)))*T_2
W_23 = m_dot*C_p*(T_3-T_2)
W_48 = m_dot*C_p*(T_4-T_8)
W_net = W_48-W_23


