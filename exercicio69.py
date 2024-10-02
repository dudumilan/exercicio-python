  
import random

def classificacao(times, jogos):
    pontos = {}
    vitorias = {}
    saldo_gols = {}
    gols_pro = {}
    for time in times:
        pontos[time] = 0
        vitorias[time] = 0
        saldo_gols[time] = 0
        gols_pro[time] = 0
    for jogo in jogos:
        time1, time2, gols1, gols2 = jogo
        if gols1 > gols2:
            pontos[time1] += 3
            vitorias[time1] += 1
        elif gols2 > gols1:
            pontos[time2] += 3
            vitorias[time2] += 1
        else:
            pontos[time1] += 1
            pontos[time2] += 1
        saldo_gols[time1] += gols1 - gols2
        saldo_gols[time2] += gols2 - gols1
        gols_pro[time1] += gols1
        gols_pro[time2] += gols2
    classificacao = sorted(times, key=lambda time: (-pontos[time], -vitorias[time], -saldo_gols[time], -gols_pro[time]), reverse=True)
    for i, time in enumerate(classificacao):
        print(f"{i+1}. {time} - Pontos: {pontos[time]}, Vitórias: {vitorias[time]}, Saldo: {saldo_gols[time]}, Gols: {gols_pro[time]}")
    return classificacao