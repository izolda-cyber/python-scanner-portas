import socket

# Lista de portas comuns para escanear
portas_comuns = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 8080]

def escanear_portas(ip):
    print(f"Escaneando {ip}...\n")
    for porta in portas_comuns:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip, porta))
        if resultado == 0:
            print(f"Porta {porta} aberta")
        else:
            print(f"Porta {porta} fechada")
        sock.close()

if __name__ == "__main__":
    ip_alvo = input("Digite o IP para escanear: ")
    escanear_portas(ip_alvo)
