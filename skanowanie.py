import numpy as np

q_cnt = 0
e_cnt = 0
m_cnt = 0
t_cnt = 0
x_cnt = 0
h_cnt = 0
with open('skanowanie.txt', 'r') as f:
    for line in f:
        if line[0] == 'q':
            q_cnt +=1
        elif line[0] == 'e':
            e_cnt +=1
        elif line[0] == 'm':
            m_cnt +=1
        elif line[0] == 't':
            t_cnt +=1
        elif line[0] == 'x':
            x_cnt +=1
        elif line[0] == 'h':
            h_cnt +=1
print('qq', q_cnt, np.sqrt(q_cnt), q_cnt/5, np.sqrt(q_cnt)/5)
print('ee', e_cnt, np.sqrt(e_cnt), e_cnt/5, np.sqrt(e_cnt)/5)
print('mm', m_cnt, round(np.sqrt(m_cnt), 1), m_cnt/5, round(np.sqrt(m_cnt), 1)/5)
print('tt', t_cnt, round(np.sqrt(t_cnt),1), t_cnt/5, round(np.sqrt(t_cnt), 1)/5)
#print('tlo', x_cnt, x_cnt/5)
#print('hold', h_cnt, h_cnt/5)
print('inne', h_cnt + x_cnt, round(np.sqrt(h_cnt + x_cnt),1), (h_cnt+x_cnt)/5, round(np.sqrt(h_cnt + x_cnt),1)/5)
print('suma', q_cnt+e_cnt+m_cnt+t_cnt+x_cnt+h_cnt)